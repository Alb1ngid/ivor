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

    def double_health(self):
        self.health_points *= 2
        print(f'Здоровье было удвоено! Было: {int(self.health_points/2)} Стало: {self.health_points}')

    def __str__(self):
        return (f"Прозвище: {self.nickname}\n"
                f"Супер способность: {self.superpower}\n"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


new_hero = SuperHero('Peter Parker', 'Spider-Man', 'Web', 50, 'With great power, there must also come great responsibility')

new_hero.print_hero_name()
new_hero.double_health()
print(new_hero)
print(len(new_hero))