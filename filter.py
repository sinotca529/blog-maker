#!/usr/bin/env python3
import panflute as pf

def html_escape(code: str) -> str:
    map = str.maketrans({
        '&': "&amp;",
        '<': "&lt;",
        '>': "&gt;",
        '"': "&quot;"
    })
    return code.translate(map)

def gen_code_block_html(lang: str, caption: str, code: str) -> str:
    has_lang = len(lang) != 0
    has_caption = len(caption) != 0

    pre_tag_begin = ""
    if has_lang:
        if lang == "rs":
            lang = "rust"
        pre_tag_begin = f'<pre><code class="{lang}">'
    else:
        pre_tag_begin = '<pre><code class="nohljsln txt">'

    fig_caption = ""
    if has_caption:
        fig_caption = f'<figcaption class="code-caption">{caption}</figcaption>'

    # code.replace()
    return "\n<figure>" + fig_caption + pre_tag_begin + html_escape(code) + "</code></pre>" + "</figure>"


def code_block(elem, _doc):
    if isinstance(elem, pf.CodeBlock):
        code = elem.text
        lang = elem.classes[0] if len(elem.classes) > 0 else ""
        caption = elem.attributes.get("caption", "")

        html = gen_code_block_html(lang, caption, code)
        return pf.RawBlock(html)

def main():
    pf.run_filter(code_block)

if __name__ == "__main__":
    main()
