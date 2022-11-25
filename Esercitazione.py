import random 
x= random.randint (0,50)
y= random.randint (0,50)
z= random.randint (0,50)
if x<y and x<z:
    print(x)
    if y<z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif y<z:
    print(y)
    if x<z:
        print(x)
        print(z)
    else:
        print(z)
        print(x)
else:
    print(z)
    if x<y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)

print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")

automobili= ["Abarth", "Ferrari", "Lamborghini", "Maserati", "FIAT"]
Moto= ["Honda", "Suzuki", "BMW", "Duke"]
aM= automobili + Moto
aM.sort ()
print(aM)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")

import random
lista= []
for i in range (0,50):
    lista.append (random.randint (0,10000000000))
listadispari=[]
for x in lista:
    if x%2==1:
        listadispari.append(x)
lista=listadispari
print(lista)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")

import random
lista= []
Valori_Stampati= 0
for i in range(50):
    lista.append (random.randint(1,100))
for x in lista:
    if x>50 or x<10:
        print(x)
        Valori_Stampati= Valori_Stampati + 1
print(Valori_Stampati)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")
