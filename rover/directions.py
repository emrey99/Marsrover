from abc import ABC, abstractmethod


class Directions(ABC):

    turn_left_side = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'

    }

    turn_right_side = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'

    }

    @abstractmethod
    def turn_left(self):
        raise NotImplementedError()

    @abstractmethod
    def turn_right(self):
        raise NotImplementedError()

    @abstractmethod
    def move(self):
        raise NotImplementedError()


