class Nodo():
    
    #constructor
    def __init__(self,datos):

        self.__datos=datos;
        self.__enlace=None;

    def get_datos(self):
        return self.__datos

    def set_datos(self,datos):
        self.__datos=datos

    def get_enlace(self):
        return self.__enlace

    def set_enlace(self,siguiente):
        self.__enlace=siguiente

    
