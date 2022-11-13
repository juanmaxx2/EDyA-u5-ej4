import numpy as np
from bucket import Bucket

class Hash:
    __Hash = None
    __tam = None
    __primario = None
    __overflow = None
    __actualOverflow = None

    def __init__(self, tam, tamBucket):
        self.__tam = tam
        i = math.floor(tam/tamBucket)
        while not self.esprimo(i):
            i += 1
        self.__primario = i
        self.__overflow = math.floor(i*0.3)
        self.__actualOverflow = self.__primario + 1
        self.__Hash = np.empty(i + self.__overflow, dtype = Bucket)
        for i in range(len(self.__Hash)):
            self.__Hash[i] = Bucket(tamBucket)

    def Insertar(self, num):
        i = str(num)[-2:]
        i = int(i)
        if i > self.__primario:
            i = (i % self.__primario)
        resultado = self.__Hash[i].agregar(num)
        if not resultado:
            if self.__actualOverflow < len(self.__Hash) and self.__Hash[self.__actualOverflow].estaLleno():
                self.__actualOverflow +=1
            if self.__actualOverflow == len(self.__Hash):
                print("Tabla Llena")
            else:
                self.__tablaHash[self.__actualOverflow].agregar(num)

    def buscar(self, num):
        i = str(num)[-2:]
        i = int(i)
        if i > self.__primario:
            i = (i % self.__primario)
            resultado = False
            if self.__Hash[i].isElement(num):
                print("Esta en primario")
                resultado = True
        else:
            for i in range(self.__primario, len (self.__Hash)):
                if self.__Hash[i].isElement(num):
                    print(("Esta en overflow"))
                    resultado = True
        return resultado

    def Mostrar(self):
        for i in range(self.__primario+1):
            print(self.__Hash[i])
            print("Overflow:")
            for j in range(self.__primario, len(self.__Hash)):
                print(self.__Hash[j])

    def esPrimo(self, num):
        resultado = True
        i = 2
        while i < num and resultado:
            if (num % i) == 0:
                resultado = False
            i += 1
        return resultado