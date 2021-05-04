import re
import sys
from keyword_token import keywords
from separator_token import separators
from number_token import numberLiteral
from string_token import stringLiteral
from type_token import types


class Token(object):

    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '[%s, %s, %s]' % (self.type, self.val, self.pos)


class LexerError(Exception):

    def __init__(self, pos):
        self.pos = pos


class Lexer(object):

    def __init__(self, rules, skip_whitespace=True):

        idx = 1
        regex_parts = []
        self.group_type = {}
        for regex, type in rules:
            groupname = 'GROUP%s' % idx
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            self.group_type[groupname] = type
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, str):
        self.str = str
        self.pos = 0

    def token(self):

        if self.pos >= len(self.str):
            return None
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.str, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None
            m = self.regex.match(self.str, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname]
                tok = Token(tok_type, m.group(groupname), self.pos)
                self.pos = m.end()
                return tok

            raise LexerError(self.pos)

    def tokens(self):
        while 1:
            tok = self.token()
            if tok is None:
                break
            yield tok


if __name__ == '__main__':
    rules = [
        keywords,
        numberLiteral,
        # stringLiteral,
        separators,
        types,
        ('[a-zA-Z_]\w*',    'IDENTIFIER'),
        ('\+',              'PLUS'),
        ('\-',              'MINUS'),
        ('\*',              'MULTIPLY'),
        ('\/',              'DIVIDE'),
        ('\(',              'LP'),
        ('\)',              'RP'),
        ('=',               'EQUALS'),
    ]

    lx = Lexer(rules, skip_whitespace=True)
    lx.input(
        'class Array private constructor() { val size: Int operator fun get(index: Int in in ): T  operator fun set(index: Int, value: T): Unit   operator fun iterator(): Iterator }')

    try:
        for tok in lx.tokens():
            print(tok)
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
