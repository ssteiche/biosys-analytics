#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-19
Purpose: Check the outcome of a tictactoe game to determine a winning state
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'state', metavar='str', help='The state of the board', type=str)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    state = args.state

    if len(args.state) != 9:
        die('State "{}" must be 9 characters of only ., X, O'.format(state))

    for n in list(args.state):
        if n != 'X' and n != 'O' and n != '.':
            die('State "{}" must be 9 characters of only ., X, O'.format(state))
    
    wins = {'XXX......': 'X', 'OOO......': 'O', '...XXX...': 'X', 
            '...OOO...': 'O', '......XXX': 'X', '......OOO': 'O',
            'X..X..X..': 'X', 'O..O..O..': 'O', '.X..X..X.': 'X',
            '.O..O..O.': 'O', '..X..X..X': 'X', '..O..O..O': 'O',
            'X...X...X': 'X', 'O...O...O': 'O', '..X.X.X..': 'X',
            '..O.O.O..': 'O'}

    if wins.get(state) == 'X':
        print('X has won')
    elif wins.get(state) == 'O':
        print('O has won')
    else:
        print('No winner')

# --------------------------------------------------
if __name__ == '__main__':
    main()
