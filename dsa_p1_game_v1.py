#Projeto 1 - Desenvolvimento de Jogo da Forca em Python

import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():
    #Windows
    if name == 'nt':
        _ = system('cls')
    #Mac ou Linux 
    else:
        _ = system('clear')
        
#Função
def game():
    
    limpa_tela()
    print("\n Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo: \n")
    
    #Lista de palavras para o jogo
    palavras = ['alfaiate', 'marmota', 'linguagem','perfume','aparato','habilidade','tecnologia']

    #Escolhe randomicamente uma palavra da lista
    palavra = random.choice(palavras)
    
    #lista comprehension para exibição dos traços
    letras_descobertas = ['_' for letra in palavra]
    
    #número de chances
    chances = 8
    
    #lista de erros
    letras_erradas = []
    
    #loop enquanto as chances  forem maior que zero
    while chances > 0:
        
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        #Tentativa
        tentativa = input("\n Digite uma letra: ").lower()
        
        #Condicional
        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
            
        #Condional 2
        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra)
            break
        
        
#Bloco main
if __name__ == "__main__":
    game()