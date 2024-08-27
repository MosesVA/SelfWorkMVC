from abc import ABC, abstractmethod


class PastaProduct(ABC):

    @abstractmethod
    def make_pasta(self, order):
        pass

    @abstractmethod
    def add_additional_ingredient(self):
        pass

    @abstractmethod
    def cooking_pasta(self, order):
        pass


class MenuPasta(PastaProduct):
    menu = {
        "Карбонара": [90, 130,
                      ["спагетти", "яйцо куриное", "бекон", "чеснок", "петрушка", "орегано", "сыр Пармезан (крошка)"]],
        "Лазанья болоньезе": [90, 140, ["листы лазаньи", "фарш из говядины и свинины", "томаты в собственном соку",
                                        "паста томатная", "лук репчатый"]],
        "Фетучини Альфредо": [110, 150, ["гнёзда фетучини", "сёмга филе на коже", "сливки 30%", "масло сливочное",
                                         "сыр Пармезан молодой"]],
    }
    additional_ingredients = []

    def make_pasta(self, order):
        if order in self.menu.keys() and self.additional_ingredients:
            return f"Формируем пасту {order} с составом:\n{', '.join(self.menu[order][2])}\nДополнительно: {', '.join(self.additional_ingredients)}"
        elif order in self.menu.keys():
            return f"Формируем пасту {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"

    def add_additional_ingredient(self):
        ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.additional_ingredients.append(ingredient)
            ingredient = input("Выберете дополнительный ингредиент или нажмите стоп: ")

    def cooking_pasta(self, order):
        if not self.additional_ingredients:
            return f"Готовим пасту {order} со стандартным составом:\n{', '.join(self.menu[order][2])}\n"
        else:
            return f"Готовим пасту {order} со дополнительными ингредиентами:\n{', '.join(self.additional_ingredients)}\n"


class OwnPasta(PastaProduct):
    ingredients = []

    def make_pasta(self, order):
        ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        while ingredient not in ['stop', 'end', 'стоп', 'конец', 'нет']:
            self.ingredients.append(ingredient)
            ingredient = input("Выберете желаемый ингредиент или нажмите стоп: ")
        print()
        return f"Формируем пасту {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}"

    def add_additional_ingredient(self):
        pass

    def cooking_pasta(self, order):
        own_pasta = {order: [150, 200, self.ingredients]}
        return f"Готовим пасту {order} с желаемыми ингредиентами:\n{', '.join(self.ingredients)}\n", own_pasta
