#!/usr/bin/env python3
'''cattreats.py

This simple script finds the location of a selected cat's name in one list and
its favorite treat at the corresponding location in another. Both items are
printed to the screen afterward.

Limitations:
This code will not work if the cat's name is not in list of cat names.

Usage: ./cattreats.py

David Whipp - 12.9.2016
'''

# Set the selected cat
SelectedCat = 7

# Create and fill lists of cats and treats
Cats = ['Garfield', 'Nermal', 'Tom Cat', 'Puss in Boots', 'Hobbes', 'Stimpy', 'Snowball II']
Treats = ['Lasagne', 'Praise', 'Mice', 'Power', 'Calvin', 'Fresh kitty litter']

# Find location of selected cat
CatIndex = Cats.index(SelectedCat)

# Print cat name and favorit treat on screen
print("The favorite treat of", SelectedCat, "is", Treats[SelectedCat])
