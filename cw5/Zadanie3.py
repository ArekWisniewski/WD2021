# Poczytaj o metodach __ge__, __gt__, __le__, __lt__,
# przeciąż je i spróbuj wykorzystać w instrukcji warunkowej do porównania dwóch instancji obiektów klasy Kwadrat.

class Kwadrat():

    def __init__(self, x):
        self.x = x

    def __ge__(self, kwadrat):
        if self.x >= kwadrat.x:
            return True
        else:
            return False

    def __gt__(self, kwadrat):
        if self.x > kwadrat.x:
            return True
        else:
            return False

    def __le__(self, kwadrat):
        if self.x <= kwadrat.x:
            return True
        else:
            return False

    def __lt__(self, kwadrat):
        if self.x < kwadrat.x:
            return True
        else:
            return False


k1 = Kwadrat(6)
k2 = Kwadrat(3)

if k1 >= k2:
    print("k1 >= k2")
if k1 > k2:
    print("k1 > k2")
if k1 < k2:
    print("k1 < k2")
if k1 <= k2:
    print("k1 <= k2")