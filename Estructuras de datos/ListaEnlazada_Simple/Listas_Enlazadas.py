
from Nodo import Nodo
class Listas_Enlazadas():

    #constructor
    def __init__(self):
        self.__primero=None
        self.__size=0

    def get_size(self):
        return self.__size

    def visualizar(self):
        tmp=self.__primero
        while(tmp!=None):
            print(tmp.get_datos())
            tmp=tmp.get_enlace();
    
    def insertar_inicio(self,datos):
        if (self.__primero is None):
            self.__primero=Nodo(datos)
        else:
            tmp=self.__primero
            nuevo=Nodo(datos)
            nuevo.set_enlace(tmp)
            self.__primero=nuevo
        self.__size+=1

    def insetar_final(self,datos):
        if(self.__primero is None):
            self.__primero=Nodo(datos)
        else:
            nuevo=Nodo(datos)    
            tmpF=self.__primero

            while(tmpF.get_enlace()!=None):
                tmpF=tmpF.get_enlace()
            
            tmpF.set_enlace(nuevo)
        self.__size+=1


    def esta_vacio(self):
        if(self.__primero==None):
            return True
        else:
            return False
            
    def eliminar_primero(self):
        if(self.esta_vacio()!=True):
            self.__primero= self.__primero.get_enlace()
            self.__size-=1
    
    def eliminar_ultimo(self):
        if(self.esta_vacio()!=True):
            tmp=self.__primero
            while(tmp.get_enlace().get_enlace()!=None):
                tmp=tmp.get_enlace()
            tmp.set_enlace(None)
            self.__size-=1

    def editar_por_posicion(self,posicion,datos):
        if(posicion>=0 and posicion<self.__size):
            if(posicion==0):
                self.__primero.set_datos(datos)
            else:
                tmp=self.__primero
                i=0
                while(i<posicion):
                    tmp=tmp.get_enlace()
                    i+=1
                tmp.set_datos(datos)


lista = Listas_Enlazadas()
lista.insertar_inicio(1)
lista.insertar_inicio(10)
lista.insetar_final(3)
lista.insetar_final(2)
lista.eliminar_ultimo()
lista.eliminar_primero()
lista.editar_por_posicion(0,100)
lista.visualizar()