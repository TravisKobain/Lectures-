#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 23:11:03 2017

@author: KStar
"""

from util import deco

print('<1>')

@deco
def first():
    print('<2>')
    
@deco
def second():
    third()
    print('<3>')

@deco
def third():
    print('<4>')
    
if __name__ == '__main__':
    first()
    second()
    #third()
    print('<6>')