#!/usr/bin/env python3
# Вариант 11
# Известна стоимость 1 кг конфет, печенья и яблок. Найти стоимость всей покупки, если купили x кг конфет, у кг печенья и кг яблок.
candy_price, cookie_price, apple_price = (int(input("Введите стоимость конфет за кг: ")),
                                          int(input("Введите стоимость печенья за кг: ")),
                                          int(input("Введите стоимость яблок за кг: ")))
candy, cookie, apple = int(input("Введите вес купленных конфет: ")), int(
    input("Введите вес купленного печенья: ")), int(input("Введите вес купленных яблок: "))
print(f"Стоимость всей покупки = {candy_price * candy + cookie_price * cookie + apple_price * apple}")