#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-01-31
Purpose: Count vowels, check that subject and verd number agrees, and proper use of plurals 
"""

import os
import sys


# --------------------------------------------------
def main():
    string = sys.argv[1:]

    if len(string) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    count = 0
    for letter in vowels:
        count += str(string).count(letter)
    
    if count == 1:    
       print('There is {} vowel in \"{}.\"'.format(count, string[0]))
    elif count > 1:    
       print('There are {} vowels in \"{}.\"'.format(count, string[0]))
    elif count == 0:    
       print('There are {} vowels in \"{}.\"'.format(count, string[0]))
# --------------------------------------------------
main()
