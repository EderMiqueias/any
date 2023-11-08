import ply.lex as lex

from tokens import tokens
from rules import *


def reader(data: str) -> dict:
    lexer = lex.lex()
    lexer.input(data)
    lexed_tokens = {}
    for tok in lexer:
        if tok.lineno not in lexed_tokens:
            lexed_tokens[tok.lineno] = {}
        lexed_tokens[tok.lineno][tok.lexpos] = tok.value
    return lexed_tokens


print(reader(
    '''
    3 + 4 * 10
    + -20 *2
    '''
))
