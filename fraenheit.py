import random as rd
random_number = rd.randint(1,2)
print(random_number)

while True:
    Tempertatura = input("ingresa la unidad de temperatura a convertir (celsius/farenheit): ").lower()
    if Tempertatura == "celsius":
        celsius = float(input("ingresa la temperatura en celsius: "))
        farenheit = (celsius * 9/5) + 32
        print(f"La temperatura en farenheit es: {farenheit}")
        break
    
    elif Tempertatura == "farenheit":
        farenheit = float(input("ingresa la temperatura en farenheit: "))
        celsius = (farenheit - 32) * 5/9
        print(f"La temperatura en celsius es: {celsius}")
        break

    else:
        print("opcion no valida")

    
