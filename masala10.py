class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Savat:
    def __init__(self, nom, mahsulotlar=None):
        self.nom = nom
        if mahsulotlar is None:
            mahsulotlar = []
        self.mahsulotlar = mahsulotlar

    def mahsulot_qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(mahsulot.narx for mahsulot in self.mahsulotlar)

    def __str__(self):
        return f"Savat: {self.nom}, mahsulotlar soni: {len(self)}"

savat1 = Savat('Ali savati')
savat1.mahsulot_qoshish(Mahsulot('Non', 5000))
savat1.mahsulot_qoshish(Mahsulot('Sut', 12000))
savat1.mahsulot_qoshish(Mahsulot('Tuxum', 18000))

savat2 = Savat('Bo\'sh savat')

print(savat1)
if savat1:
    print(f"Umumiy narx: {savat1.umumiy_narx()} so‘m")

print(savat2)
if savat2:
    print(f"Umumiy narx: {savat2.umumiy_narx()} so‘m")
else:
    print("Savat bo'sh")