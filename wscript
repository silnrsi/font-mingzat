#!/usr/bin/python3
# this is a smith configuration file

# set the default output folders
out = "results"  # default is currently buildlinux2
DOCDIR = ["documentation", "web"]  # add "web" to default
# OUTDIR = "installers"  # until these are defaults in smith itself we need to keep them
ZIPDIR = "releases"
TESTDIR = "tests"
# TESTRESULTSDIR = "tests"
# STANDARDS = "reference"
generated = "generated/"

# set package name
APPNAME = "Mingzat"

# set the font family name
FAMILY = APPNAME

DESC_NAME = "Mingzat"
DESC_SHORT = "Unicode font for the Lepcha script"

DEBPKG = 'fonts-sil-mingzat'

getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = "alpha"

ftmlTest('tests/ftml-smith.xsl', fonts = ['reference/Mingzat-Regular.ttf'], addfontindex = 1, fontmode = 'collect')

fontfamily=APPNAME
designspace('source/' + FAMILY + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            ap = 'source/${DS:FILENAME_BASE}_ap.xml',
            version = VERSION,  # Needed to ensure dev information on version string
            graphite=gdl('./source/Mingzat_glyphs.gdl',
                    master = 'source/graphite/main.gdl', 
                    params='-D -w3541 -w2504 -w4510',
                    depends=['source/graphite/main.gdl', 'source/graphite/stddef.gdh']
                ),
            opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/master.feax',     # 'source/opentype/${DS:FILENAME_BASE}.fea',
                    mapfile = 'source/${DS:FILENAME_BASE}.map'
                ),
            script='lepc',
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/' + FAMILY + '-WOFF-metadata.xml'),
)
