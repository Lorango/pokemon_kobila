# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:26:54 2018

@author: Lorango
"""

import sys

if not ('../bavul' in sys.path):
    sys.path.append("../bavul")

import bavul.tiles.tmx_read

pl_1 = bavul.tiles.tmx_read.Plocica('tilesets/pokemon_test_1.tsx')
ma_1 = bavul.tiles.tmx_read.Karta('maps/test_1.tmx')
