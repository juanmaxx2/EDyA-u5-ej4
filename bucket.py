from numpy import np
class Bucket:
    __arre = None
    __contador = None

    def __init__(self, tam):
        self.__arre = np.zeros(tam, dtype = int)
        self.__contador = 0
    
    def agregar (self, elem):
        resultado = False
        if elem in self.__arre:
            print("clave repetida")
        elif self.__contador < len(self.__arre):
            self.__arre[self.__contador] = elem
            self.__contador += 1
            resultado = True
        return resultado