###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
print("Exercici 1")
def saludar_a(nom,salutacio="Hola"):
    print(f"{salutacio}, {nom}!")
saludar_a("Adri")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(num):
    if num % 2 == 0:
        return True
    else:
        return False
num_usuari = int(input("Exercici 2: Introdueix un num: "))
print(f"{num_usuari} es parell? {es_parell(num_usuari)}")

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    for i in numeros:
        suma += i
    mitja = suma / len(numeros)
    return mitja
llista = [1,2,3,4,5]
print(f"Exercici 3: Llista: {llista}, mitjana = {mitjana(llista)}")

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    suma = 0
    for i in args:
        suma += i
    print(suma)
print("Exercici 4")
sumar_tot(1,2)
sumar_tot(1,2,3,4,5)
sumar_tot(1,2,3,4,5,6,7,8,9,10)

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero,limit=10):
    print(f"Taula de multiplicar de {numero}")
    for i in range(1,limit+1):
        print(f"{numero}x{i} = {numero*i}")
num = int(input("Exercici 5: Posa un numero: "))
taula_multiplicar(num)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
print("Exercici 6")
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")
mostrar_perfil(nom = "Adri", edat = 19, grau = "Telecos")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(num):
    facto = 1
    for i in range(1,num+1):
        facto *= i
    print(facto)
num_facto = 2
factorial(num_facto)

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    vocals = 0
    text = text.lower()
    for x in text:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            vocals += 1
    print(vocals)
paraula = input("Exercici 8: Introdueix paraula: ")
comptar_vocals(paraula)

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def min_max(numeros):
    min = numeros[0]
    max = numeros[0]
    for i in numeros:
        if i < min:
            min = i
        elif i > max:
            max = i
    resultat = [min,max]
    return resultat
r_minmax = min_max([1,-4,3,10])
r_min = r_minmax[0]
r_max = r_minmax[1]
print(f"Exercici 9: Min = {r_min}, Max = {r_max}")

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
    text = text.lower()
    comprovar = True
    for i in range(0,len(text)):
        if text[i] != text[len(text)-i-1]:
            comprovar = False
    if comprovar == False:
        return False
    else:
        return True
paraula2 = input("Exercici 10: Introdueix un text: ")
print(f"{paraula2} es palindrom? {es_palindrom(paraula2)}")
