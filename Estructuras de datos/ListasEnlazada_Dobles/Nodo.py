class Nodo():
    
    #constructor
    def __init__(self,datos):

        self.__datos=datos;
        self.__enlace_adelante=None;
        self.__enlace_atras=None;

    def get_datos(self):
        return self.__datos

    def set_datos(self,datos):
        self.__datos=datos

    def get_enlace_atras(self):
        return self.__enlace_atras

    def set_enlace_atras(self,atras):
        self.__enlace_atras=atras

    def get_enlace_adelante(self):
        return self.__enlace_adelante

    def set_enlace_adelante(self,adelante):
        self.__enlace_adelante=adelante

    
