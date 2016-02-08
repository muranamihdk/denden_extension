# denden_extension

Denden_extension is a [Python-Markdown](https://github.com/waylan/Python-Markdown) extension enables [Den-Den Markdown](https://github.com/denshoch/DenDenMarkdown) syntax in Python-Markdown.


## Requirement

Python-Markdown 2.6 or later.


## Install
```
pip install denden_extension
```


## Usage
```
>>> import markdown
>>> from denden_extension import DenDenExtension
>>> markdown_text = '{電子出版|でんししゅっぱん}を手軽に'
>>> html_text = markdown.markdown(markdown_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
>>> html_text
'<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>'
```
or
```
python -m markdown -x markdown.extensions.extra -x markdown.extensions.nl2br -x markdown.extensions.sane_lists -x denden_extension markdown_text.md > html_text.html
```

## Description

Den-Den Markdown is an extended Markdown syntax fitted for Japanese and EPUB publishing.  
Denden_extension enables the following syntax of Den-Den Markdown in Python-Markdown.

- [Japanese Ruby Annotation](http://conv.denshochan.com/markdown#ruby)
- [Tate-Chu-Yoko](http://conv.denshochan.com/markdown#tcy)
- [Footnotes with epub:type attribute](http://conv.denshochan.com/markdown#footnotes)*1
- [EPUB pagebreak syntax](http://conv.denshochan.com/markdown#pagebreak)
- [Chunk file syntax](http://conv.denshochan.com/markdown#docbreak)*2

*1 Denden_extension depends on the Python-Markdown's footnotes extension for implementing this feature. So you also need the [markdown.extensions.footnotes](https://pythonhosted.org/Markdown/extensions/footnotes.html) or [markdown.extensions.extra](https://pythonhosted.org/Markdown/extensions/extra.html) which includes the footnotes extension.  
*2 Three or more equal signs on a line by themselves is replaced by a horizontal rule tag with docbreak class attribute(<hr class="docbreak" />).

Den-Den Markdown inherits its syntax from [PHP Markdown Extra](https://michelf.ca/projects/php-markdown/extra/). In Python-Markdown, [markdown.extensions.extra](https://pythonhosted.org/Markdown/extensions/extra.html) and [markdown.extensions.sane_lists](https://pythonhosted.org/Markdown/extensions/sane_lists.html), which are included in the Python-Markdown Library, enable PHP Markdown Extra syntax.  
Also, Den-Den Markdown adopts GFM style line break. This can be enabled by [markdown.extensions.nl2br](https://pythonhosted.org/Markdown/extensions/nl2br.html), which is also included with the Python-Markdown.

The following syntax of Den-Den Markdown is not implemented in denden_extension.

- Twitter account autolink syntax

About the details of Den-Den Markdown syntax, see http://conv.denshochan.com/markdown (Japanese).

## Change log

- 0.1 (2015-08-23) -- first experimental release
