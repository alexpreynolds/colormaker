#!/usr/bin/env python

import sys
import json
import colorsys
import math
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--seed", action="store", type="string", dest="seed", help="RGB seed or starting color as braced triplet, e.g. \"[222,0,0]`\"")
parser.add_option("-n", "--number", action="store", type="string", dest="number", help="Number of desired colors (including seed color)")
parser.add_option("-x", "--asHex", action="store_true", dest="asHex", default=False, help="Print colors as hex values")
parser.add_option("-r", "--asRGB", action="store_true", dest="asRGB", default=False, help="Print colors as RGB triplets")
parser.add_option("-a", "--asRGBA", action="store_true", dest="asRGBA", default=False, help="Print colors as RGBA quartets")
(options, args) = parser.parse_args()

if not (options.seed and options.number):
    args = ["-h"]
    (options, args) = parser.parse_args(args)
    sys.exit(-1)

GOLDEN_RATIO_CONJUGATE = 0.618033988749895

def generate_color(h, s, v):
    h = h + GOLDEN_RATIO_CONJUGATE
    h = h % 1
    c = hsv2rgb(h, s, v)
    return [ c['red'] , c['green'], c['blue'] ]

def hsv2rgb(h, s, v):
    c = { 'red' : None, 'green' : None, 'blue' : None }
    if s == 0:
        rv = int(round(v * 255))
        c = { 'red' : rv, 'green' : rv, 'blue': rv }
    else:
        vh = h * 6
        if vh == 6:
            vh = 0
        vi = math.floor(vh)
        v1 = v * (1 - s)
        v2 = v * (1 - s * (vh - vi))
        v3 = v * (1 - s * (1 - (vh - vi)))
        if vi == 0:
            c = { 'red': v, 'green': v3, 'blue': v1 }
        elif vi == 1:
            c = { 'red': v2, 'green': v, 'blue': v1 }
        elif vi == 2:
            c = { 'red': v1, 'green': v, 'blue': v3 }
        elif vi == 3:
            c = { 'red': v1, 'green': v2, 'blue': v }
        elif vi == 4:
            c = { 'red': v3, 'green': v1, 'blue': v }
        else:
            c = { 'red': v, 'green': v1, 'blue': v2 }

        c = { 'red': int(round(c['red'] * 255)), 'green': int(round(c['green'] * 255)), 'blue': int(round(c['blue'] * 255)) }
        
    return c

try:
    seed = json.loads(options.seed)
except ValueError, e:
    args = ["-h"]
    (options, args) = parser.parse_args(args)
    sys.exit(-1)

seed_hsv = colorsys.rgb_to_hsv(float(seed[0]) / 255, float(seed[1]) / 255, float(seed[2]) / 255)

if options.asHex:
    print '#%02x%02x%02x' % (seed[0], seed[1], seed[2])
    for i in xrange(int(options.number) - 1):
        new_seed = generate_color(seed_hsv[0], seed_hsv[1], seed_hsv[2])
        seed_hsv = colorsys.rgb_to_hsv(float(new_seed[0]) / 255, float(new_seed[1]) / 255, float(new_seed[2]) / 255)
        print '#%02x%02x%02x' % (new_seed[0], new_seed[1], new_seed[2])

elif options.asRGB:
    print ''.join(['rgb(', ','.join([str(x) for x in seed]), ')'])
    for i in xrange(int(options.number) - 1):
        new_seed = generate_color(seed_hsv[0], seed_hsv[1], seed_hsv[2])
        seed_hsv = colorsys.rgb_to_hsv(float(new_seed[0]) / 255, float(new_seed[1]) / 255, float(new_seed[2]) / 255)
        print ''.join(['rgb(', ','.join([str(x) for x in new_seed]), ')'])

elif options.asRGBA:
    print ''.join(['rgba(', ','.join([str(x) for x in seed]), ',1)'])
    for i in xrange(int(options.number) - 1):
        new_seed = generate_color(seed_hsv[0], seed_hsv[1], seed_hsv[2])
        seed_hsv = colorsys.rgb_to_hsv(float(new_seed[0]) / 255, float(new_seed[1]) / 255, float(new_seed[2]) / 255)
        print ''.join(['rgba(', ','.join([str(x) for x in new_seed]), ',1)'])
