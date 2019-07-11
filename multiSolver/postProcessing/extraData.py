#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:39:40 2018

@author: rodrigo
"""

class extraData(object):
    
    def __init__(self):
        
        

        self.TErrorAbsolute = {'label': ['TErrorAbsolute'],
                               'title': ['Temperature absolute error'],
                               'unit': '($K$)',
                               'rank': 0}
        
        self.TErrorRelative = {'label': ['TErrorRelative'],
                               'title': ['Temperature relative error'],
                               'unit': '',
                               'rank': 0}

        self.pErrorAbsolute = {'label': ['pErrorAbsolute'],
                               'title': ['Pressure absolute error'],
                               'unit': '($Pa$)',
                               'rank': 0}

        self.pErrorRelative = {'label': ['pErrorRelative'],
                               'title': ['Pressure relative error'],
                               'unit': '',
                               'rank': 0}
        
        self.UErrorAbsolute = {'label': ['UErrorAbsolute'],
                               'title': ['Velocity absolute error'],
                               'unit': '($m \cdot s^{-1}$)',
                               'rank': 0}

        self.UErrorRelative = {'label': ['UErrorRelative'],
                               'title': ['Velocity relative error'],
                               'unit': '',
                               'rank': 0}

        self.fluxErrorAbsolute = {'label': ['fluxErrorAbsolute'],
                                  'title': ['Flux absolute error'],
                                  'unit': '($m^{-2} \cdot s^{-1}$)',
                                  'rank': 0}

        self.fluxErrorRelative = {'label': ['fluxErrorRelative'],
                                  'title': ['Flux relative error'],
                                  'unit': '',
                                  'rank': 0}
