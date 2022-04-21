import abc
from abc import ABC


class Band(ABC):
    def __init__(self, name="unknown"):
        self.name = name
        Band.name = name


class Musician(Band):
    pass


class Guitarist(Band):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return "Guitarist instance. Name = Joan Jett"



print((Guitarist("Joan Jett")))


class Bassist(Band):
    pass


class Drummer(Band):
    pass
