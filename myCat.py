# myCat.py
'''
Python clone of the command line program: * cat *
'''

import argparse
import sys


def main(args):

    pass

def argsSetup():
    '''
    setup arguments and flag names using argparse
    '''
    parser = argparse.ArgumentParser(
        prog="myCat",
        description="Python clone of the command line program: * cat *"
    )
    parser.add_argument(
        'files',
        nargs='*',
        help="  --  file(s) to concatenate"
    )
    parser.add_argument(
        '-n',
        action='store_true',
        help="  --  Number the output lines, starting at 1"
    )
    parser.add_argument(
        '-b',
        action='store_true',
        help="  --  Number the non-blank output lines, starting at 1"
    )
    parser.add_argument(
        '-t',
        '--test',
        action='store_true',
        help="  --  run TEST SUITE"
    )
    args = parser.parse_args()
    
    # check for standard input error
    if args.files.count('-') > 1:
        parser.error("  --  too many '-' symbols used")
    
    # check for file provided if flag provided
    if (args.n or args.b) and not args.files:
        parser.error("  --  must provide file(s) with flag ' -n or '-b'")
    
    return args


if __name__ == '__main__':
    args = argsSetup()
    main(args)