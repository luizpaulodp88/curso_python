# ========== desafio 003 Soma de dois números, sem depuração de entrada de dados ==============

# Solicita ao usuário que digite o primeiro número, converte o valor recebido de string para inteiro e o armazena na variável 'num1'
num1 = int(input("Digite um número: "))

# Solicita ao usuário que digite o segundo número, converte o valor recebido de string para inteiro e o armazena na variável 'num2'
num2 = int(input("Digite outro número: "))

# Realiza a soma dos dois números inteiros e armazena o resultado na variável 'resulta'
resulta = num1 + num2

# Exibe uma mensagem formatada mostrando os números informados e o resultado da soma
print(f'A soma de {num1} + {num2} = {resulta}')

'''
Funções e métodos utilizados:

* input(): Função nativa do Python usada para receber dados de entrada inseridos pelo usuário através do teclado (retorna uma string).

* int(): Função nativa do Python usada para converter um valor (como uma string numérica) em um número inteiro.

* print(): Função nativa do Python usada para exibir saídas (mensagens ou valores) na tela do terminal.

* f-string (f"..."): Mecanismo de formatação de strings do Python que permite inserir variáveis diretamente dentro da string usando chaves {}.'''