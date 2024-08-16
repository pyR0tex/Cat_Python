# myCat.py
'''
Python clone of the command line program: * cat *
'''

import argparse
import sys


def main(args):
    if not args.files:
        if args.n:
            i = 1
            while True:
                try:
                    line = input()
                    print(f"        {i} {line}")
                    i+=1
                except EOFError:
                    break
        elif args.b:
            i = 1
            while True:
                try:
                    line = input()
                    if line:
                        print(f"        {i} {line}")
                        i+=1
                except EOFError:
                    break
        else:
            while True:
                try:
                    line = input()
                    print(line)
                except EOFError:
                    break
    else:
        for arg in args.files:
            if arg == '-':
                if args.n:
                    i = 1
                    while True:
                        try:
                            line = input()
                            print(f"        {i} {line}")
                            i+=1
                        except EOFError:
                            break
                    pass
                elif args.b:
                    i = 1
                    while True:
                        try:
                            line = input()
                            if line:
                                print(f"        {i} {line}")
                                i+=1
                            pass
                        except EOFError:
                            break
                    pass
                else:
                    while True:
                        try:
                            line = input()
                            print(line)
                        except EOFError:
                            break
                    pass
            else:
                try:
                    with open(arg) as file:
                        if args.n:
                            i = 1
                            for line in file:
                                print(f"        {i} {line}")
                                i+=1
                            pass
                        elif args.b:  
                            i = 1
                            for line in file:
                                if line != '\n':
                                    print(f"        {i} {line}")
                                    i   +=1
                            pass

                        else:
                            content = file.read()
                            if content:
                                print(f"{content}")
                            pass
                        
                except (Exception,FileNotFoundError, EOFError) as e:
                    print(f"    error: {e}")
                    sys.exit(1)
                
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
    
    return args


if __name__ == '__main__':
    args = argsSetup()
    main(args)