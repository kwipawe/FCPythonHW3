"""
Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile elementow chcesz wysłać, a następnie
wymaga podania wagi dla każdej z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:

Liczbę paczek wysłanych
Liczbę kilogramów wysłanych
Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

Restrykcje:

Waga elementów musi być z przedziału od 1 do 10 kg.
Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg, dodawanie paczek zostaje zakończone i wszystkie
paczki są wysłane. Wyświetlane jest podsumowanie.

Przykład 1:

Ilość elementów: 2
Wagi elementów: 7, 9
Podsumowanie:

Wysłano 1 paczkę (7+9)
Wysłano 16 kg
Suma pustych kilogramów: 4kg
Najwięcej pustych kilogramów ma paczka 1 (4kg)

Przykład 2:

 Ilość elementów: 6
Wagi elementów: 3, 6, 5, 8, 2, 3
Podsumowanie:

Wysłano 2 paczki (3+6+5, 8+2+3)
Wysłano 27 kg
Suma pustych kilogramów: 13kg
Najwięcej pustych kilogramów ma paczka 2 (7kg)

Przykład 3:
 Ilość elementów: 2

Wagi elementów: 7, 14
 Podsumowanie:
Wysłano 1 paczkę (7)
Wysłano 7 kg
Suma pustych kilogramów: 13kg
Najwięcej pustych kilogramów ma paczka 13
"""

# powitanko
print("Witaj w programie do obsługi ładowarki paczek 'Bezos 1.0'.")

# inicjalizacja zmiennych
MAX_WEIGHT = 20
elements_count = int(input("Ile elementów chcesz wysłać? "))
element_weight = 0
total_elements_weight = 0
parcel_count = 1
current_weight_in_parcel = 0
most_empty_parcel_nr = 1
most_waste_weight = 0
#petla pobierajaca wage elementow
for i in range(elements_count):
    element_weight = int(input(f"Podaj wagę elementu nr {i + 1} (Waga elementu musi wynosić między 1 a 10 kg): "))
    #koniec programu jesli element ma nieprawidlowa wage
    if element_weight > 10 or element_weight < 1:
        print(f"Nieprawidłowa waga elementu.")
        break
    #sprawdzenie czy element miesci sie w paczce
    if current_weight_in_parcel + element_weight > MAX_WEIGHT:
        print(f"\n Paczka nr {parcel_count} zapełniona: {current_weight_in_parcel} kg.\n")

        #sprawdzenie pustych kg
        if MAX_WEIGHT - current_weight_in_parcel > most_waste_weight:
            most_waste_weight = MAX_WEIGHT - current_weight_in_parcel
            most_empty_parcel_nr = parcel_count

        #tworzenie nowej paczki jesli element sie nie miesci
        parcel_count += 1
        current_weight_in_parcel = element_weight
        total_elements_weight += element_weight
    #dodawanie kolejnego elementu jesli sie miesci
    else:
        current_weight_in_parcel += element_weight
        total_elements_weight += element_weight
#komunikat przy zapelnieniu paczki
print(f"Paczka {parcel_count} zapełniona: {current_weight_in_parcel} kg.\n")

#sprawdzenie pustych kg w ostatniej paczce
if current_weight_in_parcel > most_waste_weight:
    most_waste_weight = MAX_WEIGHT - current_weight_in_parcel
    most_empty_parcel_nr = parcel_count


#wyswietlenie wynikow
print(f"Liczba elementow: {elements_count}.")
print(f"Liczba paczek: {parcel_count}.")
print(f"Łączna waga elementów wysłanych: {total_elements_weight} kg.")
print(f"Paczka z największą ilością pustych kilogramów: {most_empty_parcel_nr}: {most_waste_weight}.")