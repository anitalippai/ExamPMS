from datetime import datetime


class Booking:
    def __init__(self):
        self.bookings = {}

    def free_room(self, room_number, start_date, end_date):
        room_bookings = self.bookings.get(room_number, [])
        for booking in room_bookings:
            if not (booking['end_date'] < start_date or booking['start_date'] > end_date):
                return False
        return True

    def book(self, room_number, start_date, end_date):
        if room_number not in self.bookings:
            self.bookings[room_number] = []

        if self.free_room(room_number, start_date, end_date):
            self.bookings[room_number].append({'start_date': start_date, 'end_date': end_date})
            return (f"Room {room_number} booked between "
                    f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}.")
        else:
            return f"Room {room_number} is not available in this period"

    def booking_dates(self, room_number):
        room_bookings = self.bookings.get(room_number, [])
        booking_str_list = []
        for booking in room_bookings:
            start_date_str = booking['start_date'].strftime('%Y-%m-%d')
            end_date_str = booking['end_date'].strftime('%Y-%m-%d')
            booking_str_list.append(f"{start_date_str} - {end_date_str}")
        return ", ".join(booking_str_list)


def new_booking():
    booking = Booking()

    while True:
        choose = input("What would you like to do? (bookings, book, quit): ")
        if choose == "bookings":
            room_number = int(input("Enter room number to check bookings: "))
            booked_dates = booking.booking_dates(room_number)
            if booked_dates:
                print(f"Bookings for Room {room_number}: {booked_dates}")
            else:
                print(f"No bookings found for Room {room_number}")
        elif choose == "book":
            room_number = int(input("Add room number: "))
            start_date_str = input("Start date (format: yyyy-mm-dd): ")
            end_date_str = input("End date (format: yyyy-mm-dd): ")
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            booked_room = booking.book(room_number, start_date, end_date)
            print(booked_room)
        elif choose == "quit":
            print("See you soon!")
            break
        else:
            print("Invalid select.")


new_booking()