class Band:
    def __init__(self, name="unknown"):
        self.name = name


class Musician:
    pass


class Guitarist(Band):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"


class Bassist:
    pass


class Drummer:
    pass
