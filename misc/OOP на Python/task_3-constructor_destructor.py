import random

class Person:
    def __init__(self, name, surname, qual = 1):
        self.name = name
        self.surname = surname
        self.qual = qual
    
    def getInfo(self):
        info = "Name: {}\n".format(self.name)
        info += "Surname: {}\n".format(self.surname)
        info += "Qualification: {}\n".format(self.qual)
        return info

    def __del__(self):
        print("Matane, dear {0} {1}".format(self.name, self.surname))

person_1 = Person("Klaus", "Frietz", random.randint(1, 100))
person_2 = Person("Erich", "Hartmann", random.randint(1, 100))
person_3 = Person("Leo", "Trotsky", random.randint(1, 100))
person_list = [person_1, person_2, person_3]

less_qualified = person_1
for person in person_list:
    print(person.getInfo())
    if person.qual < less_qualified.qual:
        less_qualified = person
        
del(less_qualified)
input()