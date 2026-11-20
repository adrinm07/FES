###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.
estudiant = {"nom" : "Adri",
             "edat" : 19,
             "assignatures" : ["FES","RiOG","CiCE"]}
print(f"Exercici 1: estudiant: {estudiant}")

# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.
print(f"Exercici 2: 2na asignatura actual: {estudiant['assignatures'][1]}")
estudiant['assignatures'][1] = "SiSD"
estudiant["edat"] = 20
print(f"2na asignatura nova: {estudiant['assignatures'][1]}, nova edat: {estudiant['edat']}")

# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.
estudiant_actu = {"grau" : "Telecos"}
estudiant.update(estudiant_actu)
del estudiant["edat"]
print(f"Exercici 3: Actualitzacio: {estudiant}")

# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print(f"Exercici 4: Existeix 'nom'?: {"nom" in estudiant}")
print(f"Existeix 'email'?: {"email" in estudiant}")

# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".
print("Exercici 5")
for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
comptador = {}
for i in paraules:
    repe = paraules.count(i)
    actu = {i : repe}
    comptador.update(actu)
    
print(f"Exercici 6: {comptador}")