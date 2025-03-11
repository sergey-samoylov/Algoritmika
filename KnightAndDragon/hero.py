#!/usr/bin/env python3
from random import randint

class Hero:
    """Создаёт любого персонажа текстовой игры "Рыцарь vs. Дракон"."""
    def __init__(
        self,
        name: str,
        weapon: str,
        armor: int,
        health: int,
        power: int,
    ) -> None:
        """Присваивает герою имя и базовые свойства."""
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.health = health
        self.power = power

        self._armor = armor
        self._health = health

    def __repr__(self) -> str:
        """Показывает текущие данные героя."""
        return (f"""
        Поприветствуйте героя -> {self.name}
        Уровень здоровья: {self.health}
        Класс брони: {self.armor}
        Сила удара: {self.power}
        Оружие: {self.weapon}"""
        )

    def alive(self) -> bool:
        """Определяет, жив ли герой."""
        return self.health > 0

    def fights(self, other: "Hero") -> bool:
        """Герой наносит урон противнику, если оба живы."""

        roll_dice = randint(1, 6) # вносим элемент случайности в игру
        attack = self.power + roll_dice

        effective_attack = min(attack, other.armor)
        remaining_attack = attack - effective_attack

        other.armor = max(0, other.armor - attack)
        other.health = max(0, other.health - remaining_attack)

        print(f"⚔ -> УДАР! {self.name} атакует {other.name} "
              f"с силой {attack} используя {self.weapon}!")
        print(f"🛡 {other.name} покачнулся. "
              f"Класс брони упал до {other.armor}, "
              f"а уровень здоровья до {other.health}")

        # ✅ Если противник погиб, бой сразу же прерывается
        if not other.alive():
            print(f"💀 {other.name} пал в этом нелегком бою!")
            return False  # Сражение прервано

        return True  # Сражение продолжается

    def heal(self):
        self.armor = self._armor * 2
        self.health = self._health * 2
        self.power *= 2
