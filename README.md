# denden_extension

[Python-Markdown](https://github.com/waylan/Python-Markdown) extention for [Den-Den Markdown](https://github.com/denshoch/DenDenMarkdown).


## requirement

Python-Markdown 2.6 or later.


## install

    pip install denden_extension


## usage

    >>> import markdown
    >>> from denden_extension import DenDenExtension
    >>> markdown.markdown('{電子出版|でんししゅっぱん}を手軽に', extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
    '<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>'

or

    $ python -m markdown -x markdown.extensions.extra -x markdown.extensions.nl2br -x markdown.extensions.sane_lists -x denden_extension input.txt


## features

- Japanese Ruby Annotation: implemented
- Tate-Chu-Yoko: implemented
- Footnotes with epub:type attribute: implemented (requires markdown.extensions.extra or markdown.extensions.footnotes)
- EPUB pagebreak syntax: implemented
- Chunk file syntax: implemented
- Twitter account autolink syntax: NOT implemented

The following is implemented by Python-Markdown (requires markdown.extensions.nl2br).
- GFM style line break


## change log

- 0.1 (2015-08-24) -- first experimental release
