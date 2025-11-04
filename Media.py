import numpy as np
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
mean = np.mean([a, b, c])
print(f"La media de los números {a}, {b} y {c} es: {mean}")