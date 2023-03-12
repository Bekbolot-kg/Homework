
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def hero_name(self):
        return f'Hero name is {self.name}'

    def points_2(self):
        self.health_points *= 2

    def __str__(self):
        return f'Hero - {self.nickname} \nSuperpower - {self.superpower} \nHealth_points - {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

class FieryHero(SuperHero):
    location = 'volcano'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def points_2(self):
        self.health_points **= 2
        self.fly = True

    def fly_damage(self):
        print(f'Fly - {self.fly}')
        print(f'Damage - {self.damage}')


class WaterHero(SuperHero):
    location = 'ocean'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def points_2(self):
        self.health_points **= 2
        self.fly = True

    def fly_damage(self):
        print(f'Fly - {self.fly}')
        print(f'Damage - {self.damage}')

class Villain(FieryHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 3



hero = SuperHero('Piter Parker', 'Spider man', 'Spider power', 665, 'Hello villain')

fiery_hero = FieryHero('Nurbek', 'Fiery Man', "Fiery", 500, "Blaze", 150, True)
water_hero = WaterHero('Juni', 'Water man', 'Water', 1000, "Dive", 100, False)
villain = Villain('Iko', 'Black Eye', 'Laser', 666, "I am Black Eye", 1500)

print(hero.hero_name())
hero.points_2()
print(hero)
print(len(hero))
print()

fiery_hero.points_2()
print(fiery_hero)
fiery_hero.fly_damage()
print()


print(water_hero)
water_hero.fly_damage()
print()


villain.crit()
villain.fly_damage()

print(Villain.crit(water_hero))
