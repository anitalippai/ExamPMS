from room import Room

class Double(Room):
    def __init__(self, room_number, price, boarding):
        super().__init__(room_number, price)
        self.boarding = boarding
    def __str__(self):
        return f"Double room {self.room_number}, {self.boarding}, price: {self.price} / night"

second_room = Double(201, 4500, 'All Inclusive')
print(second_room)