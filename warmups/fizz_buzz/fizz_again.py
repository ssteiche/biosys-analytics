#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-05-06
Purpose: Print Fizz where numbers are divisible by 3 and Buzz for 5 
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

#    if len(args) != 1:
#        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
#        sys.exit(1)

    last = args[0] if args else 100

    nums = range(1, int(last)+1)
    output = []
    for num in nums:
        if num % 3 == 0:
            output.append('Fizz')
        elif num % 5 == 0:
            output.append('Buzz')
        else:
            output.append(str(num))

    print(' '.join(output))

# --------------------------------------------------
main()
