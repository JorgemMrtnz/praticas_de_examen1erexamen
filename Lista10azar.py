import random as rd
import webbrowser
try:
    cara = int(input("Número del 1 al 10: "))
except ValueError:
    print("no entiendo escribe.")
Azar = rd.randint(1, 10)
if cara == Azar:
    Lista = ["Adrian", "Sergio", "David", "Hector", "Santiago", "Jorge", "Diego", "Marco", "Rojo", "Ginebra", "Izaro", "Nerea", "Andrea"]
    while True:
        try:
            N = int(input("Ingresa en cuánto quieres dividir la lista: "))
            rd.shuffle(Lista)   
            for i in range(0, len(Lista), N):
                print(Lista[i:i + N])
            break
        except ValueError:
            print("No entiendo, escribe un número válido.")
else:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
    exit()