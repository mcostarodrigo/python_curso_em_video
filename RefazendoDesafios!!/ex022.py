import time
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
dividido = nome.split()
print(f'Seu primeiro nome é {dividido [0]}, e ele tem {len(dividido[0])} letras')
