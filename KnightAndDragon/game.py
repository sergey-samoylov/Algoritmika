#!/usr/bin/env python3
from time import sleep

from hero import Hero

# Создаём героев
knight: Hero = Hero("Ричард", "меч", armor=25, health=50, power=20)
dragon: Hero = Hero("Смауг", "пламя", armor=25, health=100, power=10)
rascal: Hero = Hero('Питер', 'нож', armor=20, health=5, power=5)

def battle(attacker, defender) -> str:
    attacker, defender = attacker, defender

    while attacker.fights(defender):
        sleep(1)
        attacker, defender = defender, attacker

    # ✅ Выживает только один герой
    winner = attacker
    print(f"🏆 {winner.name} одержал победу! ")
    sleep(3)
    winner.heal()
    print(f"{winner.name} восстановил силы и стал опытнее. "
          f"Теперь сила его удара {winner.power}, "
          f"а класс брони {winner.armor}")

# История:
print("Средиземье в опасности! На помощь спешит доблестный рыцарь...")
print(knight)
sleep(5)
print(f"{knight.name} идёт по лесу. "
      f"Вдруг видит на пути мелкого воришку...")
print(rascal)
sleep(5)

if input('Сразиться? (да/нет) >>').lower() == 'да':
    battle(knight, rascal)

print(f"Наконец-то {knight.name} добрался до подземелья!")
print(f"Из темноты к нему с рёвом выполз дракон {dragon.name}...")
sleep(5)
print("Посмотрим на характеристики героев перед битвой:")
print(knight)
print(dragon)
sleep(5)

print(
    f"""
    🔥 Да начнётся смертельный бой: {knight.name} vs. {dragon.name}! 🔥
    """
)
battle(knight, dragon)

print("🎮 Игра окончена!")
