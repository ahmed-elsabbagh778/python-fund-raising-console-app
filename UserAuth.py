class User:
    def __init__(self, firstName, lastName, username, email, password, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone

    def registerUser(self, confirmPassword):
        if self.password == confirmPassword:
            return "Success"
        else:
            return "Failed"
        
    def loginUser(self, username, password):
        if self.username == username and self.password == password:
            return "user logged in"
        else:
            return "user not logged in"
        


inputFirstName = input("Enter your first name: ")
inputLastName = input("Enter your last name: ")
inputUsername = input("Enter your username: ")
inputEmail = input("Enter your email: ")
inputPassword = input("Enter your password: ")
inputConfirmPassword = input("Confirm your password: ")
inputPhone = input("Enter your phone number: ")

user1 = User(inputFirstName, inputLastName, inputUsername, inputEmail, inputPassword, inputPhone)

while user1.registerUser(inputConfirmPassword) == "Failed":
    inputConfirmPassword = input("Passwords do not match. Confirm your password: ")
else:
    print(user1.registerUser(inputConfirmPassword))

inputLoginUsername = input("Enter your username: ")
inputLoginPassword = input("Enter your password: ")
while user1.loginUser(inputLoginUsername, inputLoginPassword) == "user not logged in":
    print("Incorrect username or password")
    inputLoginUsername = input("Enter your username: ")
    inputLoginPassword = input("Enter your password: ")

else:
    print(user1.loginUser(inputUsername, inputPassword))
       
print(user1.firstName, user1.lastName, user1.username, user1.email, user1.password, user1.phone)