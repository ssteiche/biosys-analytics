#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-03-31
Purpose: Parse strange and horrible date formats
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
            description='This here code parses dates',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'date', metavar='DATE', help='A date to parse')

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
    date = args.date

    date_re1 = re.compile('(?P<year>\d{4})'
                         '[/-]?'
                         '(?P<month>\d{1,2})'
                         '[/-]?'
                         '(?P<day>\d{1,2})?'
                         '[\D]')
    
    date_re2 = re.compile('(?P<year>\d{4})'
                         '[/-]?'
                         '(?P<month>\d{1,2})'
                         '[/-]?'
                         '(?P<day>\d{1,2})?')

    date_re3 = re.compile('(?P<month>\d{1,2})'
                          '[/]'
                          '(?P<year>\d{1,2})'
                          '(?P<day>\d{4})?')
    
    date_re4 = re.compile('(?P<month>[a-zA-Z]{3,})'
                          '[-]?'
                          ',\s?'
                          '(?P<year>\d{4})'
                          '(?P<day>\d{4})?')
    
    date_re5 = re.compile('(?P<month>[a-zA-Z]{3,})'
                          '[-]'
                          '(?P<year>\d{4})'
                          '(?P<day>\d{4})?')

    match = date_re1.match(date) or date_re2.match(date) or date_re3.match(date) or date_re4.match(date) or date_re5.match(date)

    short = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    long = ('January February March April May June July August '
                    'September October November December').split()
    num_months = list(range(1,13))
    short_lookup = dict(zip(short, num_months))
    long_lookup = dict(zip(long, num_months))
    lookup = {**short_lookup, **long_lookup}

    if match == None:
        print('No match')
    else:
        if len(match.group('year')) == 4:
            year = match.group('year')
        else:
            year = '20'+match.group('year').zfill(2)
        if len(match.group('month')) < 3:
            month = match.group('month')
        else:
            month = str(lookup.get(match.group('month')))
        day = match.group('day') or '01'
        print('{}-{}-{}'.format(year, month.zfill(2), day.zfill(2)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
