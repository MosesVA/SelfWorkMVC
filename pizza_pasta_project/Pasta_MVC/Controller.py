class PastaController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_pastas():
            return self.model.get_pastas()
        else:
            return 'Нет данных!'

    def change_composition(self, title, new_composition: list, validation):
        if self.model.get_pastas():
            if validation in ['is_superuser', 'is_stuff']:
                self.model.change_composition(title, new_composition)
                return f'Состав в пасте {title} успешно изменен!'
            return 'Нет доступа!'
        else:
            return 'Нет данных!'

    def change_price(self, title, new_price, validation):
        if self.model.get_pastas():
            if validation in ['is_superuser', 'is_stuff']:
                self.model.change_price(title, new_price)
                return f'Цена пасты {title} успешно изменена!'
            return 'Нет доступа!'
        else:
            return 'Нет данных!'

    def change_weight(self, title, new_weight, validation):
        if self.model.get_pastas():
            if validation in ['is_superuser', 'is_stuff']:
                self.model.change_weight(title, new_weight)
                return f'Вес пасты {title} успешно изменен!'
            return 'Нет доступа!'
        else:
            return 'Нет данных!'

    def only_composition_weight_dict(self):
        compositions_weights = {}
        data = self.model.get_pastas()
        if data:
            for elem in data:
                for key, value in elem.items():
                    compositions_weights[value['weight']] = value['composition']
        else:
            return 'Нет данных!'
        return compositions_weights

    def only_prices_list(self):
        prices = []
        data = self.model.get_pastas()
        if data:
            for elem in data:
                for value in elem.values():
                    prices.append(value['price'])
        else:
            return 'Нет данных!'
        return prices

    def add_pasta(self, title, composition: list, price, weight, validation):
        if validation in ['is_superuser', 'is_stuff']:
            self.model.add_pasta(title, composition, price, weight)
            return 'Паста успешно добавлена!'
        else:
            return 'Нет доступа!'
