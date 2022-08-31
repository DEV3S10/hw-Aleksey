from random import randint


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def hit(self, boss, heroes):
        pass

    def __str__(self):
        return f'{self.__name} health: {self.health}, damage: [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def hit(self, boss, heroes):
        for hero in heroes:
            if boss.health > 0 and hero.health > 0:
                hero.health = hero.health - boss.damage


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_ability(self, boss, heroes):
        pass

    def hit(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            boss.health = boss.health - self.damage


# -------------Персонажы-------------------------------------------------------------
class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_ability(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, "HEAL")
        self.__heal_points = heal_points

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health = hero.health + self.__heal_points


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage + 5


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REVENGE")

    def apply_super_ability(self, boss, heroes):
        if self.health - boss.damage:
            self.damage = self.damage + (boss.damage / 12)
        else:
            boss.damage = boss.damage


class Thor(Hero):
    def __init__(self, name, health, damage, stan=0):
        super().__init__(name, health, damage, "STAN")
        self.__stan = stan

    def apply_super_ability(self, boss, heroes):
        if self.health > 0 and round_number == 1:
            self.damage = self.__stan
        elif self.damage == self.__stan:
            boss.damage = 50
        else:
            boss.damage = 0


class Golem(Hero):
    def __init__(self, name, health, damage, protection=0):
        super().__init__(name, health, damage, "PROTECTION")
        self.__protection = protection

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                self.__protection = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.__protection
                else:
                    hero.health = hero.health - boss.damage


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SAVIOR")

    def apply_super_ability(self, boss, heroes):
        self.damage = 0
        for hero in heroes:
            if hero.health >= 0:
                self.health = hero.health
                self.health = 0
            else:
                self.health = 0


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "INVISIBLE")

    def apply_super_ability(self, boss, heroes):
        pass


class Druid(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HELLPER CALL")

    def apply_super_ability(self, boss, heroes):
        pass


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HACKER")

    def apply_super_ability(self, boss, heroes):
        rnd = randint(10, 30)
        for hero in heroes:
            boss.health - rnd
            hero.health + rnd


class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        super(TrickyBastard, self).__init__(name, health, damage, "PLAY DEAD")

    def apply_super_ability(self, boss, heroes):
        pass


class AntMan(Hero):
    def __init__(self, name, health, damage):
        super(AntMan, self).__init__(name, health, damage, "ANT MAN")

    def apply_super_ability(self, boss, heroes):
        pass


# ------------parameters for game-------------------------------------------------------------
round_number = 0


def print_statistics(boss, heroes):
    print(" ")
    print(f'{round_number} ROUND -----------------')
    print(boss)
    print("---------VS--------")
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print(">>>>>>>>><<<<<<<<<<")
        print("Heroes won!!!")
        print(">>>>>>>>><<<<<<<<<<")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print(">>>>>>>>><<<<<<<<<<")
        print("Boss won!!!")
        print(">>>>>>>>><<<<<<<<<<<")
    return all_heroes_dead


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(boss, heroes)
    for hero in heroes:
        hero.hit(boss, heroes)
        hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss("Lord", randint(700, 2000), 50)
    warrior = Warrior("Curry", randint(250, 300), 10)
    medic_1 = Medic("Doctor", randint(220, 240), 5, 15)
    magic = Magic("Samuel", randint(250, 300), 20)
    berserk = Berserk("Berserk", randint(250, 320), 25)
    thor = Thor("Chris", randint(230, 340), 20)
    golem = Golem("Golem", randint(500, 800), 2)
    witcher = Witcher("Witcher", randint(400, 500), 0)
    avrora = Avrora("Avrora", randint(230, 300), 15)
    hacker = Hacker("Hacker", randint(220, 300), 20)
    tricky = TrickyBastard("Tricky", randint(230, 3100), 15)
    antMan = AntMan("AntMan", randint(250, 350), 20)

    heroes = [warrior, medic_1, magic, berserk, thor, golem, witcher, avrora, hacker, tricky, antMan]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        round(boss, heroes)


start()
