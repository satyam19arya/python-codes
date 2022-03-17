#1 Create a class programmer for storing information of the programmers working at microsoft
class Programmer:
    company="Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}")


aman=Programmer("Aman","Skype")
rohan=Programmer("Rohan","Github")
aman.getInfo()
rohan.getInfo()


#2 Write a class calculator capable of finding square,cube and square root of a number
class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The value of {self.num} square is {self.num **2}")

    def cube(self):
        print(f"The value of {self.num} cube is {self.num **3}")

    def squareRoot(self):
        print(f"The value of {self.num} square root is {self.num **0.5}")

a=Calculator(5)
a.square() 
a.cube()
a.squareRoot()


#3 Write a class Train which has methods to book a ticket, get status(no. of seats) and get fare information of trains running under Indian Railways
class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare =fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"You ticket is booked! You seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full!")


a=Train("Rajdhani Express (12326)",400,1)
a.getStatus()
a.bookTicket()
a.getStatus()
a.bookTicket()