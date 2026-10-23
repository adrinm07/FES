###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
nivell = float(input("Exercici 1: Introdueix el nivell de senyal Wi-Fi (RSSI) en dBm: "))
if nivell >= -50:
    print("Cobertura excel·lent")
elif -67 <= nivell < -50:
    print("Cobertura bona")
elif -75 <= nivell < -67:
    print("Cobertura feble")
else:
    print("Cobertura molt feble")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia = float(input("Exercici 2: Introdueix la potència òptica rebuda en dBm: "))
if -27 <= potencia <= -8:
    print("Nivell de recepció acceptable")
elif potencia < -27:
    print("Nivell de recepció massa baix")
else:
    print("Nivell de recepció massa alt")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Exercici 3: Introdueix el consum de dades mòbils en GB: "))
if consum <= 20:
    print("Consum dins del límit")
else:
    print(f"Consum fora del límit. Has consumit {consum - 20} GB addicionals.")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
los = int(input("Exercici 4: L'indicador LOS està encès? (1/0): "))
internet = int(input("L'indicador d'Internet està encès? (1/0): "))
if internet == 0:
    print("Revisa el cable de fibra")
elif los == 0:
    print("Comprova el servei del proveïdor")
else:
    print("La connexió sembla funcionar correctament")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
sai = int(input("Exercici 5: Posa el percentatge de bateria disponible al SAI: "))
if 0 <= sai < 20:
    print("Nivell crític")
elif 20 <= sai <= 49:
    print("Nivell baix")
elif 50 <= sai <= 100:
    print("Nivell suficient")
else:
    print("Fora de rang")