class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_hero_name(self):
        print(f'Имя героя: {self.name}')

    def increase_health(self):
        self.health_points *= 2
        print(f'Здоровье было удвоено! Было: {int(self.health_points/2)} Стало: {self.health_points}')

    def __str__(self):
        return (f"Прозвище: {self.nickname}\n"
                f"Супер способность: {self.superpower}\n"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)

# new_hero = SuperHero('Peter Parker', 'Spider-Man', 'Web', 50,
#                      'With great power, there must also come great responsibility')
#
# new_hero.print_hero_name()
# new_hero.increase_health()
# print(new_hero)
# print(len(new_hero))


class AirHero(SuperHero):
    areas_to_defend = ['Sky Castle', 'Great Tower', 'Block C']

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def increase_health(self):
        self.health_points **= 2
        self.fly = True
        print('Здоровье было возведено в квадрат!')

    def print_phrase(self):
        print('True in the True_phrase')


class EarthHero(SuperHero):
    areas_to_defend = ['Block A', 'Block B', 'Block C', 'Sacred City']

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def increase_health(self):
        self.health_points **= 2
        self.fly = True
        print('Здоровье было возведено в квадрат!')

    def print_phrase(self):
        print('True in the True_phrase')


air_hero = AirHero('Jake Robinson', 'Hawk', 'Hawk eye', 80, 'God bless you', 55, True)
earth_hero = EarthHero('Michel Brakestone', 'Titan', 'Iron body', 190, "It's a show time!", 35)
print(air_hero)
air_hero.increase_health()
air_hero.print_phrase()
print('==================')
print(earth_hero)
earth_hero.increase_health()
earth_hero.print_phrase()


class Villain(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2
        print('Урон был возведен в квадрат')


vil1 = Villain('Brad', 'Boss', 'Manipulating', 100, 'Get him', 30)
print('==================')
print(vil1)
vil1.crit()
