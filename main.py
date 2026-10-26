import os


def citeste_sir():
    print("1. Citire șir de numere de la tastatură")
    text = input("Introduceți numerele separate prin spațiu: ")
    
    sir = []
    for x in text.split():
        sir.append(int(x))
        
    return sir


def citeste_matrice():
    print("\n2. Citire matrice de numere")
    linii = int(input("Introduceți numărul de linii: "))
    coloane = int(input("Introduceți numărul de coloane: "))
    
    matrice = []
    print("Introduceți elementele pentru fiecare linie (câte", coloane, "numere pe linie, separate prin spațiu):")
    
    for i in range(linii):
        linie_text = input("Linia " + str(i + 1) + ": ")
        
        linie = []
        for x in linie_text.split():
            linie.append(int(x))
            
        matrice.append(linie)
        
    return matrice


def citeste_sir_din_fisier():
    print("\n3. Citire șir de numere din fișier")
    nume_fisier = input("Introduceți numele fișierului (ex: date.txt): ")
    
    # Verificăm dacă fișierul există pe calculator
    if not os.path.exists(nume_fisier):
        print("Eroare: Fișierul nu există!")
        return []
        
    # Deschidem fișierul în modul citire ("r" de la read)
    with open(nume_fisier, "r") as f:
        continut = f.read()
        
    sir = []
    for x in continut.split():
        sir.append(int(x))
        
    return sir


def afiseaza_date(sir, matrice, sir_fisier):
    print("\n================ REZULTATE ================")
    print("Șirul citit de la tastatură este:", sir)
    print("Matricea citită este:", matrice)
    print("Șirul citit din fișier este:", sir_fisier)


if __name__ == "__main__":
    sir = citeste_sir()
    matrice = citeste_matrice()
    sir_fisier = citeste_sir_din_fisier()
    afiseaza_date(sir, matrice, sir_fisier)