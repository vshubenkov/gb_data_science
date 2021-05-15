class ClsWorker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.dict_sallary = {"wage": wage, "bonus": bonus}


class ClsPosition(ClsWorker):
    def get_full_name(self):
        return self.name, self.surname, self.position

    def get_total_income(self):
        return self.dict_sallary["wage"] + self.dict_sallary["bonus"]


obj_Position = ClsPosition("Slava", "Shubenkov", "IT", 1000, 200)
print(obj_Position.get_full_name())
print(obj_Position.get_total_income())
