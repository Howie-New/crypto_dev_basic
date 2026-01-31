#!/usr/bin/env python3
"""
AsciiDoc to Markdown 转换脚本
专门针对 https://github.com/inoutcode/bitcoin_book_2nd.git 和 https://github.com/inoutcode/ethereum_book.git 的中文翻译版本
"""

import re
from pathlib import Path


def convert_asciidoc_to_markdown(content: str, filename: str) -> str:
    """将 AsciiDoc 内容转换为 Markdown"""
    lines = content.split('\n')
    result = []
    in_code_block = False
    in_sidebar = False
    in_admonition = None  # 'tip', 'warning', 'note'
    admonition_started = False
    in_latex = False
    code_lang = ''
    sidebar_title = ''

    i = 0
    while i < len(lines):
        line = lines[i]

        # 处理 LaTeX 数学公式块 (前面有 [latexmath] 标记)
        if line.strip() == '[latexmath]':
            in_latex = 'pending'  # 标记等待下一个 ++++ 开始
            i += 1
            continue

        # 处理 ++++ 块
        if line.strip() == '++++':
            if in_latex == 'pending':
                # 开始 LaTeX 块
                result.append('')
                result.append('$$')
                in_latex = 'content'
            elif in_latex == 'content':
                # 结束 LaTeX 块
                result.append('$$')
                in_latex = False
            else:
                # HTML passthrough 块，直接输出内容
                i += 1
                while i < len(lines) and lines[i].strip() != '++++':
                    result.append(lines[i])
                    i += 1
            i += 1
            continue

        if in_latex == 'content':
            result.append(line)
            i += 1
            continue

        # 处理代码块开始标记 [source,lang]
        source_match = re.match(r'\[source,\s*(\w+)\]', line.strip())
        if source_match:
            code_lang = source_match.group(1)
            i += 1
            continue

        # 处理代码块 ----
        if line.strip() == '----':
            if in_code_block:
                result.append('```')
                in_code_block = False
                code_lang = ''
            else:
                if code_lang:
                    result.append(f'```{code_lang}')
                else:
                    result.append('```')
                in_code_block = True
            i += 1
            continue

        # 在代码块内，原样输出
        if in_code_block:
            result.append(line)
            i += 1
            continue

        # 处理提示框标记 [TIP] / [WARNING] / [NOTE]
        if line.strip() == '[TIP]':
            in_admonition = 'tip'
            admonition_started = False
            i += 1
            continue
        if line.strip() == '[WARNING]':
            in_admonition = 'warning'
            admonition_started = False
            i += 1
            continue
        if line.strip() == '[NOTE]':
            in_admonition = 'note'
            admonition_started = False
            i += 1
            continue

        # 处理 ==== 块边界
        if line.strip() in ['====', '=====================================================================']:
            if in_admonition and not admonition_started:
                # 开始提示框内容
                result.append('')
                if in_admonition == 'tip':
                    result.append('> **提示:**')
                elif in_admonition == 'warning':
                    result.append('> **警告:**')
                elif in_admonition == 'note':
                    result.append('> **注意:**')
                admonition_started = True
            elif in_admonition and admonition_started:
                # 结束提示框
                in_admonition = None
                admonition_started = False
                result.append('')
            i += 1
            continue

        # 在提示框内容中
        if in_admonition and admonition_started:
            if line.strip():
                result.append('> ' + convert_inline(line.strip()))
            else:
                result.append('>')
            i += 1
            continue

        # 处理侧边栏 .title + ****
        if line.startswith('.') and not line.startswith('..') and i + 1 < len(lines):
            potential_title = line[1:].strip()
            if potential_title and lines[i + 1].strip() == '****':
                sidebar_title = potential_title
                in_sidebar = True
                result.append('')
                result.append(f'> **{sidebar_title}**')
                result.append('>')
                i += 2
                continue

        # 处理 **** 块边界
        if line.strip() == '****':
            if in_sidebar:
                in_sidebar = False
                result.append('')
            i += 1
            continue

        # 在侧边栏内容中
        if in_sidebar:
            if line.strip():
                result.append('> ' + convert_inline(line.strip()))
            else:
                result.append('>')
            i += 1
            continue

        # 跳过属性行
        if re.match(r'^\[role=', line.strip()):
            i += 1
            continue

        # 跳过 include 指令
        if line.strip().startswith('include::'):
            i += 1
            continue

        # 处理锚点 [[anchor]]
        anchor_match = re.match(r'^\[\[([^\]]+)\]\]$', line.strip())
        if anchor_match:
            anchor_id = anchor_match.group(1)
            result.append(f'<a id="{anchor_id}"></a>')
            i += 1
            continue

        # 处理标题
        title_match = re.match(r'^(=+)\s+(.+)$', line)
        if title_match:
            level = len(title_match.group(1))
            title_text = title_match.group(2)
            result.append('')
            result.append('#' * level + ' ' + convert_inline(title_text))
            result.append('')
            i += 1
            continue

        # 处理图片标题行 (单独的 .title)
        if line.startswith('.') and not line.startswith('..'):
            potential_caption = line[1:].strip()
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('image::'):
                # 这是图片标题，跳过（图片处理时会处理）
                i += 1
                continue

        # 处理定义列表 term::
        def_match = re.match(r'^(.+?)::(.*)$', line)
        if def_match and not line.strip().startswith('http') and not line.strip().startswith('image:'):
            term = def_match.group(1).strip()
            desc = def_match.group(2).strip()
            result.append('')
            result.append(f'**{convert_inline(term)}**')
            if desc:
                result.append(f': {convert_inline(desc)}')
            result.append('')
            i += 1
            continue

        # 处理表格
        if line.strip().startswith('|==='):
            # 简单处理：收集表格内容
            table_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('|==='):
                if lines[i].strip():
                    table_lines.append(lines[i])
                i += 1
            i += 1  # 跳过结束的 |===

            # 转换表格
            if table_lines:
                md_table = convert_table(table_lines)
                result.extend(md_table)
            continue

        # 处理普通行
        converted_line = convert_inline(line)
        result.append(converted_line)
        i += 1

    return '\n'.join(result)


def convert_table(table_lines: list) -> list:
    """转换 AsciiDoc 表格为 Markdown 表格"""
    rows = []
    current_row = []

    for line in table_lines:
        cells = re.split(r'\s*\|\s*', line.strip())
        cells = [c for c in cells if c]  # 移除空单元格
        if cells:
            current_row.extend(cells)
            # 检查是否是完整行（简化处理）
            if len(current_row) >= 2:
                rows.append(current_row[:])
                current_row = []

    if not rows:
        return []

    result = []
    # 表头
    result.append('| ' + ' | '.join(convert_inline(c) for c in rows[0]) + ' |')
    result.append('| ' + ' | '.join('---' for _ in rows[0]) + ' |')
    # 数据行
    for row in rows[1:]:
        result.append('| ' + ' | '.join(convert_inline(c) for c in row) + ' |')

    return result


def convert_inline(text: str) -> str:
    """转换行内格式"""

    # 移除索引标记 ((("term"))) 和相关变体
    text = re.sub(r'\(\(\([^)]*\)\)\)', '', text)
    text = re.sub(r'\(\("[^"]*"\)\)', '', text)
    # 清理空括号 ()
    text = re.sub(r'\(\)', '', text)

    # 处理图片 image::path["alt"] 或 image::path["alt",options]
    def replace_image(m):
        path = m.group(1)
        alt = m.group(2) if m.group(2) else ''
        # 清理 alt 文本中的引号
        alt = alt.strip('"\'')
        return f'![{alt}]({path})'

    text = re.sub(r'image::([^\[]+)\["([^"]*)"[^\]]*\]', replace_image, text)
    text = re.sub(r'image::([^\[]+)\[([^\]]*)\]', replace_image, text)

    # 处理带文本的外部链接 http://url[text] 或 https://url[text]
    def replace_link(m):
        url = m.group(1)
        link_text = m.group(2)
        return f'[{link_text}]({url})'

    text = re.sub(r'(https?://[^\[]+)\[([^\]]+)\]', replace_link, text)

    # 处理章节内部链接 <<file#,text>> 或 <<file#anchor,text>>
    def replace_chapter_link(m):
        target = m.group(1) if m.group(1) else ''
        anchor = m.group(2) if m.group(2) else ''
        link_text = m.group(3)
        if target:
            md_file = target + '.md'
            if anchor:
                return f'[{link_text}]({md_file}#{anchor})'
            return f'[{link_text}]({md_file})'
        return f'[{link_text}](#{anchor})'

    text = re.sub(r'<<([^#>]*)#([^,>]*),([^>]+)>>', replace_chapter_link, text)

    # 处理简单锚点链接 <<anchor,text>>
    def replace_anchor_link(m):
        anchor = m.group(1)
        link_text = m.group(2)
        return f'[{link_text}](#{anchor})'

    text = re.sub(r'<<([^,>]+),([^>]+)>>', replace_anchor_link, text)

    # 处理只有锚点的链接 <<anchor>>
    text = re.sub(r'<<([^>]+)>>', lambda m: f'[{m.group(1)}](#{m.group(1)})', text)

    # 处理脚注 footnote:[text]
    text = re.sub(r'footnote:\[([^\]]+)\]', r' (\1)', text)

    # 处理等宽字体 +text+ -> `text`
    text = re.sub(r'\+([^+\n]+)\+', r'`\1`', text)

    # 处理 pass:[...] 直接输出内容
    text = re.sub(r'pass:\[([^\]]+)\]', r'\1', text)

    # 清理多余空格
    text = re.sub(r'  +', ' ', text)
    # 清理行首空格（如果不是列表项）
    text = text.strip()

    return text


def process_file(input_path: Path, output_path: Path):
    """处理单个文件"""
    print(f'转换: {input_path.name} -> {output_path.name}')
    content = input_path.read_text(encoding='utf-8')
    md_content = convert_asciidoc_to_markdown(content, input_path.name)
    output_path.write_text(md_content, encoding='utf-8')


def main():
    """主函数"""
    base_dir = Path(__file__).parent

    # 获取所有 .asciidoc 文件
    asciidoc_files = sorted(base_dir.glob('*.asciidoc'))

    print(f'找到 {len(asciidoc_files)} 个 AsciiDoc 文件')
    print('-' * 50)

    for adoc_file in asciidoc_files:
        md_file = adoc_file.with_suffix('.md')
        process_file(adoc_file, md_file)

    print('-' * 50)
    print('转换完成!')
    print(f'生成了 {len(asciidoc_files)} 个 Markdown 文件')


if __name__ == '__main__':
    main()
