import time
class Ordenamiento():
    
    #constructor
    def __init__(self,arr=[]):
        self.arr=arr
        self.comp=0
        self.tiempoFinal=0
        self.cambios=0
    
    def orden_seleccion(self,arr=None):

        if(arr!=None):
            self.arr=arr
        if(len(self.arr)<1):
            return [] 

        start=time.time()
        self.cambios=0
        self.comp=0

        for i in range(0,len(self.arr),1):
            min=i
            for j in range(i+1,len(self.arr)):
                self.comp+=1
                if(self.arr[min]>self.arr[j]):
                    min=j

            self.cambios+=1
            tmp= self.arr[i]
            self.arr[i]=self.arr[min]
            self.arr[min]=tmp
        
        end=time.time()
        self.tiempoFinal=(end-start)
        
    
    def datos(self):
        print(f'arreglo:{self.arr}\r\ncomparaciones:{self.comp}\r\ntiempo:{self.tiempoFinal}\r\ncambios:{self.cambios}')

orden=Ordenamiento([9,44,32,12,7,45,31,98,35,41,8,20,27,32,83,64,61,28,39,93,29,92,17])
orden.orden_seleccion()
orden.datos();