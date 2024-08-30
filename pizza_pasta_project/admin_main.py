from Pizza.Change_Pizza import ChangePizza
from Pasta.Change_Pasta import ChangePasta

pizza_changer = ChangePizza('Грибная')
print(pizza_changer.set_new_cost_price('Грибная', 200))
print(pizza_changer.set_new_sale_price('Грибная', 300))
print(pizza_changer.set_ingredients('Грибная', "чесночный соус", "колбаса", "шампиньоны", "сыр моцарелла", "базилик"))
print(pizza_changer.add_to_menu('Грибная'))
removed_data, new_menu = ChangePizza.remove_from_menu('Грибная')
print(removed_data)
print(new_menu)
print(ChangePizza.remove_from_menu('Грибная'))

# pizza_changer = ChangePizza('Лесная')
# print(pizza_changer.set_new_cost_price('Лесная', 400))
# print(pizza_changer.set_new_sale_price('Лесная', 600))
# print(pizza_changer.set_ingredients('Лесная', "луковый соус", "шишки", "грибы", "ягоды", "базилик"))
# print(pizza_changer.add_to_menu('Лесная'))

pasta_changer = ChangePasta('Мак энд чиз')
print(pasta_changer.set_new_cost_price('Мак энд чиз', 150))
print(pasta_changer.set_new_sale_price('Мак энд чиз', 200))
print(pasta_changer.set_ingredients('Мак энд чиз', "сыр Манчестер", "сыр Чеддер", "макароны из кукурузной муки",
                                    "сливки 10%", "масло сливочное"))
print(pasta_changer.add_to_menu('Мак энд чиз'))
removed_data, new_menu = ChangePasta.remove_from_menu('Мак энд чиз')
print(removed_data)
print(new_menu)
print(ChangePasta.remove_from_menu('Мак энд чиз'))
