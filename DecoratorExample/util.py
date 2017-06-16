#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:29:48 2017

@ramalhoorg

@author: KStar
"""

print('<A>')

def deco(f):
    print('<B>')
    def inner():
        print('<C>')
        f()
    return inner

print('<D>')