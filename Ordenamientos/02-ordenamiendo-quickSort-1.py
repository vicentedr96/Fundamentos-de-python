import time

class Ordenamiento():

    #constructor
    def __init__(self,arr=[]):
        self.arr=arr
        self.comp=0
        self.tiempoFinal=0
        self.cambios=0
    
    def orden_creciente(self,arr=None):

        if(arr!=None):
            self.arr=arr
        if(len(self.arr)<1):
            return [] 

        izquierda=list([])
        derecha=list([])
        pivote= list([self.arr[0]])

        for i in range(1,len(self.arr),1):
            self.comp+=1
            if self.arr[i]<pivote[0]:
                self.cambios+=1
                izquierda.insert(0,self.arr[i])
            else:
                self.cambios+=1
                derecha.insert(0,self.arr[i])

        self.arr=self.orden_creciente(izquierda) + pivote + self.orden_creciente(derecha);
        return self.arr
    
    def main(self,arr):
        self.arr=arr
        self.cambios=0
        start=time.time()
        self.orden_creciente(self.arr)
        end=time.time()
        self.tiempoFinal=(end-start)

    def datos(self):
            print(f'arreglo:{self.arr}\r\ncomparaciones:{self.comp}\r\ntiempo:{self.tiempoFinal}\r\ncambios:{self.cambios}')

orden=Ordenamiento()
orden.main([9,44,32,12,7,45,31,98,35,41,8,20,27,32,83,64,61,28,39,93,29,92,17])
orden.datos();