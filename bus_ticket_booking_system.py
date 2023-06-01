# Bus ticket booking system

# user class
class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

# bus class
class Bus:
    def __init__(self, coach, driver, arrival, departure, from_destination, to_destination) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_destination = from_destination
        self.to_destination = to_destination
        self.seat = ["Empty" for i in range(20)]

# Phibus class
class Phibus:
    total_bus = 5
    bus_list = []

    def add_bus(self):
        bus_no = int(input("Enter bus no: "))
        flag = 1

        for bus in self.bus_list:
            if bus_no == bus['coach']:
                print("Bus already added")
                flag = 0
                break

        if flag:
            bus_driver = input("Enter driver name: ")
            arrival_time = input("Enter bus arrival time: ")
            departur_time = input("Enter departure time: ")
            bus_from = input("Enter start place: ")
            bus_destination = input("Enter destination place: ")
            new_bus = Bus(bus_no, bus_driver, arrival_time, departur_time, bus_from, bus_destination)    
            self.bus_list.append(vars(new_bus))
            print("\nBus added successfully")
            print(self.bus_list)


# counter class
class Counter(Phibus):
    def reserve_seat(self):
        bus_no = int(input("Enter bus no: "))

        for bus in self.bus_list:
            if bus_no == bus['coach']:
                passenger = input("Enter passenger name: ")
                seat_no = int(input("Enter seat no: "))

                if seat_no >= 20:
                    print("Seat doesn't exists")
                elif bus['seat'][seat_no - 1] != "Empty": 
                    print("Seat is not available")
                else:
                    bus['seat'][seat_no - 1] = passenger
            else:
                print("Bus is not available right now")

        print(self.bus_list)

# b = Bus(3, "Abdullah", "23pm", "24pm", "ctg", "dhaka")
# print(vars(b))
phibus = Phibus()
phibus.add_bus()
counter = Counter()
counter.reserve_seat()

