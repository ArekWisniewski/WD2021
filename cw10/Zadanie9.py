# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego sprzedawcy i wyświetl wykres
# kołowy z procentowym udziałem każdego sprzedawcy
# w ogólnej sumie zamówień. Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut
# ‘explode’ tego wykresu. Przetestuj ten atrybut na wykresie.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

odczyt = pd.read_csv("zamowienia.csv", header=0, delimiter=";")
grupa = odczyt.groupby(['Sprzedawca']).agg({"idZamowienia": ['count']})
sprzedawcy = grupa.index.values
zamowienia = [grupa.values[y][0] for y in range(len(grupa.values))]
Explode = (0, 0.1, 0, 0, 0, 0, 0.2, 0, 0)


def prepare_label(pct, zam):
    absolute = int(np.ceil(pct / 100. * np.sum(zam)))
    return "{:.1f}% \n({}/{})".format(pct, absolute, sum(zamowienia))


wedges, texts, autotexts = plt.pie(zamowienia, explode=Explode, shadow=True, labels=sprzedawcy,
                                   autopct=lambda pct: prepare_label(pct, zamowienia), textprops=dict(color="black"))
plt.setp(autotexts, size=8, weight="bold")
plt.legend(title='Sprzedawcy')
plt.show()