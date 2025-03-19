#!/usr/bin/env python3

class Hero:
    """Базовый класс, представляющий Героя.
       Он может создавать других персонажей.
    """

    def __init__(self, name: str) -> None:
        """
        Инициализация Героя с именем.

        Аргументы:
            name (str): Имя Героя.
        """
        self.name = name

    def summon_warrior(self) -> 'Warrior':
        """
        Создать Воина, подкласс Героя.

        Возвращает:
            Warrior: Экземпляр класса Воин.
        """
        return Warrior(input("Имя рыцаря: "), strength=100)

    def summon_magician(self) -> 'Magician':
        """
        Создать Мага, подкласс Героя.

        Возвращает:
            Magician: Экземпляр класса Маг.
        """
        return Magician(input("Имя мага: "), mana=200)


class Warrior(Hero):
    """Подкласс Героя, представляющий Воина с повышенной силой."""

    def __init__(self, name: str, strength: int) -> None:
        """
        Инициализация Воина с именем и уровнем силы.

        Аргументы:
            name (str): Имя Воина.
            strength (int): Уровень силы Воина.
        """
        super().__init__(name)
        self.strength = strength

    def swing_sword(self) -> None:
        """
        Выполнить атаку мечом, используя силу Воина.
        """
        print(f"{self.name} наносит удар мечом с силой {self.strength}!")


class Magician(Hero):
    """Подкласс Героя, представляющий Мага с магическими способностями."""

    def __init__(self, name: str, mana: int) -> None:
        """
        Инициализация Мага с именем и уровнем маны.

        Аргументы:
            name (str): Имя Мага.
            mana (int): Уровень маны Мага.
        """
        super().__init__(name)
        self.mana = mana

    def cast_fireball(self) -> None:
        """
        Создать огненный шар, используя ману Мага.
        """
        print(f"{self.name} бросает огненный шар, используя {self.mana} маны!")


if __name__ == "__main__":

    # Пример использования
    merlin = Hero("Мерлин")
    arthur = merlin.summon_warrior()
    gandalf = merlin.summon_magician()

    arthur.swing_sword()  # <Рыцарь> наносит удар мечом с силой 100!"
    gandalf.cast_fireball()  # <Маг> бросает огненный шар, используя 200 маны!"
