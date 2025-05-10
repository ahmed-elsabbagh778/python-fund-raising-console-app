import pandas as pd

# Use relative path
file_path = './users.csv'
df = pd.read_csv(file_path, dtype={'email': str}, skipinitialspace=True)

# Print the DataFrame and columns to debug
print("DataFrame:")
print(df)
print("Columns:", df.columns.tolist())

# Email validation loop
user_email_input = input("Enter Your Email: ")
is_email_exist = df['email'].str.lower().isin([user_email_input.lower()]).any()

while not is_email_exist:
    print("Email Not Exist")
    user_email_input = input("Enter Your Email: ")
    is_email_exist = df['email'].str.lower().isin([user_email_input.lower()]).any()

# Password validation loop
user_password_input = input("Enter Your Password: ")
try:
    stored_password = df.loc[df['email'].str.lower() == user_email_input.lower(), 'password'].iloc[0]
except IndexError:
    print("Email not found in the system.")
    exit(1)

# Convert stored_password to string for comparison
while str(stored_password) != user_password_input:
    print("Password Is Not Correct")
    user_password_input = input("Enter Your Password: ")

print("Welcome to The Fund Raising App")