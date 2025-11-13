import random as rd
import webbrowser
valido = False
while not valido:
    cara = input("cara o cruz :")
    if cara == "cara" or cara == "cruz":
        valido = True
Azar = rd.randint(0,1) 
if Azar == 0 and cara == "cara":
    True
elif Azar == 1 and cara == "cruz":
    True
elif Azar == 0 and cara == "cruz":
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
    exit()
elif Azar == 1 and cara == "cara":
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
    exit()  
    
Lista = ["Adrian", "Sergio", "David" ,"Hector", "Santiago", "Jorge", "Diego", "Marco", "Rojo", "Ginebra", "Izaro", "Nerea","Andrea"]
N = int(input("ingresa en cuanto quieres dividir la lista: "))
rd.shuffle(Lista)   
for i in range(0, len(Lista), N):
    print(Lista[i:i + N])