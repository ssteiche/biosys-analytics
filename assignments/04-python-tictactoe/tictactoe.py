#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-11
Purpose: Play tic tac toe with a friend
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
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        default=None)

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int,
        default=None) 

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
    state = list(args.state)
    player = args.player
    cell = args.cell

    if len(state) != 9:
        print('Invalid state "{}", must be 9 characters of only -, X, O'.format(args.state))
        sys.exit(1)

    for n in args.state:
        if n != 'X' and n != 'O' and n != '.':
            print('Invalid state "{}", must be 9 characters of only -, X, O'.format(args.state))
            sys.exit(1)

    if player != 'X' and player != 'O' and player != None:
        print('Invalid player "{}", must be X or O'.format(player))
        sys.exit(1)
    
    while cell != None:
        if cell < 1 or cell > 9:
            print('Invalid cell "{}", must be 1-9'.format(cell))
            sys.exit(1)
        else:
            break

    if any([player, cell]) and not all([player, cell]):
        print('Must provide both --player and --cell')
        sys.exit(1) 

    if cell != None and player != None:
        if state[cell - 1] != '.':
            print('Cell {} already taken'.format(cell))
            sys.exit(1)
        else:
            state[cell - 1] = player

    for i, c in enumerate(state):
        cell_val = i + 1 if c == '.' else c
        
        if i == 0:
            print('-------------')
 
        print('| {} '.format(cell_val), end = '')
        if (i + 1) % 3 == 0:
            print('|','\n-------------')

# --------------------------------------------------
if __name__ == '__main__':
    main()
