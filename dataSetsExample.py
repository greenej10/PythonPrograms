# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:26:55 2018

@author: Gabby
"""

playstationgames = {'Fallout', 'Skyrim', 'Dragon Age', 'Horizon Zero Dawn'}
print('These are playstation games:')
print(playstationgames)
xboxgames = {'Halo', 'Skyrim', 'Fallout', 'Dragon Age'}
print('\nThese are xbox games:')
print(xboxgames)
print('\nThese are the games that they have in common:')
print(playstationgames & xboxgames)
print('\nThese are games only for playstation:')
print(playstationgames - xboxgames)

xboxgames.add('Ori')
print('\n')
print(xboxgames)

#The next sets are frozensets, they cannot be changed by the user
vowels = frozenset(['A','E','I','O','U','Y'])
print('\n')
print(vowels)