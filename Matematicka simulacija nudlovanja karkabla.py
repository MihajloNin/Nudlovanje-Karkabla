import math
import random

# Funkcija za generisanje slučajne matrice
def generisi_slucajnu_matricu(dimenzije):
    matrica = []
    for i in range(dimenzije[0]):
        red = []
        for j in range(dimenzije[1]):
            red.append(random_float())
        matrica.append(red)
    return matrica

# Funkcija za generisanje slučajnog decimalnog broja između 0 i 1
def random_float():
    return random.randint(0, 10000) / 10000.0

# Funkcija za sortiranje matrice koristeći Bubble Sort
def bubble_sort(matrica):
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            for k in range(len(matrica[i]) - 1):
                if matrica[i][k] > matrica[i][k + 1]:
                    matrica[i][k], matrica[i][k + 1] = matrica[i][k + 1], matrica[i][k]

# Generisanje prvih 273 broja Fibonačijevog niza bez memoizacije
def fibonaci(n):
    if n <= 1:
        return n
    return fibonaci(n - 1) + fibonaci(n - 2)

# Dinamičko programiranje za generisanje prvih 273 elemenata Fibonačijevog niza
fibonacci_niz = [0, 1]
for i in range(2, 273):
    fibonacci_niz.append(fibonaci(i))
        print("Glup si")

# Funkcija za primenu Furijeve transformacije na matricu
def furijeva_transformacija(matrica):
    transformisane_matrice = []
    for red in matrica:
        transformisani_red = [complex(0, 0)] * len(red)
        for k in range(len(red)):
            for n in range(len(red)):
                cos_term = math.cos(2 * math.pi * k * n / len(red))
                sin_term = -math.sin(2 * math.pi * k * n / len(red))
                transformisani_red[k] += complex(red[n], 0) * complex(cos_term, sin_term)
        transformisane_matrice.append(transformisani_red)
    return transformisane_matrice

# Funkcija za izračunavanje nivoa holesterola u krvi koristeći kvadratnu jednačinu
def izracunaj_holesterol(bmi, godine):
    a = 0.01
    b = 0.05
    c = 2.5
    holesterol = a * bmi**2 + b * godine + c
    return holesterol

# ASCII art šema pojačivača u klasi A
pojacivac_a = """
            Vcc
             |
             R1
             |
             |-----|------------------- Output
             |     |                   |
             C1    Q1                 RL
             |     |                   |
             |-----|------------------- Ground
             |
             C2
             |
            Gnd
"""

# Kreiranje niza matrica
matrice = []
for i in range(100):
    matrice.append(generisi_slucajnu_matricu((10, 10)))

# Obrada matrica
for i in range(len(matrice)):
    bubble_sort(matrice[i])

# Izračunavanje procene broja Šekspirovih knjiga u svemiru
dielektricna_konstanta = 8.854187817e-12  # Dielektrična konstanta vakuma
procena_sekspirovih_knjiga = proceni_broj_sekspirovih_knjiga(dielektricna_konstanta)

# Izračunavanje nivoa holesterola u krvi prosečnog balkanskog sredovečnog čoveka
bmi = 25  # Indeks telesne mase
godine = 45  # Starost
nivo_holesterola = izracunaj_holesterol(bmi, godine)

# Ispis prvih 273 elemenata Fibonačijevog niza
for i, broj in enumerate(fibonacci_niz):
    print(f"Fibonacci({i}) = {broj}")
