#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-03-24
Purpose: Play the game of war
"""

import argparse
import sys
from itertools import product
import random

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
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
    seed = args.seed

    if not seed == None:
        random.seed(seed)

    suits = list(['♥', '♠', '♣', '♦'])
    #numbers = list(['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A'])
    numbers = list(map(str, range(2, 11))) + list('JQKA')
    deck = list(product(suits, numbers))

    lookup = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

    deck.sort()
    random.shuffle(deck)
    
    p1_wins = 0
    p2_wins = 0

#    while True:
#        if len(deck) == 0:
#            break
    while deck:
        p1 = deck.pop()
        p2 = deck.pop()
        p1card = p1[0]+p1[1]
        p2card = p2[0]+p2[1]
        if lookup[p1[1]] > lookup[p2[1]]:
            p1_wins += 1
            print('{:>3} {:>3} P1'.format(p1card, p2card))
        elif lookup[p1[1]] < lookup[p2[1]]:
            p2_wins += 1
            print('{:>3} {:>3} P2'.format(p1card, p2card))
        else:
            print('{:>3} {:>3} WAR!'.format(p1card, p2card))

    if p1_wins > p2_wins:
        print('P1 {} P2 {}: Player 1 wins'.format(p1_wins, p2_wins))
    elif p1_wins < p2_wins:
        print('P1 {} P2 {}: Player 2 wins'.format(p1_wins, p2_wins))
    else:
        print('P1 {} P2 {}: DRAW'.format(p1_wins, p2_wins))
# --------------------------------------------------
if __name__ == '__main__':
    main()
