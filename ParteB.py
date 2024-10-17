#####################################################
# PARTE B - Analisador Léxico Usando PLY            #
# Autor - Marcos Roberto Fernandes Filho (22100915) #
#####################################################

import ply.lex as lex
import argparse  # Para a linha de comando

# Lista de tokens
tokens = [
    'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'SEMICOLON'
]

# Palavras reservadas
reservadas = {
    'int': 'INT',
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
    'print': 'PRINT',
    'return': 'RETURN'
}

# Adicionando palavras reservadas aos tokens
tokens += list(reservadas.values())

# Expressões regulares
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'<>'
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'

def t_NUM(t):
    r'\d+'
    proximo_caractere_index = t.lexpos + len(t.value)
    dados_lexicos = t.lexer.lexdata

    if proximo_caractere_index < len(dados_lexicos) and dados_lexicos[proximo_caractere_index].isalpha():
        sequencia_invalida = t.value
        while proximo_caractere_index < len(dados_lexicos) and dados_lexicos[proximo_caractere_index].isalnum():
            sequencia_invalida += dados_lexicos[proximo_caractere_index]
            proximo_caractere_index += 1

        coluna = calcular_coluna(dados_lexicos, t)
        print(f"Erro léxico na linha {t.lineno}, coluna {coluna}: '{sequencia_invalida}'")
        t.lexer.skip(len(sequencia_invalida))
        return

    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def calcular_coluna(input, token):
    linha_inicio = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - linha_inicio) + 1

def t_error(t):
    coluna = calcular_coluna(t.lexer.lexdata, t)
    print(f"Erro léxico: '{t.value[0]}' na linha {t.lineno}, coluna {coluna}")
    t.lexer.skip(1)

lexer = lex.lex()

def testar_lexer(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = arquivo.read()
    lexer.input(dados)
    for token in lexer:
        coluna = calcular_coluna(dados, token)
        print(f"LexToken({token.type}, '{token.value}', {token.lineno}, {coluna})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analisador Léxico para a linguagem LSI-2024-2')
    parser.add_argument('caminho_arquivo', help='Caminho para o arquivo .lsi a ser analisado')
    args = parser.parse_args()

    testar_lexer(args.caminho_arquivo)
