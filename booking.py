from hotel import Hotel
from datetime import datetime


class Booking:
    def __init__(self, hotel, room_number):
        self.hotel = hotel
        self.room_number = room_number
        self.bookings = []

    def free_room(self, start_date, end_date):
        for booking in self.bookings:
            if not (booking['end_date'] < start_date or booking['start_date'] > end_date):
                return False
        return True

    def book(self, start_date, end_date):
        if self.free_room(start_date, end_date):
            self.bookings.append({'start_date': start_date, 'end_date': end_date})
            return (f"Room {self.room_number} booked between "
                    f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}.")
        else:
            return f"Room {self.room_number} is not available in this period"
        pass

    def make_booking(self, room_number, start_date, end_date):
        for room in self.hotel.rooms:
            if room.room_number == room_number:
                return self.book(start_date, end_date)
        return "Room is not found."

    def booking_dates(self):
        booking_str_list = []
        for booking in self.bookings:
            start_datum_str = booking['start_date'].strftime('%Y-%m-%d')
            end_date_str = booking['veg_datum'].strftime('%Y-%m-%d')
            booking_str_list.append(f"{start_datum_str} - {end_date_str}")
        return ", ".join(booking_str_list)


def new_booking(hotel: Hotel):
    hotel.upload_rooms()

    while True:
        choose = input("What would you like to do? (bookings, book, quit): ")
        if choose == "bookings":
            print("bookings")
        elif choose == "book":
            room_number = int(input("Add room number: "))
            start_date_str = input("Start date (format: yyyy-mm-dd): ")
            end_datum_str = input("End date (format: yyyy-mm-dd): ")
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_datum_str, '%Y-%m-%d')

            booking = Booking(hotel, room_number)
            booked_room = booking.make_booking(room_number, start_date, end_date)
            print(booked_room)
        elif choose == "quit":
            print("See you soon!")
            break
        else:
            print("Invalid select.")


first_hotel = Hotel('Pythonia')
new_booking(first_hotel)