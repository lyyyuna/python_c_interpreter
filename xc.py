'''
This module is main part of c interpreter
'''
import sys


def scan(src: str):
    '''
    Parse the source code, and generate the token
    '''
    token = src[0]
    return token


def expression():
    '''
    evaluate a expression
    '''
    return


def parser(src: str):
    '''
    use token to parser
    '''
    token = scan(src)


def evaluator():
    '''
    VM
    '''
    pass


def main():
    '''
    main function
    '''
    filename = sys.argv[1]
    with open(filename) as f:
        read_data = f.read()
        parser(read_data)


if __name__ == '__main__':
    main()
