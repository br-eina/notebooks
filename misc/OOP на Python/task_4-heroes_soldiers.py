import random

class Human():
    id_number = 0
    def __init__(self, team):
        self.id = Human.id_number
        # Change id_number with every initialization
        Human.id_number += 1
        self.team = team

class Hero(Human):
    def __init__(self, team, level = 1):
        Human.__init__(self, team)
        self.level = level
    def level_up(self):
        self.level += 1

class Soldier(Human):
    def __init__(self, team):
        Human.__init__(self, team)
        self.attached_hero = None
    def follow_hero(self, hero):
        self.attached_hero = hero.id

hero_A = Hero("A")
hero_B = Hero("B")

team_list = ["A", "B"]

army_A = []
army_B = []

for i in range(21):
    team = random.choice(team_list)
    if team == "A":
        army_A.append(Soldier("A"))
    else:
        army_B.append(Soldier("B"))

print("Quantity of ""A"" team: {}".format(len(army_A)))
print("Quantity of ""B"" team: {}\n".format(len(army_B)))

if len(army_A) > len(army_B):
    hero_A.level_up()
else:
    hero_B.level_up()

rand_soldier_A = random.choice(army_A)
rand_soldier_A.follow_hero(hero_A)
print("Hero id: {}".format(hero_A.id))
print("Hero level: {}".format(hero_A.level))
print("Soldier id: {}".format(rand_soldier_A.id))