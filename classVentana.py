from typing import Any

class Ventana:
    __titulo= ''
    __yInfDer=''
    __xInfDer=''
    __ySupIzq=''
    __xSupIzq=''
    def __init__(self, titulo, xSupIzq=0, ySupIzq=0, xInfDer=500, yInfDer=500):
        self.__titulo= titulo
        self.__xSupIzq= xSupIzq
        self.__ySupIzq= ySupIzq
        self.__xInfDer= xInfDer
        self.__yInfDer= yInfDer
    
    def getTitulo(self):
        return self.__titulo
    
    def getXsup(self):
        return self.__xSupIzq
    def getYsup(self):
        return self.__ySupIzq
    def getXinf(self):
        return self.__xInfDer
    def getYinf(self):
        return self.__yInfDer
    
    def ancho(self):
        anch= (self.__xInfDer - self.__xSupIzq)
        return anch
    def alto(self):
        alt = ( self.__ySupIzq - self.__yInfDer)
        return alt
    
    def mostrar(self):
        print(f' Ventana en : x={self.__xInfDer} y={self.__ySupIzq}')

    def moverDerecha(self, valor):
        self.__xSupIzq += valor
        self.__xInfDer += valor
    def moverIzquierda(self, valor):
        self.__xSupIzq -= valor
        self.__xInfDer -= valor
   
    def bajar(self, ySupIzq=1, yInfDer=1):
        self.__ySupIzq -= ySupIzq
        self.__yInfDer -= yInfDer
    def subir(self, ySupIzq=1, yInfDer=1):
        self.__ySupIzq += ySupIzq
        self.__yInfDer += yInfDer  


    