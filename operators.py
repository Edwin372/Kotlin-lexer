operators = ['+', '-', '*', '/', '%', '**', '//',
            '=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<='
            '==', '!=', '>', '<', '>=', '<=',
            'and', 'or', 'not',
            'is', 'is not',
            'in', 'not in',
            '&', '|', '^', '~', '<<', '>>']

relation_operator = (
    '>|<|>=|<=|==|!=|', 'RELATION_OPERATOR'
)

assignment_operator = (
    '+=|-=|*=|/=|%=', 'ASSIGNMENT_OPERATOR'
)

logical_operator = (
    '&&|\|\||!', 'LOGICAL_OPERATOR'
)
