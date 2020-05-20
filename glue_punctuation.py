# -*- coding: utf-8 -*-
"""
This module glues together words and punctuation.
E.g. könyv , => könyv, or ( olasz ) => (olasz)
"""

import fileinput

def glue_punctuation():
    """Do the thing."""
    for line in fileinput.input():
        tokens = line.split(' ')
        for token in tokens:
            token_with_newline = token
            token = token.rstrip('\n')
            end_wsp = ' ' if token == token_with_newline else '\n'

            pre = False
            post = False
            # TODO nem trivi írásjelek: - ' "
            if token and token in '.,:;?!)}]*' or token == '...':
                pre = True
            if token and token in '({[':
                post = True
            print("{}{}{}".format(
                '' if pre else '|',
                token,
                '' if post else '|'), end='')
            print(end_wsp, end='')

def main():
    """Main."""
    glue_punctuation()

if __name__ == '__main__':
    main()
