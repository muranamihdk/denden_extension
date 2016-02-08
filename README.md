# denden_extension

Denden_extension is a [Python-Markdown](https://github.com/waylan/Python-Markdown) extension enables [Den-Den Markdown](https://github.com/denshoch/DenDenMarkdown) syntax in Python-Markdown.

## Requirement

Python-Markdown 2.6 or later.


## Install

    pip install denden_extension


## Usage

    >>> import markdown
    >>> from denden_extension import DenDenExtension
    >>> markdown_text = '{電子出版|でんししゅっぱん}を手軽に'
    >>> html_text = markdown.markdown(markdown_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
    >>> html_text
    '<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>'

or

    $ python -m markdown -x markdown.extensions.extra -x markdown.extensions.nl2br -x markdown.extensions.sane_lists -x denden_extension markdown_text.md > html_text.html

## Features

Denden_extension enables the following Den-Den Markdown syntax in Python-Markdown.

- Japanese Ruby Annotation
- Tate-Chu-Yoko
- Footnotes with epub:type attribute (requires markdown.extensions.extra or markdown.extensions.footnotes)
- EPUB pagebreak syntax
- Chunk file syntax

The following is enabled by markdown.extensions.nl2br which is included in Python-Markdown.

- GFM style line break

The following is not implemented in denden_extension.

- Twitter account autolink syntax


## Change log

- 0.1 (2015-08-23) -- first experimental release
