class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        print(f"Ism: {self.ism}\nMaosh: {self.maosh}")

class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        super().malumot()
        print(f"Fan: {self.fan}")

class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        super().malumot()
        print(f"Qavat: {self.qavat}")

oqituvchi1 = Oqituvchi('Malika', 5000000, 'Matematika')
oqituvchi2 = Oqituvchi('Aziz', 4500000, 'Informatika')
farrosh1 = Farrosh('Karim', 2500000, 2)
farrosh2 = Farrosh('Salima', 2500000, 3)

oqituvchi1.malumot()
oqituvchi2.malumot()
farrosh1.malumot()
farrosh2.malumot()