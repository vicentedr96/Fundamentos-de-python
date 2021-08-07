import time
class Ordenamiento():
    
    #constructor
    def __init__(self,arr=[]):
        self.arr=arr
        self.comp=0
        self.tiempoFinal=0
        self.cambios=0
    
    def orden_shell(self,arr=None):

        if(arr!=None):
            self.arr=arr
        if(len(self.arr)<1):
            return [] 

        start=time.time()
        self.cambios=0
        self.comp=0

        length=len(self.arr)
        interval= length//2
        while interval>0:
            for i in range(interval,length):
                insert_v=self.arr[i]
                insert_i=i
                while insert_i>=interval and self.arr[insert_i-interval]>insert_v:
                    self.comp+=1
                    self.cambios+=1
                    self.arr[insert_i]=self.arr[insert_i-interval]
                    insert_i-=interval
                self.cambios+=1
                self.arr[insert_i]=insert_v

            interval//=2
        
        end=time.time()
        self.tiempoFinal=(end-start)
    
    def datos(self):
        print(f'arreglo:{self.arr}\r\ncomparaciones:{self.comp}\r\ntiempo:{self.tiempoFinal}\r\ncambios:{self.cambios}')

orden=Ordenamiento([9,44,32,12,7,45,31,98,35,41,8,20,27,32,83,64,61,28,39,93,29,92,17])
orden.orden_shell()
orden.datos();