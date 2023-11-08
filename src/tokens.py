reserved = {
   'if': 'IF',
   'then': 'THEN',
   'else': 'ELSE',
   'while': 'WHILE',
}


tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   *reserved.values()
)
