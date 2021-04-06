# Przeciąż metodę __add__() dla klasy Kwadrat, która będzie zwracała instancje klasy Kwadrat o nowym boku,
# będącym sumą boków dodawanych do siebie kwadratów.
class Kwadrat():

    def __init__(self, x):
        self.x = x

    def __add__(self, kwadrat):
        return Kwadrat(self.x + kwadrat.x)

    def __str__(self):
        return f"Kwadrat x={self.x}"


k1 = Kwadrat(6)
k2 = Kwadrat(3)
k3 = k1 + k2
print(k3)