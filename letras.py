numeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"]
numero = int(input("Introduce un número: "))
if numero >= 0 and numero <= 10:
    print(numeros[numero])
else:
    print("El número no está entre 0 y 10")
