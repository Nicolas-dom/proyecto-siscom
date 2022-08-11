##ejemplo para un codigo convolucional de 6 bit de entrada, de longitud 3, memoria 2 y salida 3 bits

import numpy as np   #puede almacenar y operar con datos de manera mucho más eficiente
from functools import reduce
from numpy import binary_repr
import sys    #para terminar el codigo cuando es verdadero
# maximo bit de entrada debe ser hasta 6

n=[ ]
for i in range(6):
    a = input("ingresar un bit de entrada (1 o 0): ")
    a = a.strip()
    if a == "0":
        n.append(0)
    elif a == "1":
        n.append(1) 
    else:
        print("numero incorrecto solo pueden ser '0' o '1' ")
        sys.exit()
   
print(n) 
print(type(n)) 
#n.reverse()  
q=q=[0]*len(n)+[0,0]
z=[]

for i in range(len(n)):                          #me invierte el q
    q=np.insert(q,0,n[i])
    q=np.delete(q,len(q)-1)
    g0=[5,6,7]
    g1=[4,5,6]
    g2=[3,4,5]
    g3=[2,3,4] 
    g4=[1,2,3]
    g5=[0,1,2]
    
    
  
    
print("codificacion de: ",n)   # primer bit es el menos significativo  
#print(q)

## salida
#
#b=np.append(a)         #la funcion np.take toma el valor de las variables, en zo los valores 5,6 y 7 de q
z0=np.take(q,g0)     #muestra el ingreso del primer bit
z1=np.take(q,g1)
z2=np.take(q,g2)
z3=np.take(q,g3)
z4=np.take(q,g4)
z5=np.take(q,g5)

def concatenar(a,b):
	return a^b         #or exclusivo bit a bit de a y b.

#suma el numero binario de los 3 bits 

zr0=reduce(concatenar,z0)         #la funcion reduce va a hacer la suma de z0 y la va a guardar en la variable zr0
zr1=reduce(concatenar,z1)
zr2=reduce(concatenar,z2)
zr3=reduce(concatenar,z3)
zr4=reduce(concatenar,z4)
zr5=reduce(concatenar,z5)


#realiza la suma del generador del primer y tercer bit
print("      ingresa el primer bit: ",z0)
print("suma de los 3 numeros binario: ",zr0)
data1 = z0[2]
data2 = z0[0]
sum_data = np.bitwise_xor(data1,data2)        #or exclusivo bit a bit
print("suma del primer bit con el tercer bit: ",sum_data)
print("el primer bit: ",z0[0])

print("      ingresa el segundo bit: ",z1)
print("suma de los 3 numeros binario: ",zr1)
data1 = z1[2]
data2 = z1[0]
sum_data1 = np.bitwise_xor(data1,data2)
print("suma del primer bit con el tercer bit: ",sum_data1)
print("el primer bit: ",z1[0])

print("      ingresa el tercer bit: ",z2)
print("suma de los 3 numeros binario: ",zr2)
data1 = z2[2]
data2 = z2[0]
sum_data2 = np.bitwise_xor(data1,data2)
print("suma del primer bit con el tercer bit: ",sum_data2)
print("el primer bit: ",z2[0])

print("      ingresa el cuarto bit: ",z3)
print("suma de los 3 numeros binario: ",zr3)
data1 = z3[2]
data2 = z3[0]
sum_data3 = np.bitwise_xor(data1,data2)
print("suma del primer bit con el tercer bit: ",sum_data3)
print("el primer bit: ",z3[0])


print("      ingresa el quinto bit: ",z4)
print("suma de los 3 numeros binario: ",zr4)
data1 = z4[2]
data2 = z4[0]
sum_data4 = np.bitwise_xor(data1,data2)
print("suma del primer bit con el tercer bit: ",sum_data4)
print("el primer bit: ",z4[0])

print("      ingresa el sexto bit: ",z5)
print("suma de los 3 numeros binario: ",zr5)
data1 = z5[2]
data2 = z5[0]
sum_data5 = np.bitwise_xor(data1,data2)
print("suma del primer bit con el tercer bit: ",sum_data5)
print("el primer bit: ",z5[0])



zf=np.hstack((z0[0],sum_data,zr0))    #concatena z0,sum_data y zr0
zf1=np.hstack((z1[0],sum_data1,zr1))
zf2=np.hstack((z2[0],sum_data2,zr2))
zf3=np.hstack((z3[0],sum_data3,zr3))
zf4=np.hstack((z4[0],sum_data4,zr4))
zf5=np.hstack((z5[0],sum_data5,zr5))


z=np.append(z,zf)
z = [np.int64(k) for k in z]            # tipos de datos numéricos en NumPy  np.int64 Integer    De -9223372036854775808 a 9223372036854775807
                                          #para pasarlo a valores de lista, sino es de tipo  numpy.ndarray
z=np.append(z,zf1)
z = [np.int64(k) for k in z]

z=np.append(z,zf2)
z = [np.int64(k) for k in z]

z=np.append(z,zf3)
z = [np.int64(k) for k in z]

z=np.append(z,zf4)
z = [np.int64(k) for k in z]

z=np.append(z,zf5)
z = [np.int64(k) for k in z]

print("la salida es: ",z)
print(type(z))

