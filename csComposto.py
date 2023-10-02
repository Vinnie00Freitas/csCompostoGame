from time import sleep
# Colocando as regras do jogo
print("\n\n\n-----------------------------Vamos jogar CS Composto-------------------------------------\n\n")
sleep(1)
print("REGRAS DO JOGO:\n1 - Não pode colocar palavras que iniciam com a letra 'C' ou 'S'\n2 - Não pode usar palavras compostas ou duas ou mais palavras numa mesma rodada, Ex: Para-raio, Carro elétrico... ")

for i in range(3):
    print('============================================') 
    sleep(0.5)
sleep(0.5)

# Definindo a classe Game 

class Game:
    def __init__(self, word): # metodo construtor
        self.word = word

    def start(self): # metodo de iniciar 
        while self.is_valid():
            print(f'\n{self.word}')
            self.word = str(input('Proxima palavra: ')).upper()
            sleep(0.5)

        self.end() # quando essa linha é executada o jogo é encerrado

    def is_valid(self): # metodo definir as condições
        return (
            self.word[0] != 'S'
            and self.word[0] != 'C'
            and ' ' not in self.word
            and '-' not in self.word
        )

    def end(self): # metodo que indica o final do jogo
        print('\nEi, qual é a regra do jogo?\nVocê perdeu\n\n')

g = Game('.')
g.start()