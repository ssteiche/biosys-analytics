#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-02
Purpose: Determine tictactoe winner 
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0]

    if not re.match('[XO.]{9}', state):
        print('State "{}" must be 9 characters of only ., X, O'.format(state))
        sys.exit(1)

    if re.match('X{3}[XO.]{6}|' #XXX......
                '[XO.]{3}X{3}[XO.]{3}|' #...XXX...
                '[XO.]{6}X{3}|' #......XXX
                'X{1}[XO.]{2}X{1}[XO.]{2}X{1}[XO.]{2}|' #X..X..X..
                '[XO.]{1}X{1}[XO.]{2}X{1}[XO.]{2}X{1}[XO.]{1}|' #.X..X..X.
                '[XO.]{2}X{1}[XO.]{2}X{1}[XO.]{2}X{1}|' #..X..X..X
                'X{1}[XO.]{3}X{1}[XO.]{3}X{1}|' #X...X...X
                '[XO.]{2}X{1}[XO.]{1}X{1}[XO.]{1}X{1}[XO.]{2}' #..X.X.X..
                , state):
        print('X has won')
    elif re.match('O{3}[XO.]{6}|' #XXX......
                  '[XO.]{3}O{3}[XO.]{3}|' #...XXX...
                  '[XO.]{6}O{3}|' #......XXX
                  'O{1}[XO.]{2}O{1}[XO.]{2}O{1}[XO.]{2}|' #X..X..X..
                  '[XO.]{1}O{1}[XO.]{2}O{1}[XO.]{2}O{1}[XO.]{1}|' #.X..X..X.
                  '[XO.]{2}O{1}[XO.]{2}O{1}[XO.]{2}O{1}|' #..X..X..X
                  'O{1}[XO.]{3}O{1}[XO.]{3}O{1}|' #X...X...X
                  '[XO.]{2}O{1}[XO.]{1}O{1}[XO.]{1}O{1}[XO.]{2}' #..X.X.X..
                  , state):
        print('O has won')
    else:
        print('No winner')

    #wins = {'XXX......': 'X', 'OOO......': 'O', '...XXX...': 'X',
   #         '...OOO...': 'O', '......XXX': 'X', '......OOO': 'O',
   #         'X..X..X..': 'X', 'O..O..O..': 'O', '.X..X..X.': 'X',
   #         '.O..O..O.': 'O', '..X..X..X': 'X', '..O..O..O': 'O',
   #         'X...X...X': 'X', 'O...O...O': 'O', '..X.X.X..': 'X',
   #         '..O.O.O..': 'O'}

   # if wins.get(state) == 'X':
   #     print('X has won')
   # elif wins.get(state) == 'O':
   #     print('O has won')
   # else:
   #     print('No winner')
   # #print('State is "{}"'.format(state))


# --------------------------------------------------
main()
