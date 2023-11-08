from tokens import reserved


def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_id(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reserved.get(t.value,'ID')
    return t


def t_comment(t):
    r"""\#.*"""
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
