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
            departure_time = input("Enter departure time: ")
            bus_from = input("Enter start place: ")
            bus_destination = input("Enter destination place: ")
            # assign a bus on line
            new_bus = Bus(bus_no, bus_driver, arrival_time, departure_time, bus_from, bus_destination)    
            self.bus_list.append(vars(new_bus))
            print("\nBus added successfully")
            print(self.bus_list)

# counter class
class Counter(Phibus):
    user_list = []

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

    def display_seat_plan(self):
        bus_no = int(input("Enter bus no: "))

        for bus in self.bus_list:
            if bus_no == bus['coach']:
                print("*" * 50)
                print()
                print(f"{' ' * 10}{'#' * 10} BUS INFO {'#' * 10}")
                print(f"Bus Number: {bus_no}\t\t\tDriver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']}\t\t\tDeparture time: {bus['departure']}")
                print(f"From: {bus['from_destination']}\t\t\tTo: {bus['to_destination']}")

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a - 1]}", end="\t")
                        a += 1

                    for j in range(2):
                        print(f"{a}. {bus['seat'][a - 1]}", end="\t")
                        a += 1
                    print()
                print("*" * 50)

    def get_user(self):
        return self.user_list

    def create_passenger(self):
        name = input("Enter you username: ")
        password = input("Enter your password: ")
        new_user = User(name, password)
        self.user_list.append(vars(new_user))

    def available_buses(self):
        if len(self.bus_list) == 0:
            print("No Buses Available\n")
        else:
            print("*" * 50)
            for bus in self.bus_list:
                print()
                print(f"{' ' * 10}{'#' * 10} BUS {bus['coach']} INFO {'#' * 10}")
                print(f"Bus Number: {bus['coach']}\t\t\tDriver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']}\t\t\tDeparture time: {bus['departure']}")
                print(f"From: {bus['from_destination']}\t\t\tTo: {bus['to_destination']}")
            print("*" * 50)


while True:
    company = Phibus()
    b = Counter()
    print("1. Create an account\n2. Login to your account\n3. Exit")

    user_input = int(input("Enter your choice: "))

    if user_input == 3:
        break
    elif user_input == 1:
        b.create_passenger()
    elif user_input == 2:
        name = input("Enter your username: ")
        password = input("Enter your password: ")

        flag = 0
        is_admin = False

        if name == "admin" and password == "123":
            is_admin = True
        if is_admin == False:
            for user in b.get_user():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' ' * 10} Welcome to the BUS BOOKING SYSTEM")
                    print("1. Available Buses\n2. Show bus info\n3. Reservation\n4. Exit")
                    a = int(input("Enter your choice: "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.available_buses()
                    elif a == 2:
                        b.display_seat_plan()
                    elif a == 3:
                        b.reserve_seat()
            else:
                print("No username found\n")
        else:
            while True:
                print(f"\n{' ' * 10} Hello Admin Welcome to the BUS BOOKING SYSTEM")
                print("1. Add Bus\n2. Available Buses \n3. Show Bus Info \n4. EXIT")
                a=int(input("Enter Your Choice : "))

                if a==4:
                    break
                elif a==1:
                    b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a==3:
                    b.display_seat_plan()

# b = Bus(3, "Abdullah", "23pm", "24pm", "ctg", "dhaka")
# print(vars(b))
# phibus = Phibus()
# phibus.add_bus()
# counter = Counter()
# counter.reserve_seat()

