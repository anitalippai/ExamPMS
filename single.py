from room import Room

class Single(Room):
    def __str__(self):
        return f"Single room {self.room_number}, price: {self.price} / night"

first_room = Single(101, 3500)
print(first_room)