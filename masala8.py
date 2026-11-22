class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        if filmlar is None:
            filmlar = []
        self.filmlar = filmlar

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, indeks):
        return self.filmlar[indeks]

    def __contains__(self, film):
        return film in self.filmlar

kutubxona = FilmKutubxonasi('Mening filmlarim', ['Avatar', 'Titanic', 'Interstellar'])

print(len(kutubxona))
print(kutubxona[0])
print(kutubxona[2])
print('Titanic' in kutubxona)
print('Joker' in kutubxona)

for film in kutubxona:
    print(film)