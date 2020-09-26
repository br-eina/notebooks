import random

class Warrior:
    def setName(self, n):
        self.name = n
    def getName(self):
        try:
            return self.name
        except:
            print("Define a warrior name")
    health = 100
    damage = 20
    def hit(self, war):
        war.health = war.health - self.damage

war_1 = Warrior()
war_1.setName("Dante")

war_2 = Warrior()
war_2.setName("Nero")

war_set = [war_1, war_2]

def turn():
    # Random choose attacker
    attacker_index = random.randint(0, len(war_set) - 1)
    if attacker_index == 0:
        damaged_index = 1
    else:
        damaged_index = 0
    attacker = war_set[attacker_index]
    damaged = war_set[damaged_index]

    attacker.hit(damaged)

    print("Attacker: {0}".format(attacker.getName()))
    print("{0}'s remaining health: {1}".format(damaged.getName(), damaged.health))

    if damaged.health == 0:
        name = damaged.getName()
        print("Defeated: ", name)

for i in range(10):
    if war_1.health != 0 and war_2.health != 0:
        print("Turn {}".format(i + 1))
        turn()
        
        # print



# name = war_1.getName()
# print(name)
    