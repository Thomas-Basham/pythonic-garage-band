import abc
from abc import ABC


class Band(ABC):
    def __init__(self, name="unknown", band_name=[]):
        self.name = name
        Band.name = band_name

    @abc.abstractmethod
    def get_instrument(self):
        pass


class Musician(Band):
    pass


class Guitarist(Band):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"


class Bassist(Band):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"


class Drummer(Band):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"



