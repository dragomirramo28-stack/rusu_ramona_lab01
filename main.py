def citeste_sir():
    print("--- 1. Citire șir de numere ---")
    text_introdus = input("Introduceți numerele separate prin spațiu: ")
    sir_numere = [int(x) for x in text_introdus.split()]
    return sir_numere


def citeste_matrice():
    print("\n--- 2. Citire matrice de numere ---")
    linii = int(input("Introduceți numărul de linii: "))
    coloane = int(input("Introduceți numărul de coloane: "))
    
    matrice = []
    print(f"Introduceți elementele pentru fiecare linie (câte {coloane} numere pe linie, separate prin spațiu):")
    
    for i in range(linii):
        linie_text = input(f"Linia {i + 1}: ")
        linie_numere = [int(x) for x in linie_text.split()]
        
        while len(linie_numere) != coloane:
            print(f"Eroare! Trebuie să introduceți exact {coloane} numere.")
            linie_text = input(f"Linia {i + 1} din nou: ")
            linie_numere = [int(x) for x in linie_text.split()]
            
        matrice.append(linie_numere)
        
    return matrice


def afiseaza_date(sir, matrice):
    print("\n================ REZULTATE ================")
    print("Șirul citit este:", sir)
    
    print("\nMatricea citită este:")
    for linie in matrice:
        print("  ".join(str(elem) for elem in linie))


if __name__ == "__main__":
    sir = citeste_sir()
    matrice = citeste_matrice()
    afiseaza_date(sir, matrice)