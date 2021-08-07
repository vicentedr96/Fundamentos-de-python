from Nodo import Nodo

class Listas_Dobles():
    
    #constructor
    def __init__(self):
        self.__ultimo=None
        self.__primero=None
        self.__size=0

    def get_size(self):
        return self.__size

    def esta_vacio(self):
        if(self.__primero==None):
            return True
        else:
            return False

    def visualizar(self):
        tmp=self.__primero
        while(tmp!=None):
            print(tmp.get_datos())
            tmp=tmp.get_enlace_adelante()

    def insertar_inicio(self,datos):
        nuevo=Nodo(datos)
        if (self.__primero is None):
            self.__primero=nuevo
            self.__primero.set_enlace_adelante(None)
            self.__primero.set_enlace_atras(None)
            self.__ultimo=self.__primero
        else:
            nuevo.set_enlace_atras(None)
            nuevo.set_enlace_adelante(self.__primero)
            self.__primero.set_enlace_atras(nuevo)
            self.__primero=nuevo
        self.__size+=1

    def insetar_final(self,datos):
        nuevo=Nodo(datos)
        if(self.esta_vacio()):
            self.__primero=nuevo;
            self.__primero.set_enlace_adelante(None)
            self.__primero.set_enlace_atras(None)
            self.__ultimo=self.__primero
        else:
            self.__ultimo.set_enlace_adelante(nuevo)
            nuevo.set_enlace_atras(self.__ultimo)
            nuevo.set_enlace_adelante(None)
            self.__ultimo=nuevo
        self.__size+=1

    def eliminar_primero(self):
        if(self.esta_vacio()!=True):
            self.__primero=self.__primero.get_enlace_adelante()
            self.__primero.set_enlace_atras(None)
            self.__size-=1

    def eliminar_ultimo(self):
        if(self.esta_vacio()!=True):
            self.__ultimo=self.__ultimo.get_enlace_atras()
            self.__ultimo.set_enlace_adelante(None)
            self.__size-=1

    def editar_por_posicion(self,posicion,datos):
        if(posicion>=0 and posicion<self.__size):
            if(posicion==0):
                self.__primero.set_datos(datos)
            else:
                tmp=self.__primero
                i=0
                while(i<posicion):
                    tmp=tmp.get_enlace_adelante()
                    i+=1
                tmp.set_datos(datos)

lista = Listas_Dobles()
lista.insertar_inicio(18)
lista.insertar_inicio(29)
lista.insetar_final(8)
lista.eliminar_primero()
lista.eliminar_ultimo()
lista.editar_por_posicion(0,10)
lista.visualizar()