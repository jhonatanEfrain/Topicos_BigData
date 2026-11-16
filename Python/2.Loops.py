print("Estructuras repetitivas en Python")

# for
for i in range(1, 10):
    print(i)
for letra in ("hola mundo"):
    print(letra)
# while
contador = 1
while contador <= 3:
    print(f'intento: {contador}')
    contador += 1#contador = contador + 1
# Do while

while True:
    numero = int (input("Ingrese un numero > 0 : "))
    if numero > 0:
        break

