import random
import time 

class Ordenamiento:

    #constructor
    def __init__(self,lista=[]): 
        self.lista=lista
        self.comparaciones=0 
        self.cambios=0
        self.tiempoFinal=0

    #Ordenamiento borbuja clasica
    def ordenamiento_borbuja_v1(self):
        self.comp=0
        self.cambios=0
        start=time.time()
        for j in range(len(self.lista)-1,0,-1):
            for i in range(j):
                self.comp+=1
                if self.lista[i]>self.lista[i+1]:
                    self.cambios+=1
                    temp = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.lista[i+1] = temp
        end=time.time()
        self.tiempoFinal=(end-start)
    
    #Ordenamiento borbuja mejorado
    def ordenamiento_borbuja_v2(self):
        self.comp=0
        self.cambios=0
        intercambios = True
        numPasada = len(self.lista)-1
        start=time.time()
        while numPasada > 0 and intercambios:
            intercambios = False
            for i in range(numPasada):
                self.comp+=1
                if self.lista[i]>self.lista[i+1]:
                    self.cambios+=1
                    intercambios = True
                    temp = self.lista[i]
                    self.lista[i] = self.lista[i+1]
                    self.lista[i+1] = temp
            numPasada = numPasada-1
        end=time.time()
        self.tiempoFinal=(end-start)

    def generar_lista_aleatoriamente(self,cantidad):
        self.lista=[random.randint(1,100) for n in range(cantidad)]

    def get_lista(self):
        if len(self.lista)!=0:
            print(f'Tiempo:{self.tiempoFinal} segundos\r\nComparaciones:{self.comp}\r\nCambios:{self.cambios}\r\nLista: {self.lista}')
        else:
            print('Lista vacia')
            
    def set_lista(self,lista):
        self.lista=lista
    
#Instanciar la clase
ordenamiento=Ordenamiento()
#Colocamos los valores de nuestra lista
ordenamiento.set_lista([5,7,3,1,8,4,9,2,6])
#Generamos aletoriamente
ordenamiento.generar_lista_aleatoriamente(100)
#Ejecutamos el ordenamiento borbuja v1
ordenamiento.ordenamiento_borbuja_v1()
#Mostramos la lista ordenada
ordenamiento.get_lista()





                
            

