class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        return f"Karta egasi: {self.egasi}, balans: {self.balans} so‘m"

    def __gt__(self, other):
        return self.balans > other.balans

    def __lt__(self, other):
        return self.balans < other.balans

karta1 = Karta('Ali', '4321', 3000000)
karta2 = Karta('Malika', '8765', 5000000)

print(karta1)
print(karta2)

if karta1 > karta2:
    print(f"{karta1.egasi}ning kartasida mablag' ko'proq")
elif karta1 < karta2:
    print(f"{karta2.egasi}ning kartasida mablag' ko'proq")
else:
    print("Ikkala kartada mablag' teng")