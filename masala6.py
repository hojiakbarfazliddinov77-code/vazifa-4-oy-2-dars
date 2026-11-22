class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if self.baho >= 86:
            return "A'lo"
        elif self.baho >= 71:
            return "Yaxshi"
        elif self.baho >= 56:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"

talaba1 = Talaba('Ali', 20, 'TATU', 92)
talaba2 = Talaba('Malika', 19, 'NUUz', 64)
talaba3 = Talaba('Aziz', 21, 'WIUT', 45)

print(f"{talaba1.ism}: {talaba1.natija()}")
print(f"{talaba2.ism}: {talaba2.natija()}")
print(f"{talaba3.ism}: {talaba3.natija()}")