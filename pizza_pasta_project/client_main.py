from Pizza.pizza_creator import PizzaCreator, CreateMenuPizza, CreateOwnPizza
from Pasta.pasta_creator import PastaCreator, CreateMenuPasta, CreateOwnPasta


def client_code_pizza(creator: PizzaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pizza(order))
    print(creator.bake_pizza(order))
    print(creator.save_order_to_json(order))


def client_code_pasta(creator: PastaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pasta(order))
    print(creator.cooking_pasta(order))
    print(creator.save_order_to_json(order))


if __name__ == "__main__":
    menu_pizza = ["Гавайская", "Грибная", "Сырный цыпленок", "Пепперони", "Тунец - тысяча островов"]
    menu_pasta = ["Карбонара", "Лазанья болоньезе", "Фетучини Альфредо"]
    pizza_or_pasta = input("Что будете кушать (Пицца/Паста): ")
    user_order = input("Введите ваш заказ: ")

    if pizza_or_pasta == 'Пицца':
        if user_order in menu_pizza:
            client_code_pizza(CreateMenuPizza(), user_order)
        else:
            client_code_pizza(CreateOwnPizza(), user_order)
    elif pizza_or_pasta == 'Паста':
        if user_order in menu_pasta:
            client_code_pasta(CreateMenuPasta(), user_order)
        else:
            client_code_pasta(CreateOwnPasta(), user_order)
    else:
        print('Такого в нашем ресторане нет.')
