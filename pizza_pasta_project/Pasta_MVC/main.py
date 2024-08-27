from PastaModel import PastaModel
from View import PastaView
from Controller import PastaController

model = PastaModel()
controller = PastaController(model)
view = PastaView(controller)

view.print_default_action()
view.print_composition_weight()
view.print_prices()

print()

view.add_pasta('Карбонара',
               ['спагетти', 'яйцо куриное', 'бекон', 'чеснок', 'петрушка', 'орегано', 'сыр Пармезан (крошка)'],
               200, 500)
view.add_pasta('Лазанья болоньезе',
               ['листы лазаньи', 'фарш из говядины и свинины', 'томаты в собственном соку',
                'паста томатная', 'лук репчатый'],
               100, 450, 'is_superuser')
view.add_pasta('Фетучини Альфредо',
               ['гнёзда фетучини', 'сёмга филе на коже', 'сливки 30%', 'масло сливочное',
                'сыр Пармезан молодой'],
               150, 300, 'is_stuff')

print()

view.print_default_action()
view.print_composition_weight()
view.print_prices()

print()

view.change_composition('Лазанья болоньезе', ['листы лазаньи', 'фарш из говядины и свинины'], 'is_stuff')
view.change_price('Лазанья болоньезе', 400, 'is_stuff')
view.change_weight('Лазанья болоньезе', 600, 'is_stuff')
print()
view.print_default_action()
