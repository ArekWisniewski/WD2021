# Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki


przedmiotjednostka = {'dysk': 'szt','sok': 'l','papier': 'opakowanie',}
jednostkaprzedmiot = {value: key for key, value in przedmiotjednostka.items()}
print('Słownik:')
print(przedmiotjednostka)
print('Słownik po zamianie miejsc:')
print(jednostkaprzedmiot)