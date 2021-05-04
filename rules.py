keywords = (
    ' constructor|abstract|annotation|by|catch|companion|crossinline|data|dynamic|enum|external|final|finally|get|import|infix|init|inline|inner|internal|lateinit|noinline|open|operator|out|override|private|protected|public|reified|sealed|tailrec|set|vararg|where|field|property|receiver|param|setparam|delegate|file|expect|actual|const|suspend|class|for|while ', 'KEYWORD'
)
relation_operator = (
    '>|<|>=|<=|==|!=|', 'RELATION_OPERATOR'
)

assignment_operator = (
    '+=|-=|*=|/=|%=', 'ASSIGNMENT_OPERATOR'
)

unary_operator = (
    '+|-|++|--|!', 'UNARY_OPERATOR'
)

logical_operator = (
    '&&|\|\||!', 'LOGICAL_OPERATOR'
)

separator = {
    ''
}

string_content = (
    """(\\"|[^"])+""", 'STRING_CONTENT'
)
