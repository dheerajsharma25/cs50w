# class point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
# p= point(2,8)
# print(p.x)
# print(p.y)



class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passangers(self,name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True


    def open_seats(self):
        return self.capacity - len(self.passangers)


flight = Flight(3)

people = ["harry","ron","hermoine","ginny"]
for person in people:
    if flight.add_passangers(person):
        print(f"added {person} to the flight sucessfully")
    else:
        print(f"no available seats for {person}")
