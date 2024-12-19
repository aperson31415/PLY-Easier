#PLYE Constructor

#Starting things
output_file = open(r'Name\LANGUAGE.py', 'w')
def write(text):
    output_file.write(text)
write('''###################################
#Programming Language Made In PLYE#
###################################''')

#Tokens.txt
tokens = []
token_functions = []
rawtokens = open('Tokens.txt', 'r').readlines()
for i in rawtokens:
    tokens.append(i[:i.index(':')])
    token_functions.append([])
    token_functions[-1].append(i[i.index('[')+1:i.index(',')])
    token_functions[-1].append(i[i.index(',')+1:-1])

write('tokens = (')
for i in range(len(tokens)):
    if i < (len(tokens)-1):
        write(tokens[i]+', ')
    else:
        write(tokens[i])
write(')\n')
for i, (f, t) in enumerate(zip(token_functions, tokens)):
    if f[0] == 'function':
        write('def t_'+t+'(t):\n'+f[1]+'\nreturn t\n')
    elif i[0] == 'regEx':
        write('t_'+t+' = r\''+f[1]+'\'\n')
    elif i[0] == 'plaintext':
        write('t_'+t+' = \''+f[1]+'\'\n')
write('\n')

#Grammar.txt
grammarRules = []
grammarContents = []
rawgrammar = open('Grammar.txt', 'r').readlines()
for i in rawgrammar:
    grammarRules.append(i[:i.index(':')])
    grammarContents.append()
    grammarContents[-1].append(i[i.index('[')+1:i.index(',')])
    grammarContents[-1].append(i[i.index(',')+1:-1])

for i, (r, c) in enumerate(zip(grammarRules, grammarContents)):
    write('def p_expression_'+c[0]+' (p):')
    write("\t'''"+r+"'''\n")
    write('\tp[0] = '+c[1])
write('\n')

#Precedence.txt
precedences = []
rawPrecedence = open('Precedence.txt', 'r').readlines()
for i in rawPrecedence:
    I = i[1:-1]
    precedences.append(I.split(','))
write('precedence = (')
for i in precedences:
    write('(')
    write(', '.join(i))
    write(')')
write(')\n')

#Other.txt
rawOther = open('Other.txt', 'r').readlines()
write('t_ignore = '+rawOther[0]+'\n')

write('def t_error(t):')
write('\t'+rawOther[1]+'\n')
write('\tt.lexer.skip(1)\n')

write('def p_error(p):')
write('\t'+rawOther[2]+'\n')

write('''while True:
    code = input('Expression: ')
    
    parser = yacc.yacc()
    
    # Example parsing
    lexer = lex.lex()
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"{tok.type}, {tok.value}")
    
    result = parser.parse(code)
    print("Result:", result)''')

output_file.close()
