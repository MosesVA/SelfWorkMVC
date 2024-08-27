class PastaView:
    def __init__(self, controller):
        self.controller = controller

    def print_default_action(self):
        pastas = self.controller.default_action()
        if pastas == 'Нет данных!':
            print('Нет данных!')
        else:
            for pasta in pastas:
                for key, value in pasta.items():
                    print(f'''Паста - {key}
Состав: {", ".join(value["composition"])}
Цена: {value["price"]}
Вес: {value["weight"]}''')
                    print()

    def change_composition(self, title, new_composition: list, validation='user'):
        print(self.controller.change_composition(title, new_composition, validation))

    def change_price(self, title, new_price, validation='user'):
        print(self.controller.change_price(title, new_price, validation))

    def change_weight(self, title, new_weight, validation='user'):
        print(self.controller.change_weight(title, new_weight, validation))

    def print_composition_weight(self):
        titles_genres = self.controller.only_composition_weight_dict()
        if titles_genres == 'Нет данных!':
            print('Нет данных!')
        else:
            for key, value in titles_genres.items():
                print(f'Вес - {key}, Состав - {", ".join(value)}')

    def print_prices(self):
        prices = self.controller.only_prices_list()
        if prices == 'Нет данных!':
            print('Нет данных!')
        else:
            print(', '.join([str(i) for i in prices]))
            print()

    def add_pasta(self, title, composition: list, price, weight, validation='user'):
        print(self.controller.add_pasta(title, composition, price, weight, validation))
