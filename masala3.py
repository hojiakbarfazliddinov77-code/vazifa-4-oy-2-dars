class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda")

class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda yurmoqda")

class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal aylantirib ketmoqda")

class Piyoda(Transport):
    def harakatlanish(self):
        print("Piyoda odam yurib ketmoqda")

transportlar = [Mashina(), Velosiped(), Piyoda()]

for transport in transportlar:
    transport.harakatlanish()