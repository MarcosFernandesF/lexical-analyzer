# README - Analisadores Léxicos

## Introdução

Este repositório contém duas partes de um trabalho sobre análise léxica:

- **Parte A**: Analisador léxico simples.
- **Parte B**: Analisador léxico utilizando a biblioteca PLY.

## Versões e Depedências Utilizadas

- Python 3.12.3
- pip (gerenciador de pacotes do Python)
- biblioteca PLY.

## Instruções de Instalação

### 1. Instalar Python e pip

Se você não tem o Python instalado, siga os passos abaixo:

1. Abra o terminal.
2. Atualize o gerenciador de pacotes:

   ```bash
   sudo apt update
   ```

3. Instale o Python:

    ```bash
   sudo apt install python3
   ```
4. Instale o pip:

    ```bash
   sudo apt install python3-pip
   ```

### 2. Criar um Ambiente Virtual

Necessário para rodar o PLY.

1. Instale o ```venv```

2. Navegue até o diretório onde o projeto está localizado:

   ```bash
   cd /caminho/para/o/projeto
   ```

3. Crie o ambiente virtual:

   ```bash
   python3 -m venv nome-do-ambiente
   ```

4. Ative o ambiente virtual:

   ```bash
   source /nome-do-ambiente/bin/activate
   ```

### 3. Instalando o PLY

Com o ambiente virtual ativado, simplesmente instale a biblioteca PLY:

   ```bash
   pip install ply
   ```

## Execução do Projeto

### Parte A:

1. Navegue até o diretório onde o código da Parte A está localizado.
2. Execute o analisador com o caminho para o arquivo de código que deseja analisar, exemplo:

   ```bash
   python3 parteA.py parteACorreto.txt ou python3 parteA.py parteAIncorreto.txt
   ```

### Parte B:

1. Navegue até o diretório onde o código da Parte B está localizado.
2. Execute o analisador com o caminho para o arquivo de código que deseja analisar, exemplo:

   ```bash
   python3 parteB.py parteBCorreto.lsi ou python3 parteB.py parteBIncorreto.lsi
   ```
