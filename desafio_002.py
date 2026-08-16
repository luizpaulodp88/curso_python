# ========== desafio 002 Você nasceu em ... ==============

# Solicita ao usuário o dia, o mês e o ano de nascimento, armazenando cada valor em sua respectiva variável
dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

# Exibe uma mensagem formatada combinando as variáveis para mostrar a data completa de nascimento
print(f"Você nasceu em {dia}/{mes}/{ano}")

'''
Funções utilizadas:

* input(): Função nativa do Python usada para receber dados de entrada inseridos pelo usuário através do teclado (retorna uma string).

* print(): Função nativa do Python usada para exibir saídas (mensagens ou valores) na tela do terminal.

* f-string (f"..."): Mecanismo de formatação de strings do Python que permite inserir variáveis diretamente dentro da string usando chaves {}.'''
