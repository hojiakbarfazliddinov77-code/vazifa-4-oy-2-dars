class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print(f"Nom: {self.nom}\nMuallif: {self.muallif}\nSahifa soni: {self.sahifa_soni}")

class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        super().malumot()
        print(f"Format: {self.format}\nFayl hajmi: {self.fayl_hajmi} MB")

kitob = Kitob('O\'tkan kunlar', 'Abdulla Qodiriy', 380)
elektron_kitob = ElektronKitob('Mehrobdan chayon', 'Abdulla Qodiriy', 320, 'pdf', 4.5)

kitob.malumot()
elektron_kitob.malumot()