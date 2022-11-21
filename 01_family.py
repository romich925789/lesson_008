# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 50
        self.dirt = 50
        self.coat = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьего корма осталось {}, грязи в доме {}, шуб теперь {}'.format(
            self.food, self.money, self.cat_food, self.dirt, self.coat)


class Cat:

    def __init__(self, name, house):
        self.fullness = 30
        self.name = name
        self.house = house

    def act(self):
        if self.fullness < 30:
            self.eat()
        else:
            i = randint(1, 4)
            if i == 1:
                self.sleep()
            else:
                self.soil()

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 5
        print("{} поел".format(self.name))

    def sleep(self):
        self.fullness -= 5
        print("{} поспал".format(self.name))

    def soil(self):
        self.fullness -= 5
        self.house.dirt -= 20
        print("{} драл обои".format(self.name))

    def __str__(self):
        return 'сытость кота {}'.format(self.fullness)


class Husband:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house
        self.sum = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        self.house.dirt += 5
        if self.fullness <= 30 and self.house.food >= 30:
            self.eat()
        else:
            i = randint(1, 4)
            if i < 3:
                self.work()
            elif i >= 3:
                self.gaming()

    def eat(self):
        if self.house.food >= 30:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        self.fullness -= 10
        self.house.money += 100
        self.sum += 100
        cprint('{} работал'.format(self.name), color='yellow')

    def gaming(self):
        self.fullness -= 10
        cprint('{} играл'.format(self.name), color='yellow')

    def __str__(self):
        return 'сытость мужа {}'.format(self.fullness)


class Wife:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 30 and self.house.food >= 30:
            self.eat()
        elif self.house.food < 30 and self.house.money > 30:
            self.shopping()
        elif self.house.dirt > 30:
            self.clean_house()
        elif self.house.money > 1100:
            self.buy_fur_coat()
        elif self.house.cat_food < 20:
            self.shopping_cat_food()
        else:
            self.do_nothing()

    def eat(self):
        if self.house.food >= 30:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
        else:
            cprint('{} не поела - нет еды'.format(self.name), color='red')

    def shopping(self):
        self.fullness -= 10
        self.house.food += 60
        self.house.money -= 20
        print('Жена сходила в магазин')

    def shopping_cat_food(self):
        self.fullness -= 10
        self.house.money -= 20
        self.house.cat_food += 30
        print('Жена сходила в магазин за кошачьим кормом')

    def buy_fur_coat(self):
        self.fullness -= 10
        self.house.coat += 1
        self.house.money -= 1000
        print('Жена купила шубу')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 30
        print('Жена убиралась дома')

    def do_nothing(self):
        self.fullness -= 10
        print("Жена нихуя не делала")

    def __str__(self):
        return 'сытость жены {}'.format(self.fullness)

    def mothing(self):
        print("gg")


# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
# vitya = Cat(name='Витёк', house=home)

# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     vitya.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')

# print("За год Серёжей заработано", serge.sum, "рублей")


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self, name, house):
#         self.fullness = 30
#         self.name = name
#         self.house = house
#
#     def act(self):
#         if self.fullness < 30:
#             self.eat()
#         else:
#             i = randint(1, 4)
#             if i == 1:
#                 self.sleep()
#             else:
#                 self.soil()
#
#     def eat(self):
#         self.fullness += 20
#         print("{} поел".format(self.name))
#
#     def sleep(self):
#         self.fullness -= 5
#         print("{} поспал".format(self.name))
#
#     def soil(self):
#         self.fullness -= 5
#         self.house.dirt -= 20
#         print("{} драл обои".format(self.name))


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 30 and self.house.food >= 30:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 30:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спал'.format(self.name), color='yellow')

    def __str__(self):
        return 'сытость ребёнка {}'.format(self.fullness)


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
