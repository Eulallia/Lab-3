
def Oblicz_pole_figur(nazwa): \

    nazwa = nazwa.lower()


    if nazwa == "prostokat":
        a = int(input("Podaj dlugosc prostokata: "))
        b = int(input("Podaj szerokosc prostokata: "))

        pole_prostokata = a * b
        print(f"Pole prostokata wynosi {pole_prostokata}.")

    elif nazwa == "trojkat":
        h = int(input("Podaj wysokosc trojkata: "))
        b = int(input("Podaj dlugosc podstawy trojkata: "))

    
        pole_trojkata = 0.5 * b * h
        print(f"Pole trojkata wynosi {pole_trojkata}.")
    
    elif nazwa == "kwadrat":
        s = int(input("Podaj dlugosc boku: "))


        pole_kwadratu = s * s
        print(f"Pole kwadratu wynosi {pole_kwadratu}. ")

    elif nazwa == "koło":
        r = int(input("Podaj promień koła: "))
        pi = 3.14

        kolo_pole = pi * r * r
        print(f"pole koła wynosi{kolo_pole}.")
	
    else:
        print("NIE MA TAKIEGO KSZTALTU!")


if __name__ == "__main__":
    nazwa_ksztaltu = input("Podaj nazwe figury gemetrycznej dla ktorej chcezs obliczyc pole: ")


    Oblicz_pole_figur(nazwa_ksztaltu)
	
#Projekt Stworzyli:
# Kinga Rolczak
# Jakub Guguł
# Kamil Kałamarz
# Maja Kuźniak
