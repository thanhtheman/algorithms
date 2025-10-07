class Owner:
    user_count = 0
    def __init__(self, name, email, phone_number, address):
        self.name = name
        self.__phone_number = phone_number
        self._email = email
        self.address = address
        # print(self.__guess_what())
        Owner.user_count += 1
    
    def __guess_what(self): #only access inside
        return self.address

    @property
    def guess_what(self):
        return self.__guess_what()

    @property
    def email(self):
        return self._email
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @email.setter
    def email(self, new_email:str):
        if "@" in new_email:
            self._email = new_email
            print("Email is successfully changed!")
        else:
            raise ValueError("Email is invalid!")
    
    @staticmethod
    def is_it_community(address):
        return "bales" in address
        

owner = Owner(name="Thanh", email="th@gmail.com", phone_number="647 233 4472", address="31 bales M2N 7L6")

# print(owner.phone_number)
# print(owner.email)
# owner.email = "thanh@gmail.com" 
# print(owner.email) 

owner1 = Owner("David", "david@gmail.com", phone_number="123 456 7890", address="33 bold ave")

# print(Owner.user_count)
# print(Owner.is_it_community(owner.address))
print(owner.guess_what)
