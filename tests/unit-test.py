# -*- coding: utf-8 -*-
import sys
import re
import subprocess
import unittest
import markdown
from denden_extension import DenDenExtension



class DenDenExtensionTestCases(unittest.TestCase):

    def setUp(self):
        pass


    ###
    ###  The Utility Functions for the Test 
    ###  ----------------------------------------------


    def assert_equal_with_files(self, mdfile, htmlfile):
        if sys.version[0] == '2':
            with open(mdfile, 'r') as f:
                md_text = f.read().decode('utf-8')
            with open(htmlfile, 'r') as f:
                html_text = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open(mdfile, 'r', encoding='utf-8') as f:
                md_text = f.read()
            with open(htmlfile, 'r', encoding='utf-8') as f:
                html_text = f.read().strip()
        html_text_gened = markdown.markdown(md_text, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
        self.assertEqual(html_text, html_text_gened)


    def assert_equal_with_files_cmd(self, mdfile, htmlfile):
        if sys.version[0] == '2':
            with open(htmlfile, 'r') as f:
                html_text = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open(htmlfile, 'r', encoding='utf-8') as f:
                html_text = f.read().strip()
        html_text_gened = subprocess.check_output(['python', '-m', 'markdown', '-x', 'markdown.extensions.extra', '-x', 'markdown.extensions.nl2br', '-x', 'markdown.extensions.sane_lists', '-x', 'denden_extension', mdfile], universal_newlines=True).strip()
        if sys.version[0] == '2':
            html_text_gened = html_text_gened.decode('utf-8')
        self.assertEqual(html_text, html_text_gened)


    def assert_equal(self, source, expected):
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
        self.assertEqual(expected, actual)


    def assert_true(self, source, expected):
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
        self.assertTrue(re.match(expected, actual))



    ###
    ###  The Test Functions Start Here
    ###  ----------------------------------------------
    

    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # 素のPython-Markdownを使った場合でも、でんでんコンバーターとは出力に違いがあることの確認（denden_extensionのせいではなく、Python-Markdownの仕様であることの確認）
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    #でんでんマークダウン：ブロックの間には、空行が1行置かれる（ソースでは2行以上の空行でも、1行になる）
    #Python-Markdown：ブロックの間には、空行は置かれない（仮にソースで2行以上の空行を置いていた場合でも、ブロック間の空行はなくなる）
    def test_paragraph_with_plain_python_markdown(self):
        source = u"""これは段落です。

これは別の段落です。"""
        denden_markdown = u"""<p>これは段落です。</p>

<p>これは別の段落です。</p>"""
        py_markdown = u"""<p>これは段落です。</p>
<p>これは別の段落です。</p>"""
        actual = markdown.markdown(source)
        self.assertEqual(py_markdown, actual)


    #上記の仕様は、出力フォーマットを変えても同じ
    def test_paragraph_with_plain_python_markdown_html5(self):
        source = u"""これは段落です。

これは別の段落です。"""
        denden_markdown = u"""<p>これは段落です。</p>

<p>これは別の段落です。</p>"""
        py_markdown = u"""<p>これは段落です。</p>
<p>これは別の段落です。</p>"""
        actual = markdown.markdown(source, output_format="html5")
        self.assertEqual(py_markdown, actual)


    #でんでんマークダウン：入れ子になったブロックの下位ブロックは、インデントされる
    #Python-Markdown：



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # Python-Markdownの複数の実行方法のいずれでも、denden_extensionが使えることのテスト
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    
    #コマンドラインから実行
    #=> 他のテストで検証されているので省略

    #モジュールとして実行: markdown.markdownメソッドを使用 
    #=> 他のテストで検証されているので省略

    #モジュールとして実行: markdown.markdownFromFileメソッドを使用: テキストは「黒船前後」
    def test_denden_basic_markdownFromFile(self):
        markdown.markdownFromFile(
            input='./tests/kurofunezengo_test.txt',
            output='./tests/output_temp.html',
            encoding='utf-8',
            extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
        htmlfile = './tests/kurofunezengo_test.html'
        if sys.version[0] == '2':
            with open(htmlfile, 'r') as f:
                html_text = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open(htmlfile, 'r', encoding='utf-8') as f:
                html_text = f.read().strip()
        outputfile = './tests/output_temp.html'
        if sys.version[0] == '2':
            with open(outputfile, 'r') as f:
                html_text_gened = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open(outputfile, 'r', encoding='utf-8') as f:
                html_text_gened = f.read().strip()
        self.assertEqual(html_text, html_text_gened)


    #モジュールとして実行: markdown.Markdownクラスを使用



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    #モジュールとして実行する際に、下記3つのいずれの方法でもdenden_extensionの指定が可能であることのテスト
    # 1. extensionクラスのインスタンスを渡す
    # 2. extensionモジュール名を文字列で渡す
    # 3. extensionクラス名を文字列で渡す
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    #1. extensionクラスのインスタンスを渡す
    def test_import_extension_by_class_instance(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension()])
        self.assertEqual(expected, actual)


    #2. extensionモジュール名を文字列で渡す
    def test_import_extension_by_module_name(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'])
        self.assertEqual(expected, actual)


    #3. extensionクラス名を文字列で渡す
    def test_import_extension_by_class_name(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'])
        self.assertEqual(expected, actual)


    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    #denden_extension以外のextensionを外した場合でも正常に動くことのテスト
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    def test_omit_extra_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'])
        self.assertEqual(expected, actual)


    def test_omit_nl2br_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.sane_lists', 'denden_extension'])
        self.assertEqual(expected, actual)


    def test_omit_sane_lists_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'denden_extension'])
        self.assertEqual(expected, actual)


    def test_omit_extra_nl2br_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.sane_lists', 'denden_extension'])
        self.assertEqual(expected, actual)


    def test_omit_extra_sane_lists_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.nl2br', 'denden_extension'])
        self.assertEqual(expected, actual)


    def test_omit_nl2br_sane_lists_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'denden_extension'])
        self.assertEqual(expected, actual)


    def test_omit_all_other_extension_1(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""
        actual = markdown.markdown(source, extensions=['denden_extension'])
        self.assertEqual(expected, actual)



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # オプションが正常に機能しているかのテスト
    #
    #オプションを複数渡す場合のテストも追加すること。
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    #オプション指定のテスト1：docbreak：書式1（モジュール＋クラス）
    def test_omit_doc_break_1(self):
        source = u"""==="""
        expected = u"""<p>===</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension(docbreak=False)])
        self.assertEqual(expected, actual)


    #オプション指定のテスト1：docbreak：書式2（モジュール＋文字列1）
    def test_omit_doc_break_2(self):
        source = u"""==="""
        expected = u"""<p>===</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'], extension_configs={'denden_extension': {'docbreak': False}})
        self.assertEqual(expected, actual)


    #オプション指定のテスト1：docbreak：書式3（モジュール＋文字列2）
    def test_omit_doc_break_3(self):
        source = u"""==="""
        expected = u"""<p>===</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'], extension_configs={'denden_extension:DenDenExtension': {'docbreak': False}})
        self.assertEqual(expected, actual)


    #オプション指定のテスト2：pagenum：書式1（モジュール＋クラス）
    def test_omit_page_num_1(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ[%24]される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension(pagenum=False)])
        self.assertEqual(expected, actual)


    #オプション指定のテスト2：pagenum：書式2（モジュール＋文字列1）
    def test_omit_page_num_2(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ[%24]される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'], extension_configs={'denden_extension': {'pagenum': False}})
        self.assertEqual(expected, actual)


    #オプション指定のテスト2：pagenum：書式3（モジュール＋文字列2）
    def test_omit_page_num_3(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ[%24]される段落です。</p>"""
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'], extension_configs={'denden_extension:DenDenExtension': {'pagenum': False}})
        self.assertEqual(expected, actual)


    #オプション指定のテスト3：footnote：書式1（モジュール＋クラス）
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
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', DenDenExtension(footnote=False)])
        self.assertEqual(expected, actual)


    #オプション指定のテスト3：footnote：書式2（モジュール＋文字列1）
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
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension'], extension_configs={'denden_extension': {'footnote': False}})
        self.assertEqual(expected, actual)


    #オプション指定のテスト3：footnote：書式3（モジュール＋文字列2）
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
        actual = markdown.markdown(source, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists', 'denden_extension:DenDenExtension'], extension_configs={'denden_extension:DenDenExtension': {'footnote': False}})
        self.assertEqual(expected, actual)


    #オプション指定のテスト4：すべてオフ：（コマンドラインから）
    def test_omit_all_denden_basic_cmd(self):
        mdfile = './tests/denden_basic_test.txt'
        htmlfile = './tests/denden_basic_test_for_omit_all_option_cmd.html'
        if sys.version[0] == '2':
            with open(htmlfile, 'r') as f:
                html_text = f.read().decode('utf-8').strip()
        elif sys.version[0] == '3':
            with open(htmlfile, 'r', encoding='utf-8') as f:
                html_text = f.read().strip()
        html_text_gened = subprocess.check_output(['python', '-m', 'markdown', '-x', 'markdown.extensions.extra', '-x', 'markdown.extensions.nl2br', '-x', 'markdown.extensions.sane_lists', '-x', 'denden_extension', '-c', './tests/config.json', mdfile], universal_newlines=True).strip()
        if sys.version[0] == '2':
            html_text_gened = html_text_gened.decode('utf-8')
        self.assertEqual(html_text, html_text_gened)



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # ファイルに記載されたある程度まとまった量のマークダウンテキストを変換するテスト
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    #でんでんエディターにデフォルトで表示されている記述例をテストとして移植（モジュールとして実行）
    # ただし改ページとページ番号のテストを追加してある
    def test_denden_basic(self):
        mdfile = './tests/denden_basic_test.txt'
        htmlfile = './tests/denden_basic_test.html'
        self.assert_equal_with_files(mdfile, htmlfile)


    #でんでんエディターにデフォルトで表示されている記述例をテストとして移植（コマンドラインから実行）
    # ただし改ページとページ番号のテストを追加してある
    def test_denden_basic_cmd(self):
        mdfile = './tests/denden_basic_test.txt'
        htmlfile = './tests/denden_basic_test.html'
        self.assert_equal_with_files_cmd(mdfile, htmlfile)


    #思いつく極端な事例（境界例）（モジュールとして実行）
    def test_denden_border(self):
        mdfile = './tests/denden_border_test.txt'
        htmlfile = './tests/denden_border_test.html'
        self.assert_equal_with_files(mdfile, htmlfile)


    #思いつく極端な事例（境界例）（コマンドラインから実行）
    def test_denden_border_cmd(self):
        mdfile = './tests/denden_border_test.txt'
        htmlfile = './tests/denden_border_test.html'
        self.assert_equal_with_files_cmd(mdfile, htmlfile)


    #でんでんコンバーターのDownloadsのページにある変換用サンプル「黒船前後」（モジュールとして実行）
    def test_kurofunezengo(self):
        mdfile = './tests/kurofunezengo_test.txt'
        htmlfile = './tests/kurofunezengo_test.html'
        self.assert_equal_with_files(mdfile, htmlfile)


    #でんでんコンバーターのDownloadsのページにある変換用サンプル「黒船前後」（コマンドラインから実行）
    def test_kurofunezengo_cmd(self):
        mdfile = './tests/kurofunezengo_test.txt'
        htmlfile = './tests/kurofunezengo_test.html'
        self.assert_equal_with_files_cmd(mdfile, htmlfile)



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # でんでんマークダウン固有のシンタックスの単体テスト
    # でんでんマークダウンの記法の解説ページより移植
    # http://conv.denshochan.com/markdown
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    # ルビ
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    def test_ruby_grouped(self):
        source = u"""{電子出版|でんししゅっぱん}を手軽に"""
        expected = u"""<p><ruby>電子出版<rt>でんししゅっぱん</rt></ruby>を手軽に</p>"""

        self.assert_equal(source, expected)


    def test_ruby_mono(self):
        source = u"""{電子出版|でん|し|しゅっ|ぱん}を手軽に"""
        expected = u"""<p><ruby>電<rt>でん</rt>子<rt>し</rt>出<rt>しゅっ</rt>版<rt>ぱん</rt></ruby>を手軽に</p>"""

        self.assert_equal(source, expected)


    def test_ruby_not_1(self):
        source = u"""これは段落です。foo{|bar| bar.buz} これは段落です。"""
        expected = u"""<p>これは段落です。foo{|bar| bar.buz} これは段落です。</p>"""

        self.assert_equal(source, expected)


    def test_ruby_not_2(self):
        source = u"""これは段落です。\{Info\|Warning\} これは段落です。"""
        expected = u"""<p>これは段落です。&#123;Info&#124;Warning&#125; これは段落です。</p>"""
        py_markdown = u"""<p>これは段落です。{Info|Warning} これは段落です。</p>"""

        self.assert_equal(source, py_markdown)


    def test_ruby_not_3(self):
        source = u"""これは段落です。{Info\|Warning} これは段落です。"""
        expected = u"""<p>これは段落です。{Info&#124;Warning} これは段落です。</p>"""
        py_markdown = u"""<p>これは段落です。{Info|Warning} これは段落です。</p>"""

        self.assert_equal(source, py_markdown)


    def test_ruby_not_4(self):
        source = u"""これは段落です。`{Info|Warning}` これは段落です。"""
        expected = u"""<p>これは段落です。<code>{Info|Warning}</code> これは段落です。</p>"""

        self.assert_equal(source, expected)


    # 縦中横
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    def test_tate_chu_yoko(self):
        source = u"""昭和^53^年"""
        expected = u"""<p>昭和<span class="tcy">53</span>年</p>"""

        self.assert_equal(source, expected)


    # 脚注
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

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

        self.assert_equal(source, py_markdown)


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

        self.assert_equal(source, py_markdown)


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

        self.assert_equal(source, py_markdown)



    def test_footenote_1_with_footnotes_ext(self):
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

        actual = markdown.markdown(source, extensions=['markdown.extensions.footnotes', 'markdown.extensions.nl2br', DenDenExtension()])
        self.assertEqual(py_markdown, actual)


    def test_footenote_2_with_only_footnotes_ext(self):
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

        actual = markdown.markdown(source, extensions=['markdown.extensions.footnotes', 'markdown.extensions.nl2br', DenDenExtension()])
        self.assertEqual(py_markdown, actual)


    def test_footenote_3_with_footnotes_ext(self):
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

        actual = markdown.markdown(source, extensions=['markdown.extensions.footnotes', 'markdown.extensions.nl2br', DenDenExtension()])
        self.assertEqual(py_markdown, actual)


    # 改ページ（ファイル分割）
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    def test_doc_break(self):
        source = u"""これは通常の段落です。

=======================================

## 大見出し ##"""
        expected = u"""<p>これは通常の段落です。</p>
<hr class="docbreak" />
<h2>大見出し</h2>"""

        self.assert_equal(source, expected)


    # ページ番号
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    def test_page_number_1(self):
        source = u"""[%5]

## 大見出し ##"""
        expected = u"""<div id="pagenum_5" class="pagenum" title="5" epub:type="pagebreak"></div>
<h2>大見出し</h2>"""

        self.assert_equal(source, expected)


    def test_page_number_2(self):
        source = u"""これは途中で改ページ[%24]される段落です。"""
        expected = u"""<p>これは途中で改ページ<span id="pagenum_24" class="pagenum" title="24" epub:type="pagebreak"></span>される段落です。</p>"""

        self.assert_equal(source, expected)


    def test_page_number_3(self):
        source = u"""[%%36]

## 大見出し ##"""
        expected = u"""<div id="pagenum_36" class="pagenum" title="36" epub:type="pagebreak">36</div>
<h2>大見出し</h2>"""

        self.assert_equal(source, expected)



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # でんでんマークダウン中の、オリジナルのマークダウンおよびPHP拡張マークダウンを継承したシンタックス部分のテスト
    # でんでんマークダウンの記法の解説ページより移植
    # http://conv.denshochan.com/markdown
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=


    def test_paragraph(self):
        source = u"""これは段落です。

これは別の段落です。"""
        expected = u"""<p>これは段落です。</p>
<p>これは別の段落です。</p>"""

        self.assert_equal(source, expected)


    def test_new_line_in_paragraph(self):
        source = u"""これは段落です。
これは段落の続きです。

これは別の段落です。"""
        expected = u"""<p>これは段落です。<br />
これは段落の続きです。</p>
<p>これは別の段落です。</p>"""

        self.assert_equal(source, expected)


    def test_indent_at_top_of_line(self):
        source = u"""　これは字下げする段落です。

これは字下げしない段落です。"""
        expected = u"""<p>　これは字下げする段落です。</p>
<p>これは字下げしない段落です。</p>"""

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


    def test_list_1(self):
        source = u"""* りんご
* もも
* みかん"""
        expected = u"""<ul>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ul>"""

        self.assert_equal(source, expected)


    def test_list_2(self):
        source = u"""+ りんご
+ もも
+ みかん"""
        expected = u"""<ul>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ul>"""

        self.assert_equal(source, expected)


    def test_list_3(self):
        source = u"""- りんご
- もも
- みかん"""
        expected = u"""<ul>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ul>"""

        self.assert_equal(source, expected)


    def test_ordered_list(self):
        source = u"""1. りんご
2. もも
3. みかん"""
        expected = u"""<ol>
<li>りんご</li>
<li>もも</li>
<li>みかん</li>
</ol>"""

        self.assert_equal(source, expected)


    def test_ordered_list_escaped(self):
        source = u"""1986\. What a great season."""
        expected = u"""<p>1986. What a great season.</p>"""

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


    def test_code_inline(self):
        source = u"""段落には`<p>`タグを使います。"""
        expected = u"""<p>段落には<code>&lt;p&gt;</code>タグを使います。</p>"""

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


    def test_hyperlink_direct_1(self):
        source = u"""詳しくは[こちら](http://example.com/)をごらんください。"""
        expected = u"""<p>詳しくは<a href="http://example.com/">こちら</a>をごらんください。</p>"""

        self.assert_equal(source, expected)


    def test_hyperlink_direct_2(self):
        source = u"""詳しくは[こちら](http://example.com/ "タイトル")をごらんください。"""
        expected = u"""<p>詳しくは<a href="http://example.com/" title="タイトル">こちら</a>をごらんください。</p>"""

        self.assert_equal(source, expected)


    def test_hyperlink_indirect_1(self):
        source = u"""詳しくは[こちら][example]をごらんください。

[example]: http://example.com/"""
        expected = u"""<p>詳しくは<a href="http://example.com/">こちら</a>をごらんください。</p>"""

        self.assert_equal(source, expected)


    def test_hyperlink_indirect_2(self):
        source = u"""詳しくは[こちら][example]をごらんください。

[example]: http://example.com/ "タイトル\""""
        expected = u"""<p>詳しくは<a href="http://example.com/" title="タイトル">こちら</a>をごらんください。</p>"""

        self.assert_equal(source, expected)


    def test_hyperlink_indirect_3(self):
        source = u"""オリジナルのMarkdownは[Daring Fireball][]で公開されています。

[Daring Fireball]: http://daringfireball.net/"""
        expected = u"""<p>オリジナルのMarkdownは<a href="http://daringfireball.net/">Daring Fireball</a>で公開されています。</p>"""

        self.assert_equal(source, expected)


    def test_hyperlink_auto(self):
        source = u"""<http://example.com>

<info@example.com>"""
        expected = r"""<p><a href="http://example.com">http://example.com</a></p>
<p><a href="[&#0-9;xA-E]+?">[&#0-9;xA-E]+?</a></p>"""

        self.assert_true(source, expected)


    def test_emphasis_1(self):
        source = u"""これは*強調されたテキスト*です。

これは**重要なテキスト**です。"""
        expected = u"""<p>これは<em>強調されたテキスト</em>です。</p>
<p>これは<strong>重要なテキスト</strong>です。</p>"""

        self.assert_equal(source, expected)


    def test_emphasis_2(self):
        source = u"""これは_強調されたテキスト_です。

これは__重要なテキスト__です。"""
        expected = u"""<p>これは<em>強調されたテキスト</em>です。</p>
<p>これは<strong>重要なテキスト</strong>です。</p>"""
        py_markdown = u"""<p>これは_強調されたテキスト_です。</p>
<p>これは__重要なテキスト__です。</p>"""

        #self.assert_equal(source, expected)
        self.assert_equal(source, py_markdown)


    def test_emphasis_3(self):
        source = u"""Please open the folder "secret_magic_box"."""
        expected = u"""<p>Please open the folder "secret_magic_box".</p>"""

        self.assert_equal(source, expected)


    def test_img_direct_1(self):
        source = u"""![代替テキスト](img.jpg)"""
        expected = u"""<p><img src="img.jpg" alt="代替テキスト" /></p>"""
        py_markdown = u"""<p><img alt="代替テキスト" src="img.jpg" /></p>"""

        self.assert_equal(source, py_markdown)


    def test_img_direct_2(self):
        source = u"""![](img.jpg)"""
        expected = u"""<p><img src="img.jpg" alt="" /></p>"""
        py_markdown = u"""<p><img alt="" src="img.jpg" /></p>"""

        self.assert_equal(source, py_markdown)


    def test_img_indirect(self):
        source = u"""![代替テキスト][id]

[id]: img.jpg"""
        expected = u"""<p><img src="img.jpg" alt="代替テキスト" /></p>
"""
        py_markdown = u"""<p><img alt="代替テキスト" src="img.jpg" /></p>"""

        self.assert_equal(source, py_markdown)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


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

        self.assert_equal(source, expected)


    def test_html_1(self):
        source = u"""これは段落の中で本の<cite>タイトル</cite>に直接HTMLでマークアップした例です。"""
        expected = u"""<p>これは段落の中で本の<cite>タイトル</cite>に直接HTMLでマークアップした例です。</p>"""

        self.assert_equal(source, expected)


    def test_html_2(self):
        source = u"""これは**通常の段落**です。

<div>
**ブロックの中の段落**はMarkdownが解釈されません。
</div>"""
        expected = u"""<p>これは<strong>通常の段落</strong>です。</p>
<div>
**ブロックの中の段落**はMarkdownが解釈されません。
</div>"""

        self.assert_equal(source, expected)


    def test_html_3(self):
        source = u"""これは**通常の段落**です。

<div markdown="1">
**ブロックの中の段落**でもMarkdownが解釈されます。
</div>"""
        expected = u"""<p>これは<strong>通常の段落</strong>です。</p>
<div>
<p><strong>ブロックの中の段落</strong>でもMarkdownが解釈されます。</p>
</div>"""

        self.assert_equal(source, expected)



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # その他のテスト
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    # HTMLブロック中にネストした複雑なマークダウンでdenden_extensionが悪さをしないかのテスト
    # コードは下記より
    # https://pythonhosted.org/Markdown/extensions/extra.html#nested-markdown-inside-html-blocks
    # ただしResult:は extra, nl2br, sain_lists 各extensionを使用する環境での出力に差し替えてある (<br />が何カ所かに追加される)
    def test_nested_markdown_inside_html_blocks(self):
        source = u"""<div markdown="1" name="Example">

The text of the `Example` element.

<div markdown="1" name="DefaultBlockMode">
This text gets wrapped in `p` tags.
</div>

The tail of the `DefaultBlockMode` subelement.

<p markdown="1" name="DefaultSpanMode">
This text *is not* wrapped in additional `p` tags.
</p>

The tail of the `DefaultSpanMode` subelement.

<div markdown="span" name="SpanModeOverride">
This `div` block is not wrapped in paragraph tags.
Note: Subelements are not required to have tail text.
</div>

<p markdown="block" name="BlockModeOverride">
This `p` block *is* foolishly wrapped in further paragraph tags.
</p>

The tail of the `BlockModeOverride` subelement.

<div name="RawHtml">
Raw HTML blocks may also be nested.
</div>

</div>

This text is after the markdown in HTML."""
        expected = u"""<div name="Example">
<p>The text of the <code>Example</code> element.</p>
<div name="DefaultBlockMode">
<p>This text gets wrapped in <code>p</code> tags.</p>
</div>
<p>The tail of the <code>DefaultBlockMode</code> subelement.</p>
<p name="DefaultSpanMode"><br />
This text <em>is not</em> wrapped in additional <code>p</code> tags.</p>
<p>The tail of the <code>DefaultSpanMode</code> subelement.</p>
<div name="SpanModeOverride"><br />
This <code>div</code> block is not wrapped in paragraph tags.<br />
Note: Subelements are not required to have tail text.</div>
<p name="BlockModeOverride">
<p>This <code>p</code> block <em>is</em> foolishly wrapped in further paragraph tags.</p>
</p>
<p>The tail of the <code>BlockModeOverride</code> subelement.</p>
<div name="RawHtml">
Raw HTML blocks may also be nested.
</div>

</div>
<p>This text is after the markdown in HTML.</p>"""

        self.assert_equal(source, expected)



    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=
    # テスト用テンプレート
    #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

    def test_(self):
        source = u""""""
        expected = u""""""

        self.assert_equal(source, expected)



if __name__ == '__main__':
    unittest.main()
    