# Fund Rasing Console App

A command-line application to manage users and projects, written in Python with CSV files used as a simple database.

## Features
- **User Registration**: Register new users with data validation (name, email, password, phone number)
- **User Login**: Log in users after verifying their username and password
- **Create Project**: Create projects for users (with validation for dates and amounts)
- **View Projects**: View all projects related to the user in a structured table
- **Edit Project**: Modify any project's details
- **Delete Project**: Permanently delete a project

## Data Storage
- Users are stored in the `users.csv` file.
- Projects are stored in the `projects.csv` file.
- Each project is linked to a user via `creator_id`.

## Validations
- Name: Letters only
- Username: Starts with letters and may include numbers
- Email: Standard format username@domain.com
- Password: Minimum 8 characters + one letter + one number + one special character
- Phone Number: Egyptian format 01X followed by 8 digits
- Project Dates: In YYYY-MM-DD format, and the end date must be later than the start date

## Libraries Used
- Pandas
- OS
- re
- datetime

## Requirements
- Python 3.6 or higher
- pandas library (can be installed via `pip install pandas`)

## How to Run
1. Run the code:
```bash
python main.py
```
2. Choose an option:
- Register
- Login
- Exit

## Author
Developed by Ahmed Elsabbagh, Othman Ahmed, Galal Owais, Ahmed Ibrahim, Asmaa Tarek and Ahmed Hani
