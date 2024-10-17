#####################################################
# PARTE A - Analisador Léxico                       #
# Autor - Marcos Roberto Fernandes Filho (22100915) #
#####################################################

import argparse

# Iniciais dos operadores lógicos.
INICIAL_OPERADORES_LOGICOS = {
    '>', '<', '=', '!'
}

# Lista de palavras-chave usada.
PALAVRAS_CHAVES = {'if', 'else', 'while', 'return'}

# Classe principal do analisador.
class AnalisadorLexico:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.tokens = []  # Lista de tokens encontrados
        self.tabela_simbolos = []  # Lista para armazenar palavras-chave
        self.linha = 1
        self.coluna = 1
        self.posicao = 0
        self.codigo = self._carregar_codigo()
    
    # Responsável por abrir o arquivo txt.
    def _carregar_codigo(self):
        try:
            with open(self.caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                return arquivo.read()
        except FileNotFoundError:
            print(f"Erro: Arquivo '{self.caminho_arquivo}' não encontrado.")
            return ''
    
    # Método principal do analisador léxico.
    def analisar(self):
        while self.posicao < len(self.codigo):
            char = self.codigo[self.posicao]
            if char.isspace():
                self._processar_espaco()
            elif char.isalpha():
                self._processar_identificador()
            elif char.isdigit():
                self._processar_numero()
            elif char in INICIAL_OPERADORES_LOGICOS:
                self._processar_operador_relacional()
            else:
                inicio = self.posicao

                while self.posicao < len(self.codigo) and not self.codigo[self.posicao].isspace():
                    self.posicao += 1

                lexema_invalido = self.codigo[inicio:self.posicao]
                print(f"Erro léxico: Lexema inválido '{lexema_invalido}' na linha {self.linha}, coluna {self.coluna}")
                self.coluna += (self.posicao - inicio)
        
        return self.tokens

    # Obtém o lexema a partir do código e dos indices.
    def _obter_lexema(self, inicio):
        return self.codigo[inicio:self.posicao]

    # Armazena os tokens se ainda não estiver entre os tokens identificados.
    def _armazenar_token(self, tipo, lexema):
        token = (tipo, lexema, self.linha, self.coluna)
        if token not in self.tokens:  
            self.tokens.append(token)

    # Armazena a palavra chave se já não estiver na tabela de símbolos.
    def _armazena_palavra_chave(self, lexema):
        if lexema not in [palavra[1] for palavra in self.tabela_simbolos]:
            self.tabela_simbolos.append(('PALAVRA_CHAVE', lexema, self.linha, self.coluna))

    # Faz o processamento dos caracteres em branco.
    def _processar_espaco(self):
        if self.codigo[self.posicao] == '\n':
            self.linha += 1
            self.coluna = 1
        else:
            self.coluna += 1
        self.posicao += 1
    
    
    # Faz o processamento dos identificadores.
    def _processar_identificador(self):
        inicio = self.posicao
        estado = 'INICIO'

        while self.posicao < len(self.codigo):
            char_atual = self.codigo[self.posicao]

            if estado == 'INICIO':
                if char_atual.isalnum():
                    estado = 'LETRA_OU_DIGITO'
                else:
                    print(f"Erro léxico: Caractere inválido {char_atual} na linha {self.linha}, coluna {self.coluna}")
                    break
            elif estado == 'LETRA_OU_DIGITO':
                if char_atual.isalnum():
                    pass
                else:
                    estado = 'ACEITACAO'
                    break
            elif estado == 'ACEITACAO':
                break

            self.posicao += 1
        
        lexema = self._obter_lexema(inicio);
        
        if lexema in PALAVRAS_CHAVES:
            self._armazena_palavra_chave(lexema);
        else:
            self._armazenar_token('IDENTIFICADOR', lexema);
        
        self.coluna += (self.posicao - inicio)
    
    # Faz o processamento dos números.
    def _processar_numero(self):
        inicio = self.posicao
        estado = 'INICIO'

        while self.posicao < len(self.codigo):
            char_atual = self.codigo[self.posicao]
            
            if estado == 'INICIO':
                if char_atual.isdigit():
                    estado = 'DIGITO'
                else:
                    print(f"Erro léxico: Caractere inválido {char_atual} na linha {self.linha}, coluna {self.coluna}")
                    break
            elif estado == 'DIGITO':
                if char_atual.isdigit():
                    pass
                else:
                    estado = 'ACEITACAO'
                    break
            elif estado == 'ACEITACAO':
                break

            self.posicao += 1

        lexema = self._obter_lexema(inicio);

        self._armazenar_token('NUMERO', lexema);
        
        self.coluna += (self.posicao - inicio)

    # Faz o processamento dos operadpres relacionais.
    def _processar_operador_relacional(self):
        inicio = self.posicao
        estado = 'INICIO'

        while self.posicao < len(self.codigo):
            char_atual = self.codigo[self.posicao]
            
            if estado == 'INICIO':
                if char_atual == '<':
                    estado = 'MENOR'
                elif char_atual == '=':
                    estado = 'IGUAL'
                elif char_atual == '>':
                    estado = 'MAIOR'
                elif char_atual == '!':
                    estado = 'EXCLAMACAO'
                else:
                    print(f"Erro léxico: Caractere inválido {char_atual} na linha {self.linha}, coluna {self.coluna}")
                    break
            elif estado == 'MENOR':
                if char_atual == '=':
                    estado = 'ACEITACAO'
                else:
                    break
            elif estado == 'IGUAL':
                if char_atual == '=':
                    estado = 'ACEITACAO'
                else:
                    break
            elif estado == 'MAIOR':
                if char_atual == '=':
                    estado = 'ACEITACAO'
                else:
                    break
            elif estado == 'EXCLAMACAO':
                if char_atual == '=':
                    estado = 'ACEITACAO'
                else:
                    break
            elif estado == 'ACEITACAO':
                break

            self.posicao += 1

        lexema = self._obter_lexema(inicio);

        self._armazenar_token('OPERADOR_RELACIONAL', lexema);
        
        self.coluna += (self.posicao - inicio)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analisador Léxico')
    parser.add_argument('caminho_arquivo', type=str, help='Caminho do arquivo de código a ser analisado')
    args = parser.parse_args()
    
    analisador = AnalisadorLexico(args.caminho_arquivo)
    
    if analisador.codigo:
        tokens = analisador.analisar()

        if any(tokens):
            print("\nTokens encontrados:")
            print("Tipo, Lexema, Linha, Coluna:")
            for token in tokens:
                print(token)

            # Imprimir a tabela de símbolos
            print("\nTabela de Símbolos:")
            print("Tipo, Lexema, Linha, Coluna:")
            for palavra_chave in analisador.tabela_simbolos:
                print(palavra_chave)
