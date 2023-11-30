from room import Room

class Single(Room):
    def __init__(self, room_number, price, type):
        super().__init__(room_number, price)
        self.type = type
    def __str__(self):
        return f"Single room {self.room_number} with {self.type} view, price: {self.price} / night"

first_room = Single(101, 3500, 'sea')
print(first_room)