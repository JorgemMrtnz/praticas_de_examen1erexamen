import random as rd
import sys as SystemExit
cara = input("cara o cruz :")
Azar = rd.randint(0,1) 
if Azar == 0 and cara == "cara":
    True
elif Azar == 1 and cara == "cruz":
    True
elif Azar == 0 and cara == "cruz":
    print ("perdiste")
    exit()
elif Azar == 1 and cara == "cara":
    print ("perdiste")
    exit()  
    
Lista = ["Adrian", "Sergio", "David" ,"Hector", "Santiago", "Jorge", "Diego", "Marco", "Rojo" ]
N = int(input("ingresa en cuanto quieres dividir la lista: "))
rd.shuffle(Lista)   
for i in range(0, len(Lista), N):
    print(Lista[i:i + N])

