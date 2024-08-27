class PastaModel:
    def __init__(self):
        self.pastas = []

    def get_pastas(self):
        return self.pastas

    def add_pasta(self, title, composition: list, price, weight):
        data = {f'{title}': {'composition': composition,
                             'price': price,
                             'weight': weight}}
        self.pastas.append(data)

    def change_composition(self, title, new_composition: list):
        for pasta in self.pastas:
            for key, value in pasta.items():
                if key == title:
                    value['composition'] = new_composition


my_pasta = PastaModel()
my_pasta.add_pasta('Карбонара',
                   ["спагетти", "яйцо куриное", "бекон", "чеснок", "петрушка", "орегано", "сыр Пармезан (крошка)"],
                   200, 500)
my_pasta.add_pasta('Лазанья болоньезе',
                   ["листы лазаньи", "фарш из говядины и свинины", "томаты в собственном соку",
                    "паста томатная", "лук репчатый"],
                   100, 450)
my_pasta.add_pasta('Фетучини Альфредо',
                   ["гнёзда фетучини", "сёмга филе на коже", "сливки 30%", "масло сливочное",
                    "сыр Пармезан молодой"],
                   150, 300)

my_pasta.change_composition('Лазанья болоньезе', ["спагетти", "яйцо куриное"])
print(my_pasta.get_pastas())
