# -*- coding: utf-8 -*-
import unittest
import markdown
from denden_extension import DenDenExtension
import sys
import re
import subprocess


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass
        

    def test_denden_basic(self):
        if sys.version[0] == '2':
            with open('./test/denden_basic_test.txt', 'r') as f:
                denden_basic_text = f.read().decode('utf-8')
            with open('./test/denden_basic_test.html', 'r') as f:
                denden_basic_html = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open('./test/denden_basic_test.txt', 'r', encoding='utf-8') as f:
                denden_basic_text = f.read()
            with open('./test/denden_basic_test.html', 'r', encoding='utf-8') as f:
                denden_basic_html = f.read().strip()
        denden_basic_html_gened = markdown.markdown(denden_basic_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(denden_basic_html, denden_basic_html_gened)


    def test_denden_basic_cmd(self):
        if sys.version[0] == '2':
            with open('./test/denden_basic_test.html', 'r') as f:
                denden_basic_html = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open('./test/denden_basic_test.html', 'r', encoding='utf-8') as f:
                denden_basic_html = f.read().strip()
        denden_basic_html_gened = subprocess.check_output(['python', '-m', 'markdown', '-x', 'markdown.extensions.extra', '-x', 'markdown.extensions.nl2br', '-x', 'markdown.extensions.sane_lists', '-x', 'denden_extension', 'test/denden_basic_test.txt'], universal_newlines=True).strip()

        self.assertEqual(denden_basic_html, denden_basic_html_gened)


    def test_denden_border(self):
        if sys.version[0] == '2':
            with open('./test/denden_border_test.txt', 'r') as f:
                denden_border_text = f.read().decode('utf-8')
            with open('./test/denden_border_test.html', 'r') as f:
                denden_border_html = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open('./test/denden_border_test.txt', 'r', encoding='utf-8') as f:
                denden_border_text = f.read()
            with open('./test/denden_border_test.html', 'r', encoding='utf-8') as f:
                denden_border_html = f.read().strip()
        denden_border_html_gened = markdown.markdown(denden_border_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(denden_border_html, denden_border_html_gened)


    def test_denden_border_cmd(self):
        if sys.version[0] == '2':
            with open('./test/denden_border_test.html', 'r') as f:
                denden_border_html = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open('./test/denden_border_test.html', 'r', encoding='utf-8') as f:
                denden_border_html = f.read().strip()
        denden_border_html_gened = subprocess.check_output(['python', '-m', 'markdown', '-x', 'markdown.extensions.extra', '-x', 'markdown.extensions.nl2br', '-x', 'markdown.extensions.sane_lists', '-x', 'denden_extension', 'test/denden_border_test.txt'], universal_newlines=True).strip()

        self.assertEqual(denden_border_html, denden_border_html_gened)


    def test_kurofunezengo(self):
        if sys.version[0] == '2':
            with open('./test/kurofunezengo_test.txt', 'r') as f:
                kurofunezengo_text = f.read().decode('utf-8')
            with open('./test/kurofunezengo_test.html', 'r') as f:
                kurofunezengo_html = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open('./test/kurofunezengo_test.txt', 'r', encoding='utf-8') as f:
                kurofunezengo_text = f.read()
            with open('./test/kurofunezengo_test.html', 'r', encoding='utf-8') as f:
                kurofunezengo_html = f.read().strip()
        kurofunezengo_html_gened = markdown.markdown(kurofunezengo_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(kurofunezengo_html, kurofunezengo_html_gened)


    def test_kurofunezengo_cmd(self):
        if sys.version[0] == '2':
            with open('./test/kurofunezengo_test.html', 'r') as f:
                kurofunezengo_html = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open('./test/kurofunezengo_test.html', 'r', encoding='utf-8') as f:
                kurofunezengo_html = f.read().strip()
        kurofunezengo_html_gened = subprocess.check_output(['python', '-m', 'markdown', '-x', 'markdown.extensions.extra', '-x', 'markdown.extensions.nl2br', '-x', 'markdown.extensions.sane_lists', '-x', 'denden_extension', 'test/kurofunezengo_test.txt'], universal_newlines=True).strip()

        self.assertEqual(kurofunezengo_html, kurofunezengo_html_gened)


    def test_import_extension_by_name(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'])

        self.assertEqual(expected, actual)


    def test_omit_doc_break_1(self):
        source = u"""==="""
        expected = u"""<p>===</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension(docbreak=False)])

        self.assertEqual(expected, actual)


    def test_omit_doc_break_2(self):
        source = u"""==="""
        expected = u"""<p>===</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'], extension_configs={'denden_extension': {'docbreak': False}})

        self.assertEqual(expected, actual)


    def test_omit_doc_break_3(self):
        source = u"""==="""
        expected = u"""<p>===</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'], extension_configs={'denden_extension:DenDenExtension': {'docbreak': False}})

        self.assertEqual(expected, actual)


    def test_omit_page_num_1(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ[%24]される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension(page_num=False)])

        self.assertEqual(expected, actual)


    def test_omit_page_num_2(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ[%24]される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'], extension_configs={'denden_extension': {'page_num': False}})

        self.assertEqual(expected, actual)


    def test_omit_page_num_3(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ[%24]される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'], extension_configs={'denden_extension:DenDenExtension': {'page_num': False}})

        self.assertEqual(expected, actual)


    def test_omit_footnote_sub_1(self):
        source = u"""これは脚注付き[^1]の段落です。
[^1]: そして、これが脚注です。"""
        expected = u"""<p>これは脚注付き<sup id="fnref:1"><a class="footnote-ref" href="#fn:1" rel="footnote">1</a></sup>の段落です。</p>
<div class="footnote">
<hr />
<ol>
<li id="fn:1">
<p>そして、これが脚注です。&#160;<a class="footnote-backref" href="#fnref:1" rev="footnote" title="Jump back to footnote 1 in the text">&#8617;</a></p>
</li>
</ol>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension(footnote_sub=False)])

        self.assertEqual(expected, actual)


    def test_omit_footnote_sub_2(self):
        source = u"""これは脚注付き[^1]の段落です。
[^1]: そして、これが脚注です。"""
        expected = u"""<p>これは脚注付き<sup id="fnref:1"><a class="footnote-ref" href="#fn:1" rel="footnote">1</a></sup>の段落です。</p>
<div class="footnote">
<hr />
<ol>
<li id="fn:1">
<p>そして、これが脚注です。&#160;<a class="footnote-backref" href="#fnref:1" rev="footnote" title="Jump back to footnote 1 in the text">&#8617;</a></p>
</li>
</ol>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'], extension_configs={'denden_extension': {'footnote_sub': False}})

        self.assertEqual(expected, actual)


    def test_omit_footnote_sub_3(self):
        source = u"""これは脚注付き[^1]の段落です。
[^1]: そして、これが脚注です。"""
        expected = u"""<p>これは脚注付き<sup id="fnref:1"><a class="footnote-ref" href="#fn:1" rel="footnote">1</a></sup>の段落です。</p>
<div class="footnote">
<hr />
<ol>
<li id="fn:1">
<p>そして、これが脚注です。&#160;<a class="footnote-backref" href="#fnref:1" rev="footnote" title="Jump back to footnote 1 in the text">&#8617;</a></p>
</li>
</ol>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'], extension_configs={'denden_extension:DenDenExtension': {'footnote_sub': False}})

        self.assertEqual(expected, actual)


    def test_paragraph(self):
        source = u"""これは段落です。

これは別の段落です。"""
        expected = u"""<p>これは段落です。</p>
<p>これは別の段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_new_line_in_paragraph(self):
        source = u"""これは段落です。
これは段落の続きです。

これは別の段落です。"""
        expected = u"""<p>これは段落です。<br />
これは段落の続きです。</p>
<p>これは別の段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_indent_at_top_of_line(self):
        source = u"""　これは字下げする段落です。

これは字下げしない段落です。"""
        expected = u"""<p>　これは字下げする段落です。</p>
<p>これは字下げしない段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_header_atx(self):
        source = u"""# 見出しレベル1 #

## 見出しレベル2 ##

### 見出しレベル3 ###

#### 見出しレベル4 ####

##### 見出しレベル5 #####

###### 見出しレベル6 ######

### 見出しレベル3"""
        expected = u"""<h1>見出しレベル1</h1>
<h2>見出しレベル2</h2>
<h3>見出しレベル3</h3>
<h4>見出しレベル4</h4>
<h5>見出しレベル5</h5>
<h6>見出しレベル6</h6>
<h3>見出しレベル3</h3>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_header_setext(self):
        source = u"""見出しレベル1
===========

見出しレベル2
-----------

見出しレベル1
==

見出しレベル2
---------------------------"""
        expected = u"""<h1>見出しレベル1</h1>
<h2>見出しレベル2</h2>
<h1>見出しレベル1</h1>
<h2>見出しレベル2</h2>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_quote(self):
        source = u"""これは通常の段落です。

> これは引用された段落です。
>
> これも引用された段落です。

これは通常の段落です。

> これは引用された段落です。
> > これは引用の中でさらに引用された段落です。
> > > > これは引用の中の引用の中の引用の中でさらに引用された段落です。

これは通常の段落です。"""
        expected = u"""<p>これは通常の段落です。</p>
<blockquote>
<p>これは引用された段落です。</p>
<p>これも引用された段落です。</p>
</blockquote>
<p>これは通常の段落です。</p>
<blockquote>
<p>これは引用された段落です。</p>
<blockquote>
<p>これは引用の中でさらに引用された段落です。</p>
<blockquote>
<blockquote>
<p>これは引用の中の引用の中の引用の中でさらに引用された段落です。</p>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
<p>これは通常の段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_1(self):
        source = u"""* りんご
* もも
* みかん"""
        expected = u"""<ul>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_2(self):
        source = u"""+ りんご
+ もも
+ みかん"""
        expected = u"""<ul>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_3(self):
        source = u"""- りんご
- もも
- みかん"""
        expected = u"""<ul>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_ordered_list(self):
        source = u"""1. りんご
2. もも
3. みかん"""
        expected = u"""<ol>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ol>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_ordered_list_escaped(self):
        source = u"""1986\. What a great season."""
        expected = u"""<p>1986. What a great season.</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_with_paragraph(self):
        source = u"""* これは箇条書きの中の段落です。

* これも箇条書きの中の段落です。"""
        expected = u"""<ul>
<li>
<p>これは箇条書きの中の段落です。</p>
</li>
<li>
<p>これも箇条書きの中の段落です。</p>
</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_with_multi_paragraphs(self):
        source = u"""* これは箇条書きの中の最初の段落です。

    これは箇条書きの中の二番目の段落です。

* これは別の箇条書きの中の段落です。"""
        expected = u"""<ul>
<li>
<p>これは箇条書きの中の最初の段落です。</p>
<p>これは箇条書きの中の二番目の段落です。</p>
</li>
<li>
<p>これは別の箇条書きの中の段落です。</p>
</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_with_quote(self):
        source = u"""* これは箇条書きの中の最初の段落です。

    > これは箇条書きの中で引用された段落です。

* これは別の箇条書きの中の段落です。"""
        expected = u"""<ul>
<li>
<p>これは箇条書きの中の最初の段落です。</p>
<blockquote>
<p>これは箇条書きの中で引用された段落です。</p>
</blockquote>
</li>
<li>
<p>これは別の箇条書きの中の段落です。</p>
</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_list_with_code(self):
        source = u"""* これは箇条書きの中の段落です。

        <body>
          <p>Hello world.</p>
        </body>

* これは別の箇条書きの中の段落です。"""
        expected = u"""<ul>
<li>
<p>これは箇条書きの中の段落です。</p>
<pre><code>&lt;body&gt;
  &lt;p&gt;Hello world.&lt;/p&gt;
&lt;/body&gt;
</code></pre>
</li>
<li>
<p>これは別の箇条書きの中の段落です。</p>
</li>
</ul>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_code_block(self):
        source = u"""これは通常の段落です。

    <body>
      <p>Hello world.</p>
    </body>

これは別の段落です。"""
        expected = u"""<p>これは通常の段落です。</p>
<pre><code>&lt;body&gt;
  &lt;p&gt;Hello world.&lt;/p&gt;
&lt;/body&gt;
</code></pre>
<p>これは別の段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_code_inline(self):
        source = u"""段落には`<p>`タグを使います。"""
        expected = u"""<p>段落には<code>&lt;p&gt;</code>タグを使います。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_horizontal_line(self):
        source = u"""* * *

***

*****

---

---------------------------------------

- - -"""
        expected = u"""<hr />
<hr />
<hr />
<hr />
<hr />
<hr />"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_doc_break(self):
        source = u"""これは通常の段落です。

=======================================

## 大見出し ##"""
        expected = u"""<p>これは通常の段落です。</p>
<hr class="docbreak" />
<h2>大見出し</h2>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_page_number_1(self):
        source = u"""[%5]

## 大見出し ##"""
        expected = u"""<div id="pagenum_5" class="pagenum" title="5" epub:type="pagebreak"></div>
<h2>大見出し</h2>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_page_number_2(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ<span id="pagenum_24" class="pagenum" title="24" epub:type="pagebreak"></span>される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_page_number_3(self):
        source = u"""[%%36]

## 大見出し ##"""
        expected = u"""<div id="pagenum_36" class="pagenum" title="36" epub:type="pagebreak">36</div>
<h2>大見出し</h2>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_hyperlink_direct_1(self):
        source = u"""詳しくは[こちら](http://example.com/)をごらんください。"""
        expected = u"""<p>詳しくは<a href="http://example.com/">こちら</a>をごらんください。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_hyperlink_direct_2(self):
        source = u"""詳しくは[こちら](http://example.com/ "タイトル")をごらんください。"""
        expected = u"""<p>詳しくは<a href="http://example.com/" title="タイトル">こちら</a>をごらんください。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_hyperlink_indirect_1(self):
        source = u"""詳しくは[こちら][example]をごらんください。

[example]: http://example.com/"""
        expected = u"""<p>詳しくは<a href="http://example.com/">こちら</a>をごらんください。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_hyperlink_indirect_2(self):
        source = u"""詳しくは[こちら][example]をごらんください。

[example]: http://example.com/ "タイトル\""""
        expected = u"""<p>詳しくは<a href="http://example.com/" title="タイトル">こちら</a>をごらんください。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_hyperlink_indirect_3(self):
        source = u"""オリジナルのMarkdownは[Daring Fireball][]で公開されています。

[Daring Fireball]: http://daringfireball.net/"""
        expected = u"""<p>オリジナルのMarkdownは<a href="http://daringfireball.net/">Daring Fireball</a>で公開されています。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_hyperlink_auto(self):
        source = u"""<http://example.com>

<info@example.com>"""
        expected = r"""<p><a href="http://example.com">http://example.com</a></p>
<p><a href="[&#0-9;xA-E]+?">[&#0-9;xA-E]+?</a></p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertTrue(re.match(expected, actual))


    def test_emphasis_1(self):
        source = u"""これは*強調されたテキスト*です。

これは**重要なテキスト**です。"""
        expected = u"""<p>これは<em>強調されたテキスト</em>です。</p>
<p>これは<strong>重要なテキスト</strong>です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_emphasis_2(self):
        source = u"""これは_強調されたテキスト_です。

これは__重要なテキスト__です。"""
        expected = u"""<p>これは<em>強調されたテキスト</em>です。</p>
<p>これは<strong>重要なテキスト</strong>です。</p>"""
        py_markdown = u"""<p>これは_強調されたテキスト_です。</p>
<p>これは__重要なテキスト__です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        #self.assertEqual(expected, actual)
        self.assertEqual(py_markdown, actual)


    def test_emphasis_3(self):
        source = u"""Please open the folder "secret_magic_box"."""
        expected = u"""<p>Please open the folder "secret_magic_box".</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_ruby_grouped(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_ruby_mono(self):
        source = u"""{電子出版|でん|し|しゅっ|ぱん}を手軽に"""
        expected = u"""<p><ruby>電<rt>でん</rt>子<rt>し</rt>出<rt>しゅっ</rt>版<rt>ぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_ruby_not_1(self):
        source = u"""これは段落です。foo{|bar| bar.buz} これは段落です。"""
        expected = u"""<p>これは段落です。foo{|bar| bar.buz} これは段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_ruby_not_2(self):
        source = u"""これは段落です。\{Info\|Warning\} これは段落です。"""
        expected = u"""<p>これは段落です。&#123;Info&#124;Warning&#125; これは段落です。</p>"""
        py_markdown = u"""<p>これは段落です。{Info|Warning} これは段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_ruby_not_3(self):
        source = u"""これは段落です。{Info\|Warning} これは段落です。"""
        expected = u"""<p>これは段落です。{Info&#124;Warning} これは段落です。</p>"""
        py_markdown = u"""<p>これは段落です。{Info|Warning} これは段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_ruby_not_4(self):
        source = u"""これは段落です。`{Info|Warning}` これは段落です。"""
        expected = u"""<p>これは段落です。<code>{Info|Warning}</code> これは段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_tate_chu_yoko(self):
        source = u"""昭和^53^年"""
        expected = u"""<p>昭和<span class="tcy">53</span>年</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_footenote_1(self):
        source = u"""これは脚注付き[^1]の段落です。

[^1]: そして、これが脚注です。"""
        expected = u"""<p>これは脚注付き<a id="fnref_1" href="#fn_1" rel="footnote" class="noteref" epub:type="noteref">1</a>の段落です。</p>

<div class="footnotes" epub:type="footnotes">
<hr />
<ol>

<li>
<div id="fn_1" class="footnote" epub:type="footnote">
<p>そして、これが脚注です。&#160;<a href="#fnref_1">&#9166;</a></p>
</div>
</li>

</ol>
</div>"""
        py_markdown = u"""<p>これは脚注付き<a id="fnref_1" href="#fn_1" rel="footnote" class="noteref" epub:type="noteref">1</a>の段落です。</p>
<div class="footnotes" epub:type="footnotes">
<hr />
<ol>
<li>
<div id="fn_1" class="footnote" epub:type="footnote">
<p>そして、これが脚注です。&#160;<a href="#fnref_1">&#9166;</a></p>
</div>
</li>
</ol>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_footenote_2(self):
        source = u"""これは脚注付き[^1]の段落です。

[^1]: これは脚注の中の段落です。

    これは同じ脚注の中の別の段落です。"""
        expected = u"""<p>これは脚注付き<a id="fnref_1" href="#fn_1" rel="footnote" class="noteref" epub:type="noteref">1</a>の段落です。</p>

<div class="footnotes" epub:type="footnotes">
<hr />
<ol>

<li>
<div id="fn_1" class="footnote" epub:type="footnote">
<p>これは脚注の中の段落です。</p>

<p>これは同じ脚注の中の別の段落です。&#160;<a href="#fnref_1">&#9166;</a></p>
</div>
</li>

</ol>
</div>"""
        py_markdown = u"""<p>これは脚注付き<a id="fnref_1" href="#fn_1" rel="footnote" class="noteref" epub:type="noteref">1</a>の段落です。</p>
<div class="footnotes" epub:type="footnotes">
<hr />
<ol>
<li>
<div id="fn_1" class="footnote" epub:type="footnote">
<p>これは脚注の中の段落です。</p>
<p>これは同じ脚注の中の別の段落です。&#160;<a href="#fnref_1">&#9166;</a></p>
</div>
</li>
</ol>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_footenote_3(self):
        source = u"""これは脚注付き[^1]の段落です。

[^1]: 
    これは脚注の中の段落です。

    これは同じ脚注の中の別の段落です。"""
        expected = u"""<p>これは脚注付き<a id="fnref_1" href="#fn_1" rel="footnote" class="noteref" epub:type="noteref">1</a>の段落です。</p>

<div class="footnotes" epub:type="footnotes">
<hr />
<ol>

<li>
<div id="fn_1" class="footnote" epub:type="footnote">
<p>これは脚注の中の段落です。</p>

<p>これは同じ脚注の中の別の段落です。&#160;<a href="#fnref_1">&#9166;</a></p>
</div>
</li>

</ol>
</div>

"""
        py_markdown = u"""<p>これは脚注付き<a id="fnref_1" href="#fn_1" rel="footnote" class="noteref" epub:type="noteref">1</a>の段落です。</p>
<div class="footnotes" epub:type="footnotes">
<hr />
<ol>
<li>
<div id="fn_1" class="footnote" epub:type="footnote">
<p>これは脚注の中の段落です。</p>
<p>これは同じ脚注の中の別の段落です。&#160;<a href="#fnref_1">&#9166;</a></p>
</div>
</li>
</ol>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_img_direct_1(self):
        source = u"""![代替テキスト](img.jpg)"""
        expected = u"""<p><img src="img.jpg" alt="代替テキスト" /></p>"""
        py_markdown = u"""<p><img alt="代替テキスト" src="img.jpg" /></p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_img_direct_2(self):
        source = u"""![](img.jpg)"""
        expected = u"""<p><img src="img.jpg" alt="" /></p>"""
        py_markdown = u"""<p><img alt="" src="img.jpg" /></p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_img_indirect(self):
        source = u"""![代替テキスト][id]

[id]: img.jpg"""
        expected = u"""<p><img src="img.jpg" alt="代替テキスト" /></p>
"""
        py_markdown = u"""<p><img alt="代替テキスト" src="img.jpg" /></p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(py_markdown, actual)


    def test_definition_list_1(self):
        source = u"""でんでんマークダウン
:   Markdownをベースにした簡易マークアップ言語

でんでんコンバーター
:   でんでんマークダウンをEPUBに変換するウェブサービス"""
        expected = u"""<dl>
<dt>でんでんマークダウン</dt>
<dd>Markdownをベースにした簡易マークアップ言語</dd>
<dt>でんでんコンバーター</dt>
<dd>でんでんマークダウンをEPUBに変換するウェブサービス</dd>
</dl>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_definition_list_2(self):
        source = u"""でんでんマークダウン
:   「電書ちゃんによる電書ちゃんのためのMarkdown拡張記法およびその実装」の略称
:   Markdownをベースにした簡易マークアップ言語

でんでんコンバーター
:   「電書ちゃんによる電書ちゃんのためのMarkdown拡張記法対応EPUBコンバーター」の略称
:   でんでんマークダウンをEPUBに変換するウェブサービス"""
        expected = u"""<dl>
<dt>でんでんマークダウン</dt>
<dd>「電書ちゃんによる電書ちゃんのためのMarkdown拡張記法およびその実装」の略称</dd>
<dd>Markdownをベースにした簡易マークアップ言語</dd>
<dt>でんでんコンバーター</dt>
<dd>「電書ちゃんによる電書ちゃんのためのMarkdown拡張記法対応EPUBコンバーター」の略称</dd>
<dd>でんでんマークダウンをEPUBに変換するウェブサービス</dd>
</dl>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_definition_list_3(self):
        source = u"""でんでんマークダウン

:   Markdownをベースにした簡易マークアップ言語

でんでんコンバーター

:   でんでんマークダウンをEPUBに変換するウェブサービス"""
        expected = u"""<dl>
<dt>でんでんマークダウン</dt>
<dd>
<p>Markdownをベースにした簡易マークアップ言語</p>
</dd>
<dt>でんでんコンバーター</dt>
<dd>
<p>でんでんマークダウンをEPUBに変換するウェブサービス</p>
</dd>
</dl>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_definition_list_4(self):
        source = u"""項目

:   これは項目を説明した段落です。

    これは項目を説明した別の段落です。

項目

:   下はプログラムのコードです。

        <body>
          <p>Hello world.</p>
        </body>

    > これは項目の説明の中の引用です。

    1. りんご
    2. もも
    3. みかん"""
        expected = u"""<dl>
<dt>項目</dt>
<dd>
<p>これは項目を説明した段落です。</p>
<p>これは項目を説明した別の段落です。</p>
</dd>
<dt>項目</dt>
<dd>
<p>下はプログラムのコードです。</p>
<pre><code>&lt;body&gt;
  &lt;p&gt;Hello world.&lt;/p&gt;
&lt;/body&gt;
</code></pre>
<blockquote>
<p>これは項目の説明の中の引用です。</p>
</blockquote>
<ol>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ol>
</dd>
</dl>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_table(self):
        source = u"""名称    | 人口
------- | ----------
東京都   | 1322万人
大阪府   | 886万人"""
        expected = u"""<table>
<thead>
<tr>
<th>名称</th>
<th>人口</th>
</tr>
</thead>
<tbody>
<tr>
<td>東京都</td>
<td>1322万人</td>
</tr>
<tr>
<td>大阪府</td>
<td>886万人</td>
</tr>
</tbody>
</table>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_html_1(self):
        source = u"""これは段落の中で本の<cite>タイトル</cite>に直接HTMLでマークアップした例です。"""
        expected = u"""<p>これは段落の中で本の<cite>タイトル</cite>に直接HTMLでマークアップした例です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_html_2(self):
        source = u"""これは**通常の段落**です。

<div>
**ブロックの中の段落**はMarkdownが解釈されません。
</div>"""
        expected = u"""<p>これは<strong>通常の段落</strong>です。</p>
<div>
**ブロックの中の段落**はMarkdownが解釈されません。
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_html_3(self):
        source = u"""これは**通常の段落**です。

<div markdown="1">
**ブロックの中の段落**でもMarkdownが解釈されます。
</div>"""
        expected = u"""<p>これは<strong>通常の段落</strong>です。</p>
<div>
<p><strong>ブロックの中の段落</strong>でもMarkdownが解釈されます。</p>
</div>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)


    def test_(self):
        source = u""""""
        expected = u""""""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])

        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
    