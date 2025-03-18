#!/usr/bin/env python3

from random import randint
from time import sleep


class Hero:
    """
    Базовый класс для всех героев.
    """

    def __init__(
        self,
        name: str,
        health: int,
        armor: int,
        power: int,
    ) -> None:
        # Инициализация атрибутов героя
        self.name = name.capitalize()
        self.health = health
        self.armor = armor
        self.power = power

    def __repr__(self) -> str:
        """
        Вывод информации о здоровье и броне героя.
        """
        return (f"\nГерой: {self.name}\n"
                f"Уровень здоровья: {self.health}\n"
                f"Класс брони: {self.armor}\n")
                
    def attack(self, enemy: "Hero") -> None:
        """
        Атака противника и нанесение урона -> сначала броне, затем здоровью.
        """
        enemy.armor -= self.power
        if enemy.armor < 0:
            # Урон проникает сквозь броню и наносится здоровью
            enemy.health += enemy.armor
            enemy.armor = 0
        print(f"{enemy.name} принимает удар."
              f"Теперь его броня: {enemy.armor}, "
              f"а уровень здоровья: {enemy.health}\n")

    def is_alive(self) -> bool:
        """
        Проверяет, жив ли герой (True — если здоровье больше 0).
        """
        return self.health > 0


class Warrior(Hero):
    """
    Класс Воин, наследует класс Hero.
    """

    def __init__(self, name: str) -> None:
        # Вызов конструктора родительского класса
        super().__init__(name, health=100, armor=50, power=15)

    def hello(self) -> None:
        print("\n-> НОВЫЙ ГЕРОЙ. Верхом на коне появился бравый воин.")
        print(self)
        sleep(2)

    def attack(self, enemy: Hero) -> None:
        print(f"-> УДАР! Храбрый воин {self.name} атакует соперника мечом!")
        super().attack(enemy)


class Magician(Hero):
    """
    Класс Маг, наследует класс Hero.
    """

    def __init__(self, name: str) -> None:
        # Вызов конструктора родительского класса
        super().__init__(name, health=50, armor=20, power=35)

    def hello(self) -> None:
        print("\n-> НОВЫЙ ГЕРОЙ. "
              "Откуда ни возьмись появился искусный волшебник.")
        print(self)

    def attack(self, enemy: Hero) -> None:
        print(f"\n-> УДАР! Ловкий маг {self.name} "
              f"накладывает заклинание на {enemy.name}")
        super().attack(enemy)
        sleep(2)

def create_hero() -> Hero:
    """
    Создаёт героев игры.
    """
    while True:
        name = input("Имя героя: ")
        if not name:
            print("Герою нужно придумать имя.")
            continue

        role = input("Воин или Маг: ").lower()
        if role == "воин":
            return Warrior(name)
        elif role == "маг":
            return Magician(name)
        else:
            print("Персонаж с такой ролью ещё не придуман. Попробуй снова.")
            sleep(2)

def battle(hero1: Hero, hero2: Hero) -> None:
    """
    Проводит бой между двумя героями до смерти одного из них.
    """
    print("\n== БИТВА НАЧИНАЕТСЯ! ==\n")

    # Случайным образом выбираем, кто будет атаковать первым
    num = randint(1, 2)
    if num == 2:
        hero1, hero2 = hero2, hero1

    while hero2.is_alive():
        hero1.attack(hero2)  # Герой 1 атакует
        if hero2.is_alive():
            hero1, hero2 = hero2, hero1  # Меняем порядок, если враг выжил

    # Объявляем победителя
    print(f"== {hero1.name} ПОБЕДИЛ! ==\n")



if __name__ == "__main__":
    first_hero = create_hero()
    second_hero = create_hero()

    first_hero.hello()
    second_hero.hello()

    battle(first_hero, second_hero)
