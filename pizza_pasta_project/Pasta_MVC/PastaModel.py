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

    def change_price(self, title, new_price: int):
        for pasta in self.pastas:
            for key, value in pasta.items():
                if key == title:
                    value['price'] = new_price

    def change_weight(self, title, new_weight: int):
        for pasta in self.pastas:
            for key, value in pasta.items():
                if key == title:
                    value['weight'] = new_weight
