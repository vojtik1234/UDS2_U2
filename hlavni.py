# Komentar
# Bod1

def pridej_cisla(a, b):
    """
    Dokumentacni retezec funkce pridej_cisla
    Funkce provede scitani dvou cisel

    :param a: Prvni cislo
    :param b: Druhe cislo
    :return: Soucet císel a a b
    """
    return a + b

# Bod2

jmeno = "Pepik"
vek = 30
print("Jmeno:", jmeno, "- Vek:", vek)

# Bod3

muj_list = [1, 2, 3, 4, 5]
muj_slovnik = {"jablko": 3, "banan": 2, "rajce": 5}

# Bod4

if vek >= 18:
    print("18 a vice")
else:
    print("17 a mene")

# Bod5

for cislo in muj_list:
    if cislo % 2 == 0:
        print(cislo, "je sude cislo")
    else:
        print(cislo, "je liche cislo")

# Bod6

muj_string = "Zdar, svete!"
slicing_string = muj_string[6:]
print(slicing_string)  # Rozsekne a vypise "svete!"

# Bod7

def pozdrav(jmeno="Host"):
    print("Zdur,", jmeno)

pozdrav()           # Vypise "Zdur, Host"
pozdrav("Pepik")    # Vypise "Zdur, Pepik"

# Bod8

def dostan_info():
    return 25, "Honzik"

vek, jmeno = dostan_info()

# Bod9

length = len(muj_list)

# Bod10

import math

odmocnina = math.sqrt(16)

# Bod11

# Instalace knihovny: pip install numpy
import numpy as np

random_cisla = np.random.randint(1, 10, 5)

# Bod12

from druhy_soubor import odmocnina

result = odmocnina(4)  # Vysledek: 16











