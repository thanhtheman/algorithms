#Abstraction

#Hiding unnecessary details on the user's standpoint. The user only cares how they can send an email. They don't care about connecting to a server, authenticating...etc. so we "abstract" those technical things from them. Encapsulation is more about control access by using public vs private properties and methods.

class EmailService:
    def _connect(self):
        print("Connecting to email server...")
    
    def _authenticate(self, username):
        print(f"Authenticating {username}...")

    def send_email(self, username):
        self._connect()
        self._authenticate(username)
        print("Email was successfully sent")
        self._disconnect()
    
    def _disconnect(self):
        print("Disconnecting...")

email = EmailService()
# email._authenticate("something")
# email.send_email("thanh")

#Inheritance
# a sub class of a big class such as: bike is a sub-calss of a big class vehicle.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print('Engine is starting...')
    def stop(self):
        print('Engine is stopping...')

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year) # passing values to the parent class
        self.number_of_doors = number_of_doors

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year) # passing values to the parent class
        self.number_of_wheeles = number_of_wheels

car = Car('Toyota', 'RAV4', 2025, 4)
bike = Bike('Mountain', 'Adventure', 2026, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
