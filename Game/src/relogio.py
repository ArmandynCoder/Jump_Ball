from time import sleep
from sys import exit

class Relogio:
    def __init__ (self):
        self.__tempo_inicial = 0
        self.__tempo_final = 10
        self.__loop = True
    
    def segundos(self):
        if self.__tempo_inicial == self.__tempo_final:
            self.__loop == False
            exit()
        if self.__tempo_inicial != self.__tempo_final:
            self.__tempo_inicial += 1
            print(self.__tempo_inicial)
        sleep(1)
