# -*- coding: utf-8 -*-
"""
This module glues together words and punctuation.
E.g. könyv , => könyv, or ( olasz ) => (olasz)
"""

import fileinput

PRE = set('.,:;?!)}]*')
PRE.add('...')
POST = set('({[')

SPACE = ' '
NEWLINE = '\n'

def glue_punctuation():
    """Do the thing."""
    for line in fileinput.input():
        tokens = line.split(SPACE)

        for token in tokens:
            token_with_newline = token
            token = token.rstrip(NEWLINE)
            end_wsp = SPACE if token == token_with_newline else NEWLINE

            # TODO nem trivi írásjelek: - ' "
            pre = token and token in PRE
            post = token and token in POST

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
