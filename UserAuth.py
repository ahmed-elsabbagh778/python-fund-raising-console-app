import re

class User:
    def __init__(self, firstName, lastName, username, email, password, phone):
        self.firstName = self.setFirstName(firstName)
        self.lastName = self.setLastName(lastName)
        self.username = self.setUsername(username)
        self.email = self.setEmail(email)
        self.password = self.setPassword(password)
        self.phone = self.setPhone(phone)

    def __str__(self):
        return (f"First name: {self.firstName}\nLast name: {self.lastName}\nUsername: {self.username}\nEmail: {self.email}\nPassword: {self.password}\nPhone number: {self.phone}")

    def setFirstName(self, firstName):
        if re.match(r'^[a-zA-Z]+$',firstName):
            self.firstName = firstName
            return firstName
        else:
            print("Invalid name")
            return
        


    def setLastName(self,lastName):
        if re.match(r'^[a-zA-Z]+$',lastName):
            self.lastName = lastName
            return lastName
        else:
            print("Invalid name")
            return

    def setUsername(self, username):
        if re.match(r'^[a-zA-Z]+[0-9]*$',username):
            self.username = username
            return username
        else:
            print("Invalid username")
            return

    def setEmail(self, email):
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
            self.email = email
            return email
        else:
            print("Invalid email")
            return

    def setPassword(self, password):
        if re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',password):
            self.password = password
            return password
        else:
            print("Invalid password")
            return

    def setPhone(self, phone):
        if re.match(r'^\+201[0125][0-9]{8}$', phone):
            self.phone = phone
            return phone
        else:
            print('Invalid Phone')
            return

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
        

inputFirstName = input("Enter your first name: ")
inputLastName = input("Enter your last name: ")
inputUsername = input("Enter your username: ")
inputEmail = input("Enter your email: ")
inputPassword = input("Enter your password: ")
inputConfirmPassword = input("Confirm your password: ")
inputPhone = input("Enter your phone number: ")

user1 = User(inputFirstName, inputLastName, inputUsername, inputEmail, inputPassword, inputPhone)
print(user1)


inputUsername = input("Enter your username: ")
inputPassword = input("Enter your password: ")

while not user1.loginUser(inputUsername, inputPassword):
    inputUsername = input("Enter your username: ")
    inputPassword = input("Enter your password: ")
else:
    print("You are logged in")