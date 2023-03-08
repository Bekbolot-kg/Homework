
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

hero = SuperHero('Piter Parker', 'Spider man', 'Spider power', 665, 'Hello villain')

print(hero.hero_name())
hero.points_2()
print(hero)
print(len(hero))

