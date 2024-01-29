<a href="https://software.sil.org/wp/wp-content/uploads/2019/03/MingzatTitle.png"><img src="https://software.sil.org/wp/wp-content/uploads/2019/03/MingzatTitle.png" alt="" width="276" height="161" class="alignnone size-full wp-image-3171" /></a>

<h2 id="about">About</h2>
Lepcha script is used by the [Lepcha language](https://www.ethnologue.com/language/lep){.external} of South Asia. This script has been in Unicode since Unicode 5.1.

**Mingzat** is a Unicode font based on Jason Glavy's **JG Lepcha** custom-encoded font. With his generous permission we have used his design and released the font under the [SIL Open Font License (OFL)](https://openfontlicense.org/){.external}. 

The name "Mingzat" means *"treasure of letters"* in the Lepcha language.

### Supported character ranges
Unicode block | Mingzat support
------------- | ---------------
Lepcha (complete)	| U+1C00..U+1C4F
Codepage 1252 (Western)¹ | ✓

A selection of characters from various other Unicode blocks is included in Mingzat. A utility such as [SIL ViewGlyph](http://scripts.sil.org/ViewGlyph_home){.external} can be used to examine the exact repertoire of this font.

¹Inclusion of basic Latin repertoire is provided as a convenience, e.g., for use in menus or for displaying markup in text files. These fonts are not intended for extensive Latin script use.

This [Type Sample](https://software.sil.org/downloads/r/mingzat/Mingzat-typesample.pdf) document demonstrates the characters and a sample text.

### Rendering Issues
Lepcha is a complex Indic script which requires reordering. The font has been tested to work on Microsoft Word, Microsoft Edge, Notepad, LibreOffice, Firefox, and Adobe InDesign. There may be some settings which must be modified in order for the font to work. For example, in Microsoft Word, go to the **Font / Advanced** menu and select **Ligatures / All**. In Adobe InDesign, select **Paragraph / Adobe World-Ready Paragraph Composer**.

Mingzat follows the Unicode syllable order: C(.)(R)(Y)(V)(F)(^). This translates into Consonant (C) followed by optional nukta (.), followed by optional Ra (R), followed by optional Ya (Y), followed by optional dependent Vowel (V), followed by optional Final consonant sign (F), followed by optional Ran (^). If this structure is followed, and your application supports proper rendering, the font will display them in the correct order. Sample nonsense syllable:

<a href="https://software.sil.org/wp/wp-content/uploads/2019/03/syll.jpg"><img src="https://software.sil.org/wp/wp-content/uploads/2019/03/syll-1024x116.jpg" alt="Lepcha nonsense syllable" class="alignleft size-large wp-image-3109" /></a>

Mingzat is designed to work with [Graphite](https://scripts.sil.org/cms/scripts/page.php?site_id=projects&amp;item_id=graphite_home){.external} or OpenType advanced font technologies. To take advantage of the advanced typographic capabilities of this font, you must be using applications that provide an adequate level of support for Graphite or OpenType.

The font has been tested in Microsoft Word, Notepad, LibreOffice, and Adobe InDesign. It also works in Microsoft Edge and Firefox. 

### Data Conversion
A compiled and uncompiled TECkit [conversion table](https://github.com/silnrsi/wsresources/tree/master/scripts/Lepc/legacy/jg-lepcha/mappings){.external} can be downloaded which maps data using the **JG Lepcha font to Unicode**. This map can be used with [TECkit](https://software.sil.org/teckit/){.external} and/or [SILConverters](https://software.sil.org/silconverters/){.external}. It has been minimally tested.

### Keyboarding
Mingzat can be used with any Unicode Lepcha keyboarding program. The [Lepcha (SIL) Unicode keyboard](https://keyman.com/keyboards/sil_lepcha){.external} for MacOS and Windows is based on a phonetic representation of the script. 

<h2 id="downloads">Downloads</h2>

### License
This font is licensed under the [SIL Open Font License (OFL)](https://openfontlicense.org/){.external}.
<a href="https://openfontlicense.org/" class="external"><img src="https://software.sil.org/wp/wp-content/uploads/2019/03/OFL_logo_rect_color.png" alt="" class="alignleft size-full wp-image-3194" /></a>

### Font
[sil_download style="table" sort="name" where="info.type == 'font'"]

### Release Notes for Version 1.100 

- Update fs bit to 7
- Update advanced width of U+00A0 NO-BREAK SPACE to match U+0020 SPACE
- Update advanced width of U+2008 PUNCTUATION SPACE to match U+002E FULL STOP
- Added visible square box to .notdef

#### Known issues

No known issues.

<h3>Previous versions</h3>
[sil_download style="table" sort="name" where="info.type == 'prev font'"]

### Release Notes for Version 1.000 

- Move font to new build system
- Update OpenType because modern computers now support the Lepcha script
- Update Graphite to fix issue with reordering
- Add Latin characters to support [Recommended characters for Non-Roman fonts](https://github.com/silnrsi/pysilfont/blob/master/lib/silfont/data/){.external}

[top]
<h2 id="contact">Source Code</h2>

Mingzat is licensed according to the terms of the SIL Open Font License. The latest source files are available in a [Github project](https://github.com/silnrsi/font-mingzat/){.external}.

[top]
<h2 id="support">Support</h2>
As these fonts and utilities are distributed at no cost, we are unable to provide a commercial level of personal technical support. We will, however, try to resolve problems that are reported to us.

We do hope that you will report problems so they can be addressed in future releases. Even if you are not having any specific problems, but have an idea on how this system could be improved, we want to hear your ideas and suggestions.

Please note that these fonts are intended for use by experienced computer users. Installing and using these fonts is not a trivial matter. The most effective technical support is usually provided by an experienced computer user who can personally sit down with you at your computer to troubleshoot the problem.

[top]
<h2 id="contact">Contact</h2>
General troubleshooting information, including frequently asked questions, can be found in the documentation. Additional information is also available on the general [Font Help Guides](https://software.sil.org/fonts/guides){.external} page. If that fails to answer your question, send an email via this contact form.

Before requesting technical support, please:

* Carefully read all the documentation provided with the font and on this site.
* Please see our [Font Help Guides](https://software.sil.org/fonts/guides).

### Language Software Community
<a href="https://community.software.sil.org/c/silfonts" class="external"><img class="lsc" src="/wp/wp-content/uploads/2017/02/LSC_icon_80x80.png" title="Go to Language Software Community for SIL Fonts &raquo;" /></a>

<p class="lsc">Support from other software users may be available through the <a href="//community.software.sil.org/c/silfonts" class="external">SIL Language Software Community</a>. This community will be growing to become the major source of software support.</p>

If that fails to answer your question, or you have a bug report, feature suggestion, or need help using the software, please contact us using the form below.

---

[contact-form-7 id="408" title="WSTech Products Contact Form"]

[top]
