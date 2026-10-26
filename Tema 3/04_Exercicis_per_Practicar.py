# ==========================================
# EXERCICIS DE PROGRAMACIÓ EN PYTHON: REPTES DE LLISTES
# Enunciats basats en problemes realistes.
# Resol cada exercici pensant quina és la millor eina o mètode de Python a utilitzar.
# ==========================================

# Exercici 1: Gestió de l'inventari d'un magatzem
# Tens la següent llista de productes al magatzem: ["ordinador", "ratolí", "teclat"].
# Han arribat dos productes nous: "pantalla" i "altaveus".
# Col·loca la "pantalla" a la primera posició de la llista i els "altaveus" al final de tot.
# A més, el segon producte ("ratolí") s'ha esgotat i s'ha de substituir per "ratolí sense fils".

llista1 = ["ordinador", "ratolí", "teclat"]
print(f"Exercici 1: llista original: {llista1}")
llista1.insert(0,"pantalla")
llista1.append("altaveus")
i = 0
while i < len(llista1):
    if llista1[i] == "ratolí":
        llista1[i] = "ratolí sense fils"
        break
    i += 1
print(f"Llista resultant: {llista1}\n")

# Exercici 2: Control d'assistència a un esdeveniment
# Es tenen dues llistes de confirmats de dos grups diferents:
grup_a = ["Anna", "Marc", "Laia"]
grup_b = ["Jordi", "Anna", "Pau"]
print(f"Exercici 2: llista a: {grup_a} / llista b: {grup_b}")
# Unifica tots els assistents en la llista del 'grup_a'.
# Esborra la primera vegada que apareix "Anna" perquè no estigui duplicada.
# L'última persona de la llista unificada decideix marxar d'urgència; extreu-la i guarda el seu nom en una variable.
# Assegura't que la llista del 'grup_b' quedi totalment buida.

grup_a += grup_b
grup_a.remove("Anna")
nom = grup_a[len(grup_a)-1]
grup_a.pop()
grup_b.clear()
print(f"Llistes resultants: llista a: {grup_a} / llista b: {grup_b}\n")

# Exercici 3: Neteja de dades d'un sensor
# Un sensor ha enregistrat les següents lectures de temperatura consecutives:
sensor = [15, 16, 99, 102, 98, 17, 18, 19]
print(f"Exercici 3: Llista original: {sensor}")
# Les lectures de l'índex 2 fins a l'índex 4 (ambdós inclosos) corresponen a picos d'error.
# Elimina exactament aquest tram d'elements defectuosos i mostra com queda la llista filtrada.

i = 0
while i < len(sensor):
    if sensor[i] > 90:
        sensor.pop(i)
        i += -1
    i+=1
print(f"Llista resultant: {sensor}\n")

# Exercici 4: Classificació de puntuacions d'un joc
# Un jugador ha obtingut les següents puntuacions en diverses partides:
puntuacions = [45, 12, 88, 45, 100, 23, 45]
print(f"Exercici 4: Puntuacions originals: {puntuacions}")
# Reorganitza les puntuacions de menor a major.
# Esbrina quantes vegades ha aconseguit el jugador la seva puntuació de 45 punts.
# Comprova si el jugador ha obtingut alguna vegada exactament 50 punts i mostra un resultat booleà (True/False).

puntuacions.sort()
p45= puntuacions.count(45)
i=0
while i < len(puntuacions):
    if puntuacions[i] == 50:
        p50 = True
        break
    i+=1
else:
    p50 = False
print(f"Vegades puntuació = 45: {p45}, ha obtingut puntuacio = 50? {p50}\n")

# Exercici 5: Sincronització de llistes de tasques
# Tens una llista original de tasques:
tasques = ["estudiar", "comprar", "netejar"]
# Crea dues còpies que siguin completament independents entre si i respecte a l'original.
# Crea també un àlies o enllaç directe a la llista original.
# Si modifiques la primera tasca a través de l'àlies per "FEINA FETA", mostra quines llistes han canviat i quines mantenen els valors originals intactes.

copia1 = tasques[:]
copia2 = tasques.copy()
enllaç = tasques

# Exercici 6: Resum d'un text d'etiquetes
# Es rep la següent cadena de text amb etiquetes separades per guions:
cadena = "python-django-flask-fastapi"
# Transforma aquesta cadena en una llista d'etiquetes individuals.
# Canvia la segona etiqueta a majúscules ("DJANGO").
# Torna a convertir la llista en una única cadena de text on les etiquetes estiguin separades per una coma i un espai (ex: "python, DJANGO, ...").

if "-" in cadena:
    llista = cadena.split("-")
    llista[1] = llista[1].upper()
    cadena_final = ", ".join(llista)
    print(f"Exercici 6: {cadena_final}\n")

# Exercici 7: Cerca i actualització en un catàleg
# Es té el següent catàleg de llibres:
llibres = ["El Quixot", "Tirant lo Blanc", "1984", "Odissea"]
print(f"Exercici 7: Original: {llibres}")
# Determina en quina posició exacta es troba l'obra "1984".
# Utilitzant aquesta posició obtinguda dinàmicament, reemplaça el títol per "1984 (Edició Especial)".

i = 0
while i < len(llibres):
    if llibres[i] == "1984":
        break
    i+=1
llibres[i] = "1984 (Edició Especial)"
print(f"Resultat: {llibres}\n")

# Exercici 8: Historial de navegació web
# Un usuari ha visitat les següents pàgines en ordre cronològic:
pagines= ["inici", "productes", "carrito", "pagament"]
print(f"Exercici 8: Original: {pagines}")
# Mostra la seqüència de navegació en ordre invers (des de la darrera pàgina fins a la primera) sense alterar la llista original.
# A continuació, inverteix l'ordre de la llista original de manera permanent.
i = 0
copia = pagines[:]
while i < len(pagines):
    copia[i] = pagines[-i-1]
    i+=1
print(f"Resultat: {copia}\n")

# Exercici 9: Reajust de promocions
# Una botiga té la següent llista de preus en euros:
preus2 = [10, 20, 30, 40, 50, 60]
print(f"Exercici 9: Original: {preus2}")
# Els preus situats entre la segona i la quarta posició (ambdues incloses) s'han de substituir per un únic valor promocional de [99].
# Mostra com es redueix la mida de la llista després d'aquesta substitució.
i = 2
j = 2
while i < 5:
    preus2.pop(j)
    i+=1
preus2.insert(2,99)
print(f"Resultat: {preus2}")


# Exercici 10: Estadístiques d'exàmens
# Un professor té les notes finals d'un grup d'alumnes: [4.5, 8.0, 9.5, 3.2, 6.7, 10.0, 5.5].
# Troba la nota més alta, la nota més baixa i la suma total de totes les notes.
# Calcula la mitjana exacta de la classe dividint la suma pel nombre total d'alumnes.

# Exercici 11: Sistema de torns d'espera (Cua d'atenció)
# Es té una cua de clients esperant ser atesos: ["Client_1", "Client_2", "Client_3", "Client_4"].
# Atén i retira de la llista el primer client que va arribar.
# A continuació, atén d'urgència i retira de la llista l'últim client que s'havia incorporat.
# Imprimeix els noms dels dos clients atesos i mostra quins clients romanen a la cua.

# Exercici 12: Tauler de joc en 2D (Matriu)
# Es té un tauler de joc representat per una graella de 3x3:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Obtingues el valor situat al centre mateix del tauler (el 5).
# Canvia el valor de l'última casella (el 9) per un 0 per indicar que està buida.
# Afegeix una nova línia completa a sota del tauler amb tres zeros: [0, 0, 0].

# Exercici 13: Depuració de registres d'usuaris
# Un sistema ha registrat identificadors d'usuari amb duplicats: [101, 203, 101, 505, 203, 404, 101].
# Processa aquesta llista per eliminar tots els identificadors repetits.
# Presenta la llista final d'identificadors únics ordenada de menor a major.

# Exercici 14: Ordenació alfabètica de noms
# Es té la següent llista de noms d'usuari: ["albert", "BEA", "carles", "ÀNGELS", "david"].
# Ordena la llista alfabèticament de la Z a la A sense que les diferències entre majúscules i minúscules afectin l'ordre correcte.

# Exercici 15: Generació de seqüències de senyal
# Es tenen dos patrons de senyal bàsics: patro_a = [1, 0] i patro_b = [9, 9].
# Genera una nova llista que repeteixi la seqüència del 'patro_a' 4 vegades segides.
# Genera una altra llista que sigui la fusió directa de 'patro_a' i 'patro_b'.