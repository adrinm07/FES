# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutats = ("Barcelona","València","Madrid","Sevilla","Oviedo")
print(f"Exercici 1: tupla ciutats: {ciutats}")
print(f"Penúltima ciutat: {ciutats[3]}")

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numeros = (1,2,6,5,2,3,5,4,3,8,6,4,6)
print(f"Exercici 2: tupla numeros: {numeros}")
print(f"Aparicions del 3: {numeros.count(3)}")

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla):
    return tuple(sorted(tupla))
tupla_ordenada = ordenar_tupla(numeros)
print(f"Exercici 3: tupla a ordenar: {numeros}")
print(f"Tupla ordenada: {tupla_ordenada}")
            