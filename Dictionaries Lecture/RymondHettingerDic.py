#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:33:33 2017
Raymond Hettinger Modern Python Dictionaries A confluence of a dozen great ideas PyCon 2017

Dictionaries 
@author: KStar
"""

import sys

class UserProperty:
    
    
    def __init__(self, v0, v1, v2, v3, v4):
        self.guido = v0
        self.sarah = v1
        self.barry = v2
        self.rachel = v3
        self.tim = v4
        
    def __repr__(self):
        return 'UserProperty(%r, %r, %r, %r, %r)' \
                % (self.guido, self.sarah, self.barry, self.rachel, self.tim)
                
    colors = UserProperty('blue', 'orange', 'green', 'yellow', 'red')
    cities = UserProperty('austin', 'dallas', 'tuscon', 'reno', 'portland')
    fruits = UserProperty('apple', 'banana', 'orange', 'pear', 'peach')
    
    for user in [colors, cities, fruits]:
        print(vars(user))
        
    print(list(map(sys.getsizeof, map(vars, [colors, cities, fruits]))))

#==============================================================================
# 
#==============================================================================

    from __future__ import division, print_function
    from pprint import pprint
    
    keys = 'guido sarah barry rachel tim'.split()
    values1 = 'blue orange green yellow red'.split()
    values2 = 'austin dallas tuscon reno portland'.split()
    values3 = 'apple banana orange pear peach'.split()
    hashes = list(map(abs, map(hash, keys)))
    entries = list(zip(hashes , keys ,values1))
    comb_entries = list(zip(hashes, keys, values1, values2, values3))

#==============================================================================
# 
#==============================================================================

    def database_linear_search():
        pprint(list(zip(keys, values1, values2, values3)))
    
#==============================================================================
# How LISP Would do it 
#==============================================================================

    def association_lists():
        pprint([
                list(zip(keys, values1)),
                list(zip(keys, values2)),
                list(zip(keys, values3)),
        ])
    
#==============================================================================
# Seperate Chaining 
#==============================================================================

    def seperate_chaining(n):
        buckets = [[] for i in range(n)]
        for pair in entries:
            key, value = pair
            i = hash(key) % n
            buckets[i].append(pair)
        pprint(buckets)
    
    # Hash table ? Something that reduces the search space, by cutting it into smaller clusters 

#==============================================================================
# Dynamic Resizing 
#==============================================================================

    def resize(self, n):
        items = self.items() # save list of key/value pairs
        self.buckets = [[] for i in range(n)] #make a new, bigger table 
        for key, value in items:   #re-insert the saved pairs 
            self[key] =  value
#==============================================================================
# adding the hash value 
#==============================================================================

    def faster_resize(self, n):
        new_buckets = [[]for i in range(n)]
        for hashvalue, key, value in self.buckets:
            bucket = new_buckets[hashvalue % n]
            bucket.append((hashvalue, key, value))

#==============================================================================
# Fast Matching 
#==============================================================================

    def fast_match(key, target_key):
        
        if key is target_key: return True
        if key.hash != target_key.hash: return False 
        return key == target_key

#==============================================================================
# Open Addressing 
#==============================================================================

    def open_addressing_linear(n):
        table = [None] * n
        for h, key, value in entries:
            i = h % n
            while table[i] is not None:
                i = (i + 1) % n
            table[i] = (key, value)
        pprint(table)
        
#==============================================================================
# Deleted Entries  - Knuth - AlgorithmD 1960's 
#==============================================================================

    def lookup(h, key):
        freeslot = None
        for h, key, value in entries:
            i = h % n
            while True:
                entry = table[i]
                if entry == FREE:
                    return entry if freeslot is None else freeslot
                elif entry == DUMMY: 
                    if freeslot is None:
                        freeslot = i 
                elif fast_match(key, entry.key):
                    return entry
                i = (i + 1) % n
            
            
#==============================================================================
# Multiple Hashing                     
#==============================================================================

    def open_addressing_multihash(n):
        table = [None] * n 
        for h, key, value in entries:
            perturb = h 
            i = h % n
            while table[i] is not None:
                print('%r collided with %r'% (key, table[i][0]))
                i = (5 * i + perturb + 1 ) % n
                perturb >>= 5
            table[i] = (h, key, value)
        pprint(table)
            
#==============================================================================
# Compact Dict             
#==============================================================================

    def compact_and_ordered(n):
        table = [None] * n
        for pos, entry in enumerate(entries):
            h = perturb = entry [0]
            i = h % n
            while table[i] is not None: 
                i = (5 * i + perturb + 1) % n
                perturb >>= 5
            table[i] = pos 
        pprint(entries)
        pprint(table)
    
    def make_index(n):
        'New seq of indices using the smallest possible datatype'
        if n <= 2**7
        return array.array('b', [FEEE]) * n
        if n <= 2**15 return array.array('h', [FEEE]) * n
        if n <= 2**31 return array.array('1', [FEEE]) * n
        return [FREE] * n
    
    def shared_and_compact(n):
        'Compact, ordered and Shared'
        table = [None] * n 
        for pos, entry in enumerate(comb_entries):
            h = perturb = entry[0]
            i = h % n 
            while table[i] is not None: 
                i = (5 * i + perturb + 1) % n
                perturb >>= 5 
            table[i] = pos
        pprint(comb_entries)
        pprint(table)

