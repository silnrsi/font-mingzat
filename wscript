#!/usr/bin/python
# Smith configuration file for Mingzat

# override the default folders
DOCDIR = ["documentation", "web"]  # add "web" to default
genout = "generated/"

# set package name
APPNAME = "Mingzat"

# set the font family name
FAMILY = APPNAME

getufoinfo('source/' + FAMILY + '-Regular' + '.ufo')
# BUILDLABEL = "alpha"

ftmlTest('tools/ftml-smith.xsl')

# ftmlTest('tools/ftml-smith.xsl', fonts = ['reference/Mingzat-Regular.ttf'], addfontindex = 1, fontmode = 'collect')

# fontfamily=APPNAME
designspace('source/' + FAMILY + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
            ap = 'source/${DS:FILENAME_BASE}_ap.xml',
            version = VERSION,  # Needed to ensure dev information on version string
#            graphite = gdl('./source/Mingzat_glyphs.gdl',
#                    master = 'source/graphite/main.gdl', 
#                    params = '-D -w3541 -w2504 -w4510',
#                    depends = ['source/graphite/main.gdl', 'source/graphite/stddef.gdh']
#                ),
            opentype = fea('source/${DS:FILENAME_BASE}.fea',
                    master = 'source/opentype/main.feax',     # 'source/opentype/${DS:FILENAME_BASE}.fea',
                    mapfile = 'source/${DS:FILENAME_BASE}.map'
                ),
            script = 'lepc',
            pdf = fret(params="-r -oi"),
            woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/' + FAMILY + '-WOFF-metadata.xml'),
)
