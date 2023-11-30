from room import Room

class Double(Room):
    def __str__(self):
        return f"Double room {self.room_number}, price: {self.price} / night"

second_room = Double(201, 4500)
print(second_room)