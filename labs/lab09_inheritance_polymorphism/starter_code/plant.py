class Plant:
    def __init__(self, name, height_cm):
        self.name = name
        self.height_cm = height_cm

    def care_instructions(self):
        return "Plants do not need to be trimmed or watered."

    def __str__(self):
        return f"{self.name} is {self.height_cm} cm tall."


class Flower(Plant):
    def __init__(self, name, height_cm, color):
        # inherit from Plant class
        Plant.__init__(self, name, height_cm)
        self.color = color

    def care_instructions(self):
        return "Flowers do not need to be trimmed, and should be watered weekly."

    def __str__(self):
        return f"{self.name} is {self.height_cm} cm tall and {self.color} is."


class Vegetable(Plant):
    def __init__(self, name, height_cm, harvest_days):
        # inherit from Plant class
        Plant.__init__(self, name, height_cm)
        self.harvest_days = harvest_days

    def care_instructions(self):
        return "Vegetables should be trimmed and watered every 3 days."

    def __str__(self):
        return f"{self.name} is {self.height_cm} cm tall and takes {self.harvest_days} days to harvest."
