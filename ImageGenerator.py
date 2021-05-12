import numpy as np
from PIL import Image
import math
import random as rm

dimTotal = pow(2, 10) #2^10=1024

#Tengo que aprender que significa esto, pero por ahora funciona
data = np.zeros( (dimTotal, dimTotal, 3), dtype=np.uint8 )

dimAparente = 16

for ronda in range(dimAparente):

    for i in range(ronda+1):
        for j in range(ronda+1):
        
            if( math.sqrt( pow(i, 2) + pow(j, 2)) < float(ronda)):
                #print(ronda, i, j, math.sqrt( pow(i, 2) + pow(j, 2)), float(ronda))
                continue
                
            #todo el rngo de colores
            #low = int(math.floor(255/dimAparente))*ronda
            #high = int(math.floor(255/dimAparente))*(ronda+1)
            
            #lgunos colores
            #low  = 85+int(math.floor(85/dimAparente))*ronda
            #high = 85+int(math.floor(85/dimAparente))*(ronda+1)
            
            #todo el rngo dividido ms pequeno
            low  = int(math.floor(255/4))*ronda
            high = int(math.floor(255/4))*(ronda+1)
            
            a = rm.randint(low,high)
            b = rm.randint(low,high)
            c = rm.randint(0,255)
            
            for m in range( int(dimTotal/dimAparente)*i, int(dimTotal/dimAparente)*(i+1) ):
                for n in range( int(dimTotal/dimAparente)*j, int(dimTotal/dimAparente)*(j+1) ):

                    data[m, n] = [a, b, c] 
                 

#for i in range(dimAparente):
#    for j in range(dimAparente):
#        
#
#        a = rm.randint(0,255)
#        b = rm.randint(0,255)
#        c = rm.randint(0,255)
#        
#        for m in range( int(dimTotal/dimAparente)*i, int(dimTotal/dimAparente)*(i+1) ):
#            for n in range( int(dimTotal/dimAparente)*j, int(dimTotal/dimAparente)*(j+1) ):
#
#                data[m, n] = [b, b, b]


#for i in range(1024):
#    for j in range(1024):
#        a = rm.randint(0,255)
#        b = rm.randint(0,255)
#        c = rm.randint(0,255)
#        data[i, j] = [a, b, c]

#for i in range(1024):
#    for j in range(513, 1024):
#        data[i, j] = [3, 200,   38]

#data[512,512] = [254, 0,   0]
#data[512,513] = [  0, 0, 255]

img = Image.fromarray( data )
img.show()
