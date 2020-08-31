'''
Criar uma burrice artificial que fale contigo
Nome: Gabriel
'''

#Apresentações
nome = input('Olá, meu nome é Gabriel! Qual o seu nome? ')
idade = input('Que nome bonito! Quantos anos você tem? ')
print('Que dahora! Você parece ser legal!')

#Série de Perguntas
p1 = input('Quero te conhecer mais! Você gosta de animes? \n 1. Sim \n 2. Não \n R= ')

if p1 == '1':
    p2 = input('Ótimo! Qual o seu preferido? \n 1. Darling in the FranXX \n 2. Bleach \n 3. One Piece \n 4. Naruto \n 5. Golden Boy \n 6. Todos R= ')
    print('Tu é o cara, só assiste anime baum!')
else:
    print('Decepcionei! Tu é um lixo mano!')
