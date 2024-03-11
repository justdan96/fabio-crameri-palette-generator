import os
import json

palettes = ['acton',
            'bam',
            'bamO',
            'bamako',
            'batlow',
            'batlowK',
            'batlowW',
            'berlin',
            'bilbao',
            'broc',
            'brocO',
            'buda',
            'bukavu',
            'cork',
            'corkO',
            'davos',
            'devon',
            'fes',
            'glasgow',
            'grayC',
            'hawaii',
            'imola',
            'lajolla',
            'lapaz',
            'lipari',
            'lisbon',
            'managua',
            'navia',
            'naviaW',
            'nuuk',
            'oleron',
            'oslo',
            'roma',
            'romaO',
            'tofino',
            'tokyo',
            'turku',
            'vanimo',
            'vik',
            'vikO'
            ]

colormap = {}

for pal in palettes:
    pal_name = pal[0].upper() + pal[1:]
    lut_path = 'ScientificColourMaps8/' + pal + '/' + pal + '.lut'
    if os.path.isfile(lut_path):
        lut_file = open(lut_path, 'r')
        lut = lut_file.readlines()
        hex = []
        for line in lut:
            rgb = line.split(' ')
            hex.append('#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2])))
        if len(lut) >= 256:
            colormap[pal_name] = hex

js = json.dumps(colormap).replace('], ', '],\n')

print('var colormaps = ' + js + ';')