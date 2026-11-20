###
# EXERCICIS (range)
###

# Exercici 1: Imprimir números de l'1 al 10
# Imprimeix els números de l'1 al 10 (inclosos) fent servir un bucle for i range().
print("Exercici 1")
for i in range(1,11):
    print(i)

# Exercici 2: Imprimir números senars de l'1 al 20
# Imprimeix tots els números senars entre 1 i 20 (inclosos) fent servir un bucle for i range().
print("Exercici 2")
for i in range(1,20):
    if i % 2 != 0:
        print(i)

# Exercici 3: Imprimir múltiples de 5
# Imprimeix els múltiples de 5 des del 5 fins al 50 (inclosos) fent servir un bucle for i range().
print("Exercici 3")
for i in range(5,51):
    if i % 5 == 0:
        print(i)

# Exercici 4: Imprimir números en ordre invers
# Imprimeix els números del 10 a l'1 (inclosos) en ordre invers fent servir un bucle for i range().
print("Exercici 4")
for i in range(1,11):
    print(11-i)

# Exercici 5: Suma de números en un rang
# Calcula la suma dels números de l'1 al 100 (inclosos) fent servir un bucle for i range().
suma = 0
for i in range(1,101):
    suma += i
print(f"Exercici 5: suma = {suma}")

# Exercici 6: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle for i range().
num = int(input("Exercici 6: Introdueix un numero: "))
print(f"TAULA DE MULTIPLICAR DE {num}")
for i in range(1,11):
    print(f"{num}x{i} = {num*i}")