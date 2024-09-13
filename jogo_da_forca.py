import random
import numpy as np

def forma(String):
    return String.lower()

def escolha_tentativa(letra_tentativa):
    while True:
        try:
            letra_tentativa = input("Escolha uma letra: ")
            if len(letra_tentativa) != 1 or not letra_tentativa.isalpha():
                raise ValueError
            elif letra_tentativa in lcertas:
                print('Letra já escolhida, por favor, digite outra letra:')
                continue
            elif letra_tentativa in lerradas:
                print('Letra já escolhida, por favor, digite outra letra:')
                continue
        except ValueError:
            print("Por favor, insira apenas uma letra do alfabeto.")
            continue
        else:
            return letra_tentativa
#Base de dados (palavras)
filmes = ['uma noite no museu', 'era uma vez', 'harry potter', 'jogos vorazes', 'king kong', 'bad boys','star wars','a vida e bela','jogos mortais','mercenarios','todo mundo em panico','uma noite no museu','minha mae e uma peça','divergente','jurassic park']
cores = ["vermelho", "laranja", "amarelo", "verde", "azul", "índigo", "violeta", "branco", "preto", "cinza", "marrom", "rosa", "roxo", "turquesa", "ciano", "magenta", "ouro", "prata", "bronze"]
musicas = ["Garota de Ipanema","Chega de Saudade","Águas de Março","O Leãozinho","Mas Que Nada","Aquarela","Felicidade","Construção","Trem das Onze","Asa Branca","Carinhoso","Meu Erro","Tropicália","Alegria, Alegria","Cálice","Pais e Filhos","Brasil","Faroeste Caboclo","O Bêbado e a Equilibrista","Vai Passar"]
lugares = ["Cristo Redentor", "Pao de Acucar", "Copacabana", "Ipanema", "Fernando de Noronha","Salvador", "Pelourinho", "Praia da Pipa", "Foz do Iguacu", "Lencois Maranhenses","Ouro Preto", "Recife Antigo", "Porto de Galinhas", "Manaus", "Praia do Forte","Beto Carrero World", "Parque Nacional da Tijuca", "Ilhabela", "Sao Paulo", "Brasilia"]
objetos = ["caneta", "caderno", "celular", "computador", "oculos de sol", "chaveiro","garrafa dagua", "carteira", "guarda-chuva", "fones de ouvido", "mochila","carro", "bicicleta", "relogio", "anel", "colar", "televisao", "ventilador","travesseiro", "cadeira", "mesa", "controle remoto", "agenda", "esmalte","tenis", "meias", "bolsa", "escova de dentes", "pente", "shampoo","condicionador", "sabonete", "toalha", "espelho", "vaso", "caneca","copo", "prato", "faca", "garfo", "colher", "panela", "frigideira","escorredor", "fogao", "geladeira", "freezer", "micro-ondas","liquidificador"]

lcertas=[]
lerradas=[]
ipalavra=[]
posicoes=[]
tentativa=()
tentativas_restantes=6
loop = 1
genero = "Escolha o tema desejado:\n1 - filmes\n2 - cores\n3 - musicas\n4 - lugares\n5 - objetos\n"

forca6 = '''
                   --------
                   |      |
                   |      
                   |     
                   |      
                   |      
                  ---
'''
forca5 = '''
                   --------
                   |      |
                   |      O
                   |     
                   |      
                   |     
                  ---
'''
forca4 = '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
'''
forca3 = '''
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                  ---
'''
forca2 = '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     
                  ---
'''
forca1 = '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                  ---
'''
forca0 = '''
                   --------
                   |      |
                   |      O            OPS! Não foi desta vez.         
                   |     \|/
                   |      |
                   |     / \\
                  ---
            
'''
print('*Bem vindo ao jogo da Forca!*')
while loop == 1:
#Escolha do gênero com Tratamento de Erro
    while True:
        try:
            n1 = int(input(genero))
            if n1 < 1 or n1 > 5:
                print("Número fora do intervalo permitido.")
                continue
        except ValueError:
            print("Caracter inválido. Por favor, digite um número de 1 a 5.")
            continue
        else:
            break
    #Bloco de escolha de gênero e palavra
    if n1 == 1:
        palavra_certa = random.choice(filmes)
        print("Você escolheu o gênero 'Filmes'!")
    elif n1 == 2:
        palavra_certa = random.choice(cores)
        print("Você escolheu o gênero 'Cores'!")
    elif n1 == 3:
        palavra_certa = random.choice(musicas)
        print("Você escolheu o gênero 'Músicas'!")
    elif n1 == 4:
        palavra_certa = random.choice(lugares)
        print("Você escolheu o gênero 'Lugares'!")
    elif n1 == 5:
        palavra_certa = random.choice(objetos)
        print("Você escolheu o gênero 'Objetos'!")
        
    #Montando a palavra
    palavra_temporaria = str(forma(palavra_certa))
    palavra = palavra_temporaria.replace(' ','-')
    nletra = len(palavra)
    while len(ipalavra)<nletra:
        ipalavra.append("")
    for x, y in enumerate(palavra):
        if y == '-':
            posicoes.append(x)
    for x in posicoes:
            ipalavra[x] = '-'
    posicoes.clear()
    print(forca6)
    print(ipalavra)
    #Escolha da letra
    while (not tentativas_restantes==0):
        if not "" in ipalavra:
            print('a palavra certa era:', palavra_certa,'\nVocê ganhou o jogo, parabéns!')
            break
        tentativa = escolha_tentativa(tentativa)
        if tentativa in palavra:
            lcertas.append(tentativa)
            for x, y in enumerate(palavra):
                if y == tentativa:
                    posicoes.append(x)
            for x in posicoes:
                ipalavra[x] = tentativa
            posicoes.clear()
        if tentativa not in palavra:
            lerradas.append(tentativa)
            tentativas_restantes-=1
        if tentativas_restantes==6:
            print(forca6)
        elif tentativas_restantes==5:
            print(forca5)
        elif tentativas_restantes==4:
            print(forca4)
        elif tentativas_restantes==3:
            print(forca3)
        elif tentativas_restantes==2:
            print(forca2)
        elif tentativas_restantes==1:
            print(forca1)
        elif tentativas_restantes==0:
            print(forca0)
            print('A palavra era:',palavra_certa)
        print(ipalavra)
        print('letras erradas:',lerradas)
    
    #Encerramento/Loop2
    while True:
        try:
            loop = int(input('Deseja jogar novamente?\n1- Sim!\n2- Não'))
            if loop != 1 and loop != 2:
                print("Caracter inválido. Por favor, escolha a opção 1 ou 2.")
                continue
        except ValueError:
            print("Caracter inválido. Por favor, escolha a opção 1 ou 2.")
            continue
        else:
            break
    if loop == 1:
        lcertas.clear()
        lerradas.clear()
        ipalavra.clear()
        posicoes.clear()
        tentativa=()
        tentativas_restantes=6
        continue
    if loop == 2:
        print('Obrigado por jogar Forca!')
        break


# In[ ]: