#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-28
Purpose: Identify common words between two files
"""

import argparse
import sys
import logging
import io
import re
from itertools import product
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Identify common words between two files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='Input files', nargs=2,
        type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')
   
    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')
    
    parser.add_argument(
        '-t', '--table', help='Table output', action='store_true')

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
def dist(s1, s2):
    """Calculate Hamming distance"""
    edits = abs(len(s1)-len(s2))
    for l1, l2 in list(zip(s1, s2)):
        if l1 != l2:
            edits += 1

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, edits))
    return edits

# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
             9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n

# --------------------------------------------------
def uniq_words(file, min_len):
    """Return the unique words in a file"""
    words = []
    for line in file:
        for word in line.split():
            clean = re.sub('[^a-zA-Z0-9]', '', word).lower()
            if clean == '':
                continue
            if len(clean) >= min_len:
                words.append(clean)

    return set(words)

# --------------------------------------------------
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])

# --------------------------------------------------
def common(words1, words2, distance):
    """Return the unique words in a file"""
    comps = product(words1, words2)
    outs = []
    for s1, s2 in comps:
        if dist(s1, s2) <= distance:
        #edits = abs(len(s1)-len(s2))
        #for l1, l2 in list(zip(s1, s2)):
        #    if l1 != l2:
        #        edits += 1
        #if edits <= distance:
            outs.append((s1, s2, dist(s1, s2)))

    return sorted(outs)

# --------------------------------------------------
def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.files
    min_len = args.min_len
    hamm = args.hamming_distance
    logfile = args.logfile
    debug = args.debug
    table = args.table

    logging.basicConfig(
        filename=logfile,
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    logging.debug('Hello, is there anybody out there?')

    if hamm < 0:
        die('--distance "{}" must be > 0'.format(hamm))

    words1 = uniq_words(files[0], min_len)
    words2 = uniq_words(files[1], min_len)
    common_words = common(words1, words2, hamm)

    if common_words:
        if table:
            print(tabulate(common_words,headers=["word1","word2","distance"],tablefmt="psql"))
        else:
            print('word1\tword2\tdistance')
            for w1, w2, num in common_words:
                print('{}\t{}\t{}'.format(w1,w2,num))
    else:
        print('No words in common.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
