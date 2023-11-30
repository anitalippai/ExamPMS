from room import Room
from single import Single
from double import Double


class Hotel:
    def __init__(self, name):
        self.rooms = []
        self.name = name

    def add_room(self, room: Room):
        self.rooms.append(room)

    def upload_rooms(self):
        self.add_room(Single(101, 2500, 'sea'))
        self.add_room(Single(102, 2000, 'garden'))
        self.add_room(Double(201, 5000, 'Breakfast'))
        self.add_room(Double(202, 6000, 'Half-pension'))

