###
# EXERCICIS
# Fes servir, sempre que puguis, els mètodes que has après.
###

# Exercici 1: Afegir i modificar elements
# Crea una llista amb els nombres de l'1 al 5.
# Afegeix-hi el nombre 6 al final fent servir append().
# Insereix-hi el nombre 10 a la posició 2 fent servir insert().
# Modifica el primer element de la llista perquè sigui 0.
llista1 = [1,2,3,4,5]
print(f"Exercici 1: Llista original: {llista1}")
llista1.append(6)       # insereix una posició extra amb el contingut
llista1.insert(2,10)    # insereix el segon element (10 )a la posicio del primer (2),
                        # els demés numeros els mou a l'esquerra
llista1[0] = 0
print(f"Llista resultant: {llista1}")

# Exercici 2: Combinar i buidar llistes
# Crea dues llistes:
llista_a = [1, 2, 3]
llista_b = [4, 5, 6, 1, 2]
print(f"Exercici 2: Llista A original: {llista_a}, llista B original: {llista_b}")

# Amplia llista_a amb llista_b fent servir extend().
# Elimina la primera aparició del nombre 1 de llista_a fent servir remove().
# Elimina l'element de l'índex 3 de llista_a fent servir pop(). Imprimeix l'element eliminat.
# Buida completament llista_b fent servir clear().
llista_a.extend(llista_b)
llista_a.remove(1)      # Elimina la primera aparació del valor de la llista
pop = llista_a.pop(3)   # Elimina i retorna l'element del index indicat
llista_b.clear()
print(f"Llista A resultant: {llista_a}, llista B resultant: {llista_b}")

# Exercici 3: Slicing i eliminació amb del
# Crea una llista amb els nombres de l'1 al 10.
# Fes servir slicing i del per eliminar els elements des de l'índex 2 fins al 5
# (sense incloure el 5).
# Imprimeix la llista resultant.print(f"Llista A resultant: {llista_a}, llista B resultant: {llista_b}")
llista3 = [1,2,3,4,5,6,7,8,9,10]
print(f"Exercici 3: Llista original: {llista3}")
del llista3[2:5]
print(f"Llista resultant: {llista3}")

# Exercici 4: Ordenar i comptar
llista4 = [5, 2, 8, 1, 9, 4, 2]
print(f"Exercici4: Llista original: {llista4}")
# Ordena la llista de manera ascendent fent servir sort().
llista4.sort()
print(f"Llista resultant: {llista4}")
# Compta quantes vegades apareix el nombre 2 a la llista fent servir count().
counter2 = llista4.count(2)
print(f"Nombre de vegades que surt 2 a la llista: {counter2}")
# Comprova si el nombre 7 és a la llista fent servir in.
comprovar7 = 7 in llista4
print(f"7 surt en la llista?: {comprovar7}")

# Exercici 5: Còpia i referència
original = [1, 2, 3]
# Crea'n una còpia anomenada copia_1 fent servir slicing.
copia_1 = original[:]
# Crea'n una altra còpia anomenada copia_2 fent servir copy().
copia_2 = original.copy()
# Crea una referència a la llista original anomenada referencia.
referencia = original
# Modifica a 10 el primer element de la llista referencia.
referencia[0] = 10
# Imprimeix les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.
print(f"Exercici 5: original: {original}")
print(f"copia_1: {copia_1}")
print(f"copia_2: {copia_2}")
print(f"referencia: {referencia}")

# Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules
menjar = ["Poma", "pera", "PLÀTAN", "taronja"]
print(f"Exercici 6: Llista original: {menjar}")
# Ordena la llista sense distingir entre majúscules i minúscules.
menjar.sort()
print(f"Llista distinguint: {menjar}")

menjar.sort(key=str.lower)
print(f"Llista sense distinguir: {menjar}")
