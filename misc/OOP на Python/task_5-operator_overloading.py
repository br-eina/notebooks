class Human:
    def __init__(self, sex):
        self.sex = sex
    def __add__(self, other):
        if self.sex != other.sex:
            return "Getero family"
        if self.sex == other.sex:
            if self.sex == "Male":
                return "Ultra gay"
            else:
                return "Fem squad"
    
human_1 = Human("Female")
human_2 = Human("Female")

print(human_1 + human_2)