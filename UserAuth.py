import re

class User:
    id_counter = 0

    def __init__(self, firstName, lastName, username, email, password, phone):
        self.id = self.generate_user_id()
        self.setFirstName(firstName)
        self.setLastName(lastName)
        self.setUsername(username)
        self.setEmail(email)
        self.setPassword(password)
        self.setPhone(phone)
    
    def __str__(self):
        return (f"User ID: {self.id}\nFirst Name: {self.firstName}\nLast Name: {self.lastName}\nUsername: {self.username}\nEmail: {self.email}\nPassword: {self.password}\nPhone: {self.phone}")

    @classmethod
    def generate_user_id(cls):
        cls.id_counter += 1
        return cls.id_counter

    def setFirstName(self, firstName):
        if re.match(r'^[a-zA-Z]+$',firstName):
            self.firstName = firstName
            return True
        else:
            print("Invalid name")
            return False
        


    def setLastName(self,lastName):
        if re.match(r'^[a-zA-Z]+$',lastName):
            self.lastName = lastName
            return True
        else:
            print("Invalid name")
            return False

    def setUsername(self, username):
        if re.match(r'^[a-zA-Z]+[0-9]*$',username):
            self.username = username
            return True
        else:
            print("Invalid username")
            return False

    def setEmail(self, email):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
            self.email = email
            return True
        else:
            print("Invalid email")
            return False

    def setPassword(self, password):
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',password):
            self.password = password
            return True
        else:
            print("Invalid password")
            return False

    def setPhone(self, phone):
        if re.match(r'^\+201[0125][0-9]{8}$', phone):
            self.phone = phone
            return True
        else:
            print('Invalid Phone')
            return False

    def registerUser(self, confirmPassword):
        if self.password == confirmPassword:
            return True
        else:
            return False
        
        
    def loginUser(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False
        

# inputFirstName = input("Enter your first name: ")
# inputLastName = input("Enter your last name: ")
# inputUsername = input("Enter your username: ")
# inputEmail = input("Enter your email: ")
# inputPassword = input("Enter your password: ")
# inputConfirmPassword = input("Confirm your password: ")
# inputPhone = input("Enter your phone number: ")

# user1 = User(inputFirstName, inputLastName, inputUsername, inputEmail, inputPassword, inputPhone)
# print(user1)


# inputUsername = input("Enter your username: ")
# inputPassword = input("Enter your password: ")

# while not user1.loginUser(inputUsername, inputPassword):
#     inputUsername = input("Enter your username: ")
#     inputPassword = input("Enter your password: ")
# else:
#     print("You are logged in")