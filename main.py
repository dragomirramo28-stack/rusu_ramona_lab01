def citeste_sir():
    print("1. Citire șir de numere ")
    text = input("Introduceți numerele separate prin spațiu: ")
    
    sir = []
    for x in text.split():
        sir.append(int(x))
        
    return sir


def citeste_matrice():
    print("\n 2. Citire matrice de numere ")
    linii = int(input("Introduceți numărul de linii: "))
    coloane = int(input("Introduceți numărul de coloane: "))
    
    matrice = []
    print("Introduceți elementele pentru fiecare linie (câte", coloane, "numere pe linie, separate prin spațiu):")
    
    for i in range(linii):
        linie_text = input("Linia " + str(i + 1) + ": ")
        
        # Transformăm linia în numere
        linie = []
        for x in linie_text.split():
            linie.append(int(x))
            
        matrice.append(linie)
        
    return matrice


def afiseaza_date(sir, matrice):
    print("\n REZULTATE ")
    print("Șirul citit este:", sir)
    
    print("\nMatricea citită este:")
    for linie in matrice:
        print(linie)


if __name__ == "__main__":
    sir = citeste_sir()
    matrice = citeste_matrice()
    afiseaza_date(sir, matrice)