#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-03-26
Purpose: Play the game of blackjack
"""

import argparse
import sys
from itertools import product
import random

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"Blackjack" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)
    
    parser.add_argument(
            '-p', '--player_hits', help='A boolean flag', action='store_true')

    parser.add_argument(
            '-d', '--dealer_hits', help='A boolean flag', action='store_true')

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
    phit = args.player_hits
    dhit = args.dealer_hits

    if not seed == None:
        random.seed(seed)

    suits = list(['♥', '♠', '♣', '♦'])
    numbers = list(['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A'])
    deck = list(product(suits, numbers))

    lookup = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}

    deck.sort()
    random.shuffle(deck)

    pc1 = deck.pop()
    dc1 = deck.pop()
    pc2 = deck.pop()
    dc2 = deck.pop()
    
    if phit == True:
        pc3 = deck.pop()
        pval = lookup[pc1[1]]+lookup[pc2[1]]+lookup[pc3[1]]
        print('P [{:2}]: {}{} {}{} {}{}'.format(pval,pc1[0],pc1[1],pc2[0],pc2[1],pc3[0],pc3[1]))
    else:
        pval = lookup[pc1[1]]+lookup[pc2[1]]
        print('P [{:2}]: {}{} {}{}'.format(pval,pc1[0],pc1[1],pc2[0],pc2[1]))
    
    if dhit == True:
        dc3 = deck.pop()
        dval = lookup[dc1[1]]+lookup[dc2[1]]+lookup[dc3[1]]
        print('D [{:2}]: {}{} {}{} {}{}'.format(dval,dc1[0],dc1[1],dc2[0],dc2[1],dc3[0],dc3[1]))
    else:
        dval = lookup[dc1[1]]+lookup[dc2[1]]
        print('D [{:2}]: {}{} {}{}'.format(dval,dc1[0],dc1[1],dc2[0],dc2[1]))
     
    if dval > 21:
        print('Dealer busts')
        sys.exit(0)
    if pval > 21:
        print('Player busts! You lose, loser!')
        sys.exit(0)    
    if dval == 21:
        print('Dealer wins!')
        sys.exit(0)
    if pval == 21:
        print('Player wins. You probably cheated')
        sys.exit(0)    
    if dval < 18:
        print('Dealer should hit')
    if pval < 18:
        print('Player should hit')

# --------------------------------------------------
if __name__ == '__main__':
    main()
