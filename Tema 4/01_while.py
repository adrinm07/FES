###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
num = 10
print("Exercici 1")
while num > 0:
    print(num)
    num -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
i = 1
suma = 0
while i <= 20:
    if(i % 2 == 0):
        suma += i
    i += 1
print(f"Exercici 2: suma = {suma}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
num3 = int(input("Exercici 3: Introdueix un enter positiu: "))
factorial = 1
while(num3 < 0):
    print("El numero no es positiu")
    num3 = int(input("Introdueix novament un enter positiu: "))
i = num3
while i > 0:
    factorial *= i
    i += -1
print(f"{num3}! = {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contraseña_user = input("Exercici 4: Introdueix contrasenya: ")

while len(contraseña_user) < 8:
    print("La contrasenya no compleix els requisits")
    contraseña_user = input("Introdueix novament contrasenya: ")
print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num5 = int(input("Exercici 5: Introdueix numero: "))
i = 1
print(f"TAULA DE MULTIPLICAR DEL {num5}")
while i <= 10:
    print(f"{num5}*{i} = {num5*i}")
    i += 1



# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

num = int(input("Exercici 6: Introdueix un enter positiu: "))
i = 2
while i <= num:
    primer = True
    j = 2
    while j*j <= i:
        if i % j == 0:
            primer = False
            break
        j += 1
    if primer == True:
        print(i)
    i += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

suma = 0
num = 1
print("Exercici 7:")
while num:
    num = int(input("Ves introduïnt nombres: "))
    if num == 0:
        break
    else:
        suma += num
print(f"Suma = {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

num = int(input("Exercici 8: Entra un num positiu: "))
xifres = 1
while True:
    if int(num / 10) == 0:
        break
    else:
        num = int(num / 10)
        xifres += 1
print(f"Xifres = {xifres}")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

num = int(input("Exercici 9: Introdueix quant nums de Fibo vols veure: "))
i = 2
fibo_Actual = 0
fibo = [0,1]
while i <= num:
    fibo_Actual = fibo[i-1] + fibo[i-2]
    fibo.append(fibo_Actual)
    i +=1
print(f"{num} nums de fibo: {fibo}")


# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

num_secret = 7
num = int(input("Exercici 9: Introdueix numero: "))

while num != num_secret:
    if num_secret < num:
        print("El numero secret és més petit")
    else:
        print("El numero secret és més gran")
    num = int(input("Introdueix numero: "))
print("L'has encertat!")