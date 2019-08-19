'''
Desafio 001
Crie um programa que escreva "Olá, mundo!" na tela.
'''
print('Opção 1: Cadeia de Caracteres')
print('Olá, Mundo!')
print('') # pula uma linha
print('Opção 2: Com uso de Variável')
msg = 'Olá, Mundo!'
print(msg)
print('') # pula uma linha
print('Opção 3: Com uso de Variável e Método')
msg = 'Olá, mundo!'
print('{}'.format(msg))
print('') # pula uma linha
print('Opção 3: Com uso de Variável e Método (versão moderna)')
msg = 'Olá, Mundo!'
print(f'{msg}')
print('') # pula uma linha
print('Opção 4: Com uso de Função')
def msg():
    print('Olá, Mundo')
msg()
