from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, price, room_number):
        self.price = price
        self.room_number = room_number

    @abstractmethod
    def information(self):
        pass