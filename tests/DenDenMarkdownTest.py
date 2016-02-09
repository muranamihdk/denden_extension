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


    """
    protected function self.assert_equal_with_files($fixtureName)

        $sourceFile = $fixtureName . '.md'
        $transformedFile = $fixtureName . '.html'
        assertTransformedFile($transformedFile, $sourceFile);


    protected function assertTransformedFile($transformedFile, $sourceFile)

        $expected = fixture($transformedFile);
        $actual = parser->transform(fixture($sourceFile));
        assertSame($expected, $actual);


    protected function fixture($fileName)

        $filePath = fixtureDir . DIRECTORY_SEPARATOR . $fileName;
        return file_get_contents($filePath);
    """

    def assert_equal_with_files(self, filename):
        mdfile = './tests/tests_DenDenMarkdown/{}.md'.format(filename)
        htmlfile = './tests/tests_DenDenMarkdown/{}.html'.format(filename)
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

    """
    def test_Abbr(self):

        self.assert_equal_with_files('abbr')

    """#<!-- ここからテスト対象
    def test_Paragraph(self):

        self.assert_equal_with_files('paragraph')

    """#--ここまでテスト対象>
    def test_BrInParagraph(self):

        self.assert_equal_with_files('br-in-paragraph')


    def test_Indent(self):

        self.assert_equal_with_files('indent')


    def test_HeadingsAtx(self):

        self.assert_equal_with_files('headings-atx')


    def test_HeadingsSetext(self):

        self.assert_equal_with_files('headings-setext')


    def test_BlockTitles(self):

        self.assert_equal_with_files('block-titles')


    def test_HeadingsSetextNumHyphens(self):

        assertTransformedFile('headings-setext.html', 'headings-setext-hyphens.md')


    def test_BlockQuote(self):

        self.assert_equal_with_files('blockquote')


    def test_BlockQuoteNest(self):

        self.assert_equal_with_files('blockquote-nest')


    def test_UlAsterisk(self):

        assertTransformedFile('ul.html', 'ul-asterisk.md')


    def test_UlPlus(self):

        assertTransformedFile('ul.html', 'ul-plus.md')


    def test_UlHyphen(self):

        assertTransformedFile('ul.html', 'ul-hyphen.md')


    def test_Ol(self):

        self.assert_equal_with_files('ol')


    def test_OlOutOfOrder(self):

        assertTransformedFile('ol.html', 'ol-out-of-order.md')


    def test_OlEscape(self):

        self.assert_equal_with_files('ol-escape')


    def test_PharagraphInList(self):

        self.assert_equal_with_files('paragraph-in-list')


    def test_MultiParagraphsInLi(self):

        self.assert_equal_with_files('multi-paragraphs-in-li')


    def test_BlockquoteInList(self):

        self.assert_equal_with_files('blockquote-in-list')


    def test_CodeInList(self):

        self.assert_equal_with_files('code-in-list')


    def test_CodeBlock(self):

        self.assert_equal_with_files('code-block')


    def test_CodeInline(self):

        self.assert_equal_with_files('code-inline')


    def test_Hr(self):

        self.assert_equal_with_files('hr')


    def test_DocBreak(self):

        self.assert_equal_with_files('docbreak')


    def test_PageNumber(self):

        self.assert_equal_with_files('page-number')


    def test_PageBreakInline(self):

        self.assert_equal_with_files('page-break-inline')


    def test_PageNumberText(self):

        self.assert_equal_with_files('page-number-text')


    def test_InlineLink(self):

        self.assert_equal_with_files('inline-link')


    def test_InlineLinkTitle(self):

        self.assert_equal_with_files('inline-link-title')


    def test_ReferenceLink(self):

        self.assert_equal_with_files('reference-link')


    def test_ReferenceLinkTitle(self):

        self.assert_equal_with_files('reference-link-title')


    def test_ReferenceLinkNoId(self):

        self.assert_equal_with_files('reference-link-no-id')


    #def test_Autolink(self):

    #    $expected = fixture('autolink.html')
    #    $source = fixture('autolink.md')
    #    $actual = parser->transform($source);
    #    assertSame(html_entity_decode($expected), html_entity_decode($actual));


    def test_AutolinkTwitter(self):

        self.assert_equal_with_files('autolink-twitter')


    def test_Emphasis(self):

        self.assert_equal_with_files('emphasis')


    def test_EmphasisUnderscore(self):

        assertTransformedFile('emphasis.html', 'emphasis-underscore.md')


    def test_UnderscoreInQuotation(self):

        self.assert_equal_with_files('underscore-in-quotation')


    def test_GroupRuby(self):

        self.assert_equal_with_files('group-ruby')


    def test_MonoRuby(self):

        self.assert_equal_with_files('mono-ruby')


    #def test_BraceFollowingVerticalLineNotTransformedToRuby(self):

    #    $source = 'これは段落です。foo{|bar| bar.buz} これは段落です。'
    #    $transformed = parser->transform($source);
    #    assertNotRegExp('/<ruby>/', $transformed);


    #def test_EscapeRuby(self):

    #    $source = 'これは段落です。\{Info\|Warning\} これは段落です。'
    #    $transformed = parser->transform($source);
    #    assertNotRegExp('/<ruby>/', $transformed);


    #def test_EscapeRubyVerticalLine(self):

    #    $source = 'これは段落です。{Info\|Warning} これは段落です。
#'
    #    $transformed = parser->transform($source);
    #    assertNotRegExp('/<ruby>/', $transformed);


    #def test_EscapeRubyBackQuotes(self):

    #    $source = 'これは段落です。`{Info|Warning}` これは段落です。'
    #    $transformed = parser->transform($source);
    #    assertNotRegExp('/<ruby>/', $transformed);


    def test_TateChuYoko(self):

        self.assert_equal_with_files('tate-chu-yoko')


    def test_Footnote(self):

        self.assert_equal_with_files('footnote')


    def test_MultiParagraphsInFootnote(self):

        self.assert_equal_with_files('multi-paragraphs-in-footnote')


    #def test_MultiParagraphsInFootnoteLineBreakAtFirst(self):

    #    assertTransformedFile('multi-paragraphs-in-footnote.html', 'multi-paragraphs-in-footnote-line-break-at-first.md')


    def test_FootnoteCannotReferenceAnotherPage(self):

        self.assert_equal_with_files('footnote-cannot-reference-another-page')


    def test_Image(self):

        self.assert_equal_with_files('image')


    def test_ImageTitle(self):

        self.assert_equal_with_files('image-title')


    def test_ImageNoAlt(self):

        self.assert_equal_with_files('image-no-alt')


    def test_ImageNoAltTitle(self):

        self.assert_equal_with_files('image-no-alt-title')


    def test_ImageReferenceLink(self):

        self.assert_equal_with_files('image-reference-link')


    def test_ImageReferenceLinkTitle(self):

        self.assert_equal_with_files('image-reference-link-title')


    def test_Dl(self):

        self.assert_equal_with_files('dl')


    def test_MultiDdInDl(self):

        self.assert_equal_with_files('multi-dd-in-dl')


    def test_ParagraphInDd(self):

        self.assert_equal_with_files('paragraph-in-dd')


    def test_BlockquoteListCodeInDd(self):

        self.assert_equal_with_files('blockquote-list-code-in-dd')


    def test_Table(self):

        self.assert_equal_with_files('table')


    def test_HtmlTag(self):

        self.assert_equal_with_files('html-tag')


    def test_NotTransformedInHtmlBlock(self):

        self.assert_equal_with_files('not-transformed-in-html-block')


    def test_NotTransformedInMath(self):

        self.assert_equal_with_files('not-transformed-in-math')


    def test_NotTransformedInScript(self):

        self.assert_equal_with_files('not-transformed-in-script')


    def test_NotTransformedInStyle(self):

        self.assert_equal_with_files('not-transformed-in-style')


    def test_NotTransformedInSvg(self):

        self.assert_equal_with_files('not-transformed-in-svg')


    def test_MarkdownInHtmlBlock(self):

        self.assert_equal_with_files('markdown-in-html-block')


    def test_BlockTagAddress(self):

        self.assert_equal_with_files('block-tag-address')


    def test_BlockTagArticle(self):

        self.assert_equal_with_files('block-tag-article')


    def test_BlockTagAside(self):

        self.assert_equal_with_files('block-tag-aside')


    def test_BlockTagBlockquote(self):

        self.assert_equal_with_files('block-tag-blockquote')


    def test_BlockTagBody(self):

        self.assert_equal_with_files('block-tag-body')


    def test_BlockTagCenter(self):

        self.assert_equal_with_files('block-tag-center')


    def test_BlockTagDd(self):

        self.assert_equal_with_files('block-tag-dd')


    def test_BlockTagDetails(self):

        self.assert_equal_with_files('block-tag-details')


    def test_BlockTagDialog(self):

        self.assert_equal_with_files('block-tag-dialog')


    def test_BlockTagDir(self):

        self.assert_equal_with_files('block-tag-dir')


    def test_BlockTagDiv(self):

        self.assert_equal_with_files('block-tag-div')


    def test_BlockTagDl(self):

        self.assert_equal_with_files('block-tag-dl')


    def test_BlockTagDt(self):

        self.assert_equal_with_files('block-tag-dt')


    def test_BlockTagFigcaption(self):

        self.assert_equal_with_files('block-tag-figcaption')


    def test_BlockTagFigure(self):

        self.assert_equal_with_files('block-tag-figure')


    def test_BlockTagFooter(self):

        self.assert_equal_with_files('block-tag-footer')


    def test_BlockTagHn(self):

        self.assert_equal_with_files('block-tag-hn')


    def test_BlockTagHeader(self):

        self.assert_equal_with_files('block-tag-header')


    def test_BlockTagHgroup(self):

        self.assert_equal_with_files('block-tag-hgroup')


    def test_BlockTagHr(self):

        self.assert_equal_with_files('block-tag-hr')


    def test_BlockTagHtml(self):

        self.assert_equal_with_files('block-tag-html')


    def test_BlockTagLegend(self):

        self.assert_equal_with_files('block-tag-legend')


    def test_BlockTagListing(self):

        self.assert_equal_with_files('block-tag-listing')


    def test_BlockLTagMenu(self):

        self.assert_equal_with_files('block-tag-menu')


    def test_BlockLTagNav(self):

        self.assert_equal_with_files('block-tag-nav')


    def test_BlockTagOl(self):

        self.assert_equal_with_files('block-tag-ol')


    def test_BlockTagP(self):

        self.assert_equal_with_files('block-tag-p')


    def test_BlockTagPlaintext(self):

        self.assert_equal_with_files('block-tag-plaintext')


    def test_BlockTagPre(self):

        self.assert_equal_with_files('block-tag-pre')


    def test_BlockTagSection(self):

        self.assert_equal_with_files('block-tag-section')


    def test_BlockTagSummary(self):

        self.assert_equal_with_files('block-tag-summary')


    def test_BlockTagStyle(self):

        self.assert_equal_with_files('block-tag-style')


    def test_BlockTagTable(self):

        self.assert_equal_with_files('block-tag-table')


    def test_BlockTagUl(self):

        self.assert_equal_with_files('block-tag-ul')


    def test_BlockTagXmp(self):

        self.assert_equal_with_files('block-tag-xmp')


    def test_PhrasingContentTagAbbr(self):

        self.assert_equal_with_files('phrasing_content_tag_abbr')


    def test_PhrasingContentTagaAea(self):

        self.assert_equal_with_files('phrasing_content_tag_area')


    def test_PhrasingContentTagAudio(self):

        self.assert_equal_with_files('phrasing_content_tag_audio')


    def test_PhrasingContentTagB(self):

        self.assert_equal_with_files('phrasing_content_tag_b')


    def test_PhrasingContentTagBdi(self):

        self.assert_equal_with_files('phrasing_content_tag_bdi')


    def test_PhrasingContentTagBdo(self):

        self.assert_equal_with_files('phrasing_content_tag_bdo')


    def test_PhrasingContentTagBr(self):

        self.assert_equal_with_files('phrasing_content_tag_br')


    def test_PhrasingContentTagButton(self):

        self.assert_equal_with_files('phrasing_content_tag_button')


    def test_PhrasingContentTagCanvas(self):

        self.assert_equal_with_files('phrasing_content_tag_canvas')


    def test_PhrasingContentTagCite(self):

        self.assert_equal_with_files('phrasing_content_tag_cite')


    def test_PhrasingContentTagCode(self):

        self.assert_equal_with_files('phrasing_content_tag_code')


    def test_PhrasingContentTagCommand(self):

        self.assert_equal_with_files('phrasing_content_tag_command')


    def test_PhrasingContentTagDatalist(self):

        self.assert_equal_with_files('phrasing_content_tag_datalist')


    def test_PhrasingContentTagDel(self):

        self.assert_equal_with_files('phrasing_content_tag_del')


    def test_PhrasingContentTagDfn(self):

        self.assert_equal_with_files('phrasing_content_tag_dfn')


    def test_PhrasingContentTagEm(self):

        self.assert_equal_with_files('phrasing_content_tag_em')


    def test_PhrasingContentTagEmbed(self):

        self.assert_equal_with_files('phrasing_content_tag_embed')


    def test_PhrasingContentTagI(self):

        self.assert_equal_with_files('phrasing_content_tag_i')


    def test_PhrasingContentTagIframe(self):

        self.assert_equal_with_files('phrasing_content_tag_iframe')


    def test_PhrasingContentTagImg(self):

        self.assert_equal_with_files('phrasing_content_tag_img')


    def test_PhrasingContentTagInput(self):

        self.assert_equal_with_files('phrasing_content_tag_input')


    def test_PhrasingContentTagIns(self):

        self.assert_equal_with_files('phrasing_content_tag_ins')


    def test_PhrasingContentTagKbd(self):

        self.assert_equal_with_files('phrasing_content_tag_kbd')


    def test_PhrasingContentTagKeygen(self):

        self.assert_equal_with_files('phrasing_content_tag_keygen')


    def test_PhrasingContentTagLabel(self):

        self.assert_equal_with_files('phrasing_content_tag_label')


    def test_PhrasingContentTagMap(self):

        self.assert_equal_with_files('phrasing_content_tag_map')


    def test_PhrasingContentTagMark(self):

        self.assert_equal_with_files('phrasing_content_tag_mark')


    def test_PhrasingContentTagMath(self):

        self.assert_equal_with_files('phrasing_content_tag_math')


    def test_PhrasingContentTagMeter(self):

        self.assert_equal_with_files('phrasing_content_tag_meter')


    def test_PhrasingContentTagNoscript(self):

        self.assert_equal_with_files('phrasing_content_tag_noscript')


    def test_PhrasingContentTagObject(self):

        self.assert_equal_with_files('phrasing_content_tag_object')


    def test_PhrasingContentTagOutput(self):

        self.assert_equal_with_files('phrasing_content_tag_output')


    def test_PhrasingContentTagProgress(self):

        self.assert_equal_with_files('phrasing_content_tag_progress')


    def test_PhrasingContentTagQ(self):

        self.assert_equal_with_files('phrasing_content_tag_q')


    def test_PhrasingContentTagRuby(self):

        self.assert_equal_with_files('phrasing_content_tag_ruby')


    def test_PhrasingContentTagS(self):

        self.assert_equal_with_files('phrasing_content_tag_s')


    def test_PhrasingContentTagSamp(self):

        self.assert_equal_with_files('phrasing_content_tag_samp')


    def test_PhrasingContentTagScript(self):

        self.assert_equal_with_files('phrasing_content_tag_script')


    def test_PhrasingContentTagSelect(self):

        self.assert_equal_with_files('phrasing_content_tag_select')


    def test_PhrasingContentTagSmall(self):

        self.assert_equal_with_files('phrasing_content_tag_small')


    def test_PhrasingContentTagSpan(self):

        self.assert_equal_with_files('phrasing_content_tag_span')


    def test_PhrasingContentTagStrong(self):

        self.assert_equal_with_files('phrasing_content_tag_strong')


    def test_PhrasingContentTagSub(self):

        self.assert_equal_with_files('phrasing_content_tag_sub')


    def test_PhrasingContentTagSup(self):

        self.assert_equal_with_files('phrasing_content_tag_sup')


    def test_PhrasingContentTagSvg(self):

        self.assert_equal_with_files('phrasing_content_tag_svg')


    def test_PhrasingContentTagTextarea(self):

        self.assert_equal_with_files('phrasing_content_tag_textarea')


    def test_PhrasingContentTagTime(self):

        self.assert_equal_with_files('phrasing_content_tag_time')


    def test_PhrasingContentTagU(self):

        self.assert_equal_with_files('phrasing_content_tag_u')


    def test_PhrasingContentTagVar(self):

        self.assert_equal_with_files('phrasing_content_tag_var')


    def test_PhrasingContentTagVideo(self):

        self.assert_equal_with_files('phrasing_content_tag_video')


    def test_PhrasingContentTagWbr(self):

        self.assert_equal_with_files('phrasing_content_tag_wbr')


    def test_FencedCodeBlock(self):

        self.assert_equal_with_files('fenced-code-block')


    def test_FencedCodeBlockGfm(self):

      self.assert_equal_with_files('fenced-code-block-gfm')


    def test_FencedCodeBlockGfmWithClass(self):

      self.assert_equal_with_files('fenced-code-block-gfm-with-class')


    def test_WithIdAttributeHn(self):

        self.assert_equal_with_files('with-id-attribute-hn')


    def test_WithIdAttributeA(self):

        self.assert_equal_with_files('with-id-attribute-a')


    def test_WithIdAttributeARefLink(self):

        self.assert_equal_with_files('with-id-attribute-a-ref-link')


    def test_WithIdAttributeImg(self):

        self.assert_equal_with_files('with-id-attribute-img')


    def test_WithIdAttributeImgRefLink(self):

        self.assert_equal_with_files('with-id-attribute-img-ref-link')


    def test_WithIdAttributeFencedCodeBlock(self):

        self.assert_equal_with_files('with-id-attribute-fenced-code-block')


    def test_WithClassAttributeHn(self):

        self.assert_equal_with_files('with-class-attribute-hn')


    def test_WithClassAttributeA(self):

        self.assert_equal_with_files('with-class-attribute-a')


    def test_WithClassAttributeARefLink(self):

        self.assert_equal_with_files('with-class-attribute-a-ref-link')


    def test_WithClassAttributeImg(self):

        self.assert_equal_with_files('with-class-attribute-img')


    def test_WithClassAttributeImgRefLink(self):

        self.assert_equal_with_files('with-class-attribute-img-ref-link')


    def test_WithClassAttributeFencedCodeBlock(self):

        self.assert_equal_with_files('with-class-attribute-fenced-code-block')


    def test_WithMultiAttributesHn(self):

        self.assert_equal_with_files('with-multi-attributes-hn')


    def test_WithMultiAttributesA(self):

        self.assert_equal_with_files('with-multi-attributes-a')


    def test_WithMultiAttributesARefLink(self):

        self.assert_equal_with_files('with-multi-attributes-a-ref-link')


    def test_WithMultiAttributesImg(self):

        self.assert_equal_with_files('with-multi-attributes-img')


    def test_WithMultiAttributesImgRefLink(self):

        self.assert_equal_with_files('with-multi-attributes-img-ref-link')


    def test_WithMultiAttributesFencedCodeBlock(self):

        self.assert_equal_with_files('with-multi-attributes-fenced-code-block')
    """


if __name__ == '__main__':
    unittest.main()
