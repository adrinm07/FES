###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
print("Exercici 1")
for i in range(21):
    if i % 2 == 0 and i != 0:
        print(i)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
suma = 0
for i in numeros:
    suma += i
print(f"Exercici 2: {suma}")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
num_max = numeros[0]
for i in numeros:
    if i > num_max:
        num_max = i
print(f"Exercici 3: Num max = {num_max}")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
llista = []
for i in range(len(paraules)):
    if len(paraules[i]) >= 5:
        llista.append(paraules[i])
print(f"Exercici 4: Llista: {llista}")

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
count = 0
llista = []
lletra = input("Exercici 5: Introdueix una lletra: ")
for i in range(len(paraules)):
    if paraules[i][0] == lletra:
        llista.append(paraules[i])
print(f"Llista: {llista}")

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
suma = 0
longitud = len(tensions)
for i in range(len(tensions)):
    suma += tensions[i]
mitjana = suma/longitud
print(f"Exercici 6: Mitjana = {mitjana}")

# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
llista = []
tensio = 12
for i in range(len(resistencies)):
    llista.append(round(tensio/resistencies[i],2))
print(f"Exercici 7: Corrents: {llista}")

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
suma = 0
for i in range(len(nivells_soroll)):
    if nivells_soroll[i] > -80:
        suma += 1
print(f"Exercici 8: superen -80: {suma} soroll/s")

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
bits_diferents = 0
for i in range(len(bits_transmesos)):
    if bits_transmesos[i] != bits_rebuts[i]:
        bits_diferents += 1
taxa_error = bits_diferents/len(bits_rebuts)
print(f"Exercici 9: taxa = {taxa_error}")

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
print("Exercici 10")
for i in range(len(frequencies)):
    print(f"Periode {i+1} = {1/frequencies[i]}")