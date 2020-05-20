# -*- coding: utf-8 -*-
"""Create trivial `spl` format by spitting at . ? !"""

import fileinput

SPACE=' '
NEWLINE='\n'

def glue_punctuation():
    """Do the thing."""
    for line in fileinput.input():
        tokens = line.split(SPACE)
        for token in tokens:
            token_with_newline = token
            token = token.rstrip(NEWLINE)
            end_wsp = SPACE if token == token_with_newline else NEWLINE

            print("{}".format(token), end='')

            if token and token[-1] in '.?!':
                print(NEWLINE, end='')
            else:
                print(end_wsp, end='')

def main():
    """Main."""
    glue_punctuation()

if __name__ == '__main__':
    main()
