# Project status [![Build Status](https://build.palaso.org/app/rest/builds/buildType:Fonts_Mingzat/statusIcon)](https://build.palaso.org/viewType.html?buildTypeId=Fonts_Mingzat&guest=1)  


Mingzat is based on Jason Glavy's JG Lepcha font which was a custom-encoded font. We have used his design with his generous permission. He also agreed to allow the font to be released under the SIL Open Font License (OFL). 

To download the fonts visit the [Mingzat page](https://software.sil.org/mingzat/) or the [Github releases page](https://github.com/silnrsi/font-mingzat/releases).

For a complete list of changes in this version see the [FONTLOG.txt](FONTLOG.txt).

For copyright and licensing information - including any Reserved Font Names - see [OFL.txt](OFL.txt).

For practical information about using, modifying and redistributing this font see [OFL-FAQ.txt](OFL-FAQ.txt).

# Developer notes

Font sources are in the [UFO3](https://unifiedfontobject.org/versions/ufo3/) format with font family structures defined using [designspace](https://github.com/fonttools/fonttools/tree/master/Doc/source/designspaceLib). OpenType source code is stored in the [.fea](https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html) format in the UFO (features.fea) but is maintained in a separate file using the more efficient and powerful [.feax](https://github.com/silnrsi/feax/blob/main/docs/feaextensions.md) format.

The fonts are built using a completely free and open source workflow using industry-standard tools ([fonttools](https://github.com/fonttools/fonttools)), a package of custom python scripts ([pysilfont](https://github.com/silnrsi/pysilfont)), and a build and packaging system ([Smith](https://github.com/silnrsi/smith)). The whole toolchain is available as a Docker container. 

Full instructions for setting up the tools and building SIL fonts are available on a dedicated web site: [Building and Modifying SIL Fonts](https://writingsystems.info/topics/fonts/building-and-modifying-sil-fonts/).

## Contributing to the project

We warmly welcome contributions to the fonts, such as new glyphs, enhanced smart font code, or bug fixes. The [brief overview of contributing changes](https://writingsystems.info/topics/fonts/building-and-modifying-sil-fonts/#contributing-changes) is a good place to begin. The next step is to contact us by responding to an existing issue or creating an issue in the Github repository and expressing your interest. We can then work together to plan and integrate your contributions.

To enable us to accept contributions in a way that honors your contribution and respects your copyright while preserving long-term flexibility for open source licensing, you would also need to agree to the **SIL Global Contributor License Agreement for Font Software (v1.0)** prior to sending us your contribution. To read more about this requirement and find out how to submit the required form, please visit the [CLA information page](https://software.sil.org/fontcla).


