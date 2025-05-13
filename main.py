import pandas as pd
import os
import re
from datetime import datetime, timedelta


class User:
    def __init__(
        self, id, first_name, last_name, username, email, password, phone, projects=[]
    ):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__projects = projects

    @staticmethod
    def register():

        while True:
            inputFirstName = input("Enter your first name: ")
            if inputFirstName.lower() == "exit":
                print("Registration Cancelled")
                return
            if not re.match(r"^[a-zA-Z]+$", inputFirstName):
                print("Invalid name. Only letters are allowed.")
                continue
            else:
                break

        while True:
            inputLastName = input("Enter your last name: ")
            if inputLastName.lower() == "exit":
                print("Registration Cancelled")
                return
            if not re.match(r"^[a-zA-Z]+$", inputLastName):
                print("Invalid name. Only letters are allowed.")
                continue
            else:
                break

        while True:
            inputUsername = input("Enter your username: ")
            if inputUsername.lower() == "exit":
                print("Registration Cancelled")
                return
            if not re.match(r"^[a-zA-Z]+[0-9]*$", inputUsername):
                print("Invalid username. Only letters and numbers are allowed.")
                continue
            else:
                break

        while True:
            inputEmail = input("Enter your email: ")
            if inputEmail.lower() == "exit":
                print("Registration Cancelled")
                return
            if not re.match(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", inputEmail
            ):
                print("Invalid email.")
                continue
            else:
                break

        while True:
            inputPassword = input("Enter your password: ")
            if inputPassword.lower() == "exit":
                print("Registration Cancelled")
                return
            if not re.match(
                r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$", inputPassword
            ):
                print(
                    "Invalid password. Password must be at least 8 characters long and contain at least one letter and one number and one special character"
                )
                continue
            else:
                break

        while True:
            inputConfirmPassword = input("Confirm your password: ")
            if inputConfirmPassword.lower() == "exit":
                print("Registration Cancelled")
                return
            if inputPassword != inputConfirmPassword:
                print("Passwords do not match.")
                continue
            else:
                break

        while True:
            inputPhone = input("Enter your phone number: ")
            if inputPhone.lower() == "exit":
                print("Registration Cancelled")
                return
            if not re.match(r"^01[0125][0-9]{8}$", inputPhone):
                print("Invalid Egyptian Phone")
                continue
            else:
                break

        user = User(
            User.generate_user_id(),
            inputFirstName,
            inputLastName,
            inputUsername,
            inputEmail,
            inputPassword,
            inputPhone,
        )
        user.save_to_file()
        return user

    @staticmethod
    def generate_user_id():
        file_path = "users.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                return int(df.tail(1)["id"].iloc[0]) + 1
        return 1

    def save_to_file(self):
        file_path = "users.csv"

        user_data = {
            "id": [self.__id],
            "first_name": [self.__first_name],
            "last_name": [self.__last_name],
            "username": [self.__username],
            "email": [self.__email],
            "password": [self.__password],
            "phone": [self.__phone],
        }

        df_new = pd.DataFrame(user_data)

        if os.path.exists(file_path):
            df_existing = pd.read_csv(file_path)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_csv(file_path, index=False)
        else:
            df_new.to_csv(file_path, index=False)

        print("User registered successfully!")

    @staticmethod
    def login():
        while True:
            inputUsername = input("Enter your username: ")
            inputPassword = input("Enter your password: ")

            df = pd.read_csv("users.csv")

            user_data = df[
                (df["username"] == inputUsername) & (df["password"] == inputPassword)
            ]

            if user_data.empty:
                print("Invalid username or password.")
            else:
                user = user_data.iloc[0]

                projects_df = pd.read_csv("projects.csv")
                user_projects_data = projects_df[
                    projects_df["creator_id"] == user["id"]
                ]
                user_projects = []

                for _, project in user_projects_data.iterrows():
                    project_obj = Project(
                        project["id"],
                        project["title"],
                        project["details"],
                        project["target_amount"],
                        project["start_date"],
                        project["end_date"],
                        project["creator_id"],
                    )
                    project_obj._Project__id = project["id"]
                    user_projects.append(project_obj)

                return User(
                    user["id"],
                    user["first_name"],
                    user["last_name"],
                    user["username"],
                    user["email"],
                    user["password"],
                    user["phone"],
                    user_projects,
                )

    @staticmethod
    def is_valid_date_format(date_str):
        # pattern: YYYY-MM-DD only (e.g., 2024-05-11)
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        return bool(re.match(pattern, date_str))

    def insert_project(self):

        while True:
            title = input("Enter project title: ").strip()
            if title and not title.isdigit():
                break
            print("Invalid input. Title cannot be empty or digits only.")

        while True:
            details = input("Enter project details: ").strip()
            if details and not details.isdigit():
                break
            print("Invalid input. Details cannot be empty or digits only.")

        while True:
            total_target = input("Enter total target amount: ").strip()
            if total_target.isdigit():
                break
            else:
                print("Target amount must be a number.")

        while True:
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            if User.is_valid_date_format(start_date):
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            else: print("Invalid date format. Please use YYYY-MM-DD.")

        while True:
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            if User.is_valid_date_format(end_date):
                try:
                    datetime.strptime(end_date, "%Y-%m-%d")
                    if end_date >= start_date:
                        break
                    else:
                        print("End date must be after start date.")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            else: print("Invalid date format. Please use YYYY-MM-DD.")

        # Save project
        project = Project(
            id=Project.generate_project_id(),
            title=title,
            details=details,
            target_amount=total_target,
            start_date=start_date,
            end_date=end_date,
            creator_id=self.__id,
        )
        project.insert()
        self.__projects.append(project)

    def show_projects(self):

        # If user wants to filter by date
        filter_choice = (
            input("Do you want to filter projects by date? (y/n): ").strip().lower()
        )
        if filter_choice == "y":
            filtered_projects = self.search_projects_by_date()

            if not filtered_projects:
                print("No projects match the given date range.")
                return
        elif (
            not self.__projects
        ):  # if no filter requested and it is found that there are no projects ..
            print("No projects are there for you")
            return

        else:  # if no filter and there is ..
            filtered_projects = self.__projects

        # now show whatever we got..
        print(
            f"{'ID'.ljust(4)} | {'Title'.ljust(15)} | {'Details'.ljust(30)} | {'Target Amount'.ljust(15)} | {'Start Date'.ljust(10)} | {'End Date'.ljust(10)}"
        )
        print("-" * 100)

        for project in filtered_projects:
            project.show()

    def delete_project(self):
        if not self.__projects:
            print("You have no projects to delete.")
            return
        try:
            project_id = int(input("Enter the ID of the project you want to delete: "))

            for project in self.__projects:
                if project.get_id() == project_id:
                    project.delete()
                    self.__projects.remove(project)
                    print("Project deleted successfully.")
                    return

            print("Project not found.")

        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    def edit_project(self):
        if not self.__projects:
            print("You have no projects to edit.")
            return

        self.show_projects()
        try:
            project_id = int(input("Enter the ID of the project to edit: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        # Finding the chosen project by ID
        project = next(
            (p for p in self.__projects if p._Project__id == project_id), None
        )
        if project is None:
            print("Project not found.")
            return

        print("Leave any prompt blank to keep its current value.\n")

        # Either you'll put the new values or it'll keep the old ones
        # Title
        current_title = project._Project__title
        title_input = input(f"Title [{current_title}]: ")
        new_title = title_input.strip() or current_title

        # Details
        current_details = project._Project__details
        details_input = input(f"Details [{current_details}]: ")
        new_details = details_input.strip() or current_details

        # Target amount limits
        MIN_AMOUNT = 1000.0
        MAX_AMOUNT = 10_000_000.0

        # Target amount
        while True:
            current_target = project._Project__target_amount
            target_input = input(f"Target amount (EGP) [{current_target}]: ").strip()
            if not target_input:
                new_target_amount = current_target
                break
            try:
                new_target_amount = float(target_input)
                if new_target_amount < MIN_AMOUNT:
                    print(f"Amount must be at least {MIN_AMOUNT:,.0f} EGP.")
                elif new_target_amount > MAX_AMOUNT:
                    print(f"Amount must not exceed {MAX_AMOUNT:,.0f} EGP.")
                else:
                    break
            except ValueError:
                print("Invalid number. Please enter a numeric value.")

        # Set the date range
        MIN_DATE = datetime.today().date()
        MAX_DATE = (
            datetime.today() + timedelta(days=5 * 365)
        ).date()  # 5 years from today

        def prompt_for_date(prompt_text, current_value):
            current_date = datetime.strptime(current_value, "%Y-%m-%d").date()
            while True:
                date_input = input(
                    f"{prompt_text} [{current_date.isoformat()}]: "
                ).strip()
                if not date_input:
                    return current_date.isoformat()
                try:
                    user_date = datetime.strptime(date_input, "%Y-%m-%d").date()
                    if user_date < MIN_DATE:
                        print(f"Date cannot be before today ({MIN_DATE.isoformat()})")
                    elif user_date > MAX_DATE:
                        print(
                            f"Date cannot be more than 5 years from now ({MAX_DATE.isoformat()})"
                        )
                    else:
                        return user_date.isoformat()
                except ValueError:
                    print("Invalid format. Use YYYY-MM-DD.")

        while True:
            current_start = project._Project__start_date
            new_start_date = prompt_for_date("Start date", current_start)

            current_end = project._Project__end_date
            new_end_date = prompt_for_date("End date", current_end)

            if new_end_date > new_start_date:
                break
            else:
                print("Error: End date must be after start date. Please try again.")

        # Update CSV on disk
        projects_df = pd.read_csv("projects.csv")
        projects_df.loc[
            projects_df["id"] == project_id,
            ["title", "details", "target_amount", "start_date", "end_date"],
        ] = [
            new_title,
            new_details,
            new_target_amount,
            new_start_date,
            new_end_date,
        ]
        projects_df.to_csv("projects.csv", index=False)

        # Update the object as if the user wanna display it here, it has to show the new values, not the old ones.
        project._Project__title = new_title
        project._Project__details = new_details
        project._Project__target_amount = new_target_amount
        project._Project__start_date = new_start_date
        project._Project__end_date = new_end_date

        print("Project updated successfully.")

    # search by date
    def search_projects_by_date(self):
        while True:
            search_start_date = input(
                "Enter start date to search (YYYY-MM-DD) or leave empty to skip: "
            ).strip()
            if not search_start_date:
                break
            if User.is_valid_date_format(search_start_date):
                try:
                    search_start_date = datetime.strptime(search_start_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Could not be read as date!")
                    continue
            print("Invalid start date format. Please use YYYY-MM-DD.")

        # End date input with validation loop
        while True:
            search_end_date = input(
                "Enter end date to search (YYYY-MM-DD) or leave empty to skip: "
            ).strip()
            if not search_end_date:
                break
            if User.is_valid_date_format(search_end_date):
                try:
                    search_end_date = datetime.strptime(search_end_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Could not be read as date!")
                    continue
            print("Invalid end date format. Please use YYYY-MM-DD.")

        filtered_projects = []

        for project in self.__projects:
            project_start_date = datetime.strptime(project.get_start_date(), "%Y-%m-%d")
            project_end_date = datetime.strptime(project.get_end_date(), "%Y-%m-%d")

            if search_start_date and project_start_date < search_start_date:
                continue
            if search_end_date and project_end_date > search_end_date:
                continue

            filtered_projects.append(project)

        return filtered_projects


# Project class to handle project creation, editing, deletion, and viewing
class Project:
    def __init__(
        self, id, title, details, target_amount, start_date, end_date, creator_id
    ):
        self.__id = id
        self.__title = title
        self.__details = details
        self.__target_amount = target_amount
        self.__start_date = start_date
        self.__end_date = end_date
        self.__creator_id = creator_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_id(self):
        return self.__id

    def insert(self):
        try:
            self.__id = Project.generate_project_id()
            new_project = {
                "id": self.__id,
                "title": self.__title,
                "details": self.__details,
                "target_amount": self.__target_amount,
                "start_date": self.__start_date,
                "end_date": self.__end_date,
                "creator_id": self.__creator_id,
            }

            file_path = "projects.csv"

            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df = pd.concat([df, pd.DataFrame([new_project])], ignore_index=True)
            else:
                df = pd.DataFrame([new_project])

            df.to_csv(file_path, index=False)

            print("Project inserted successfully")

        except Exception as e:
            print(f"Error inserting project: {e}")

    @staticmethod
    def generate_project_id():
        file_path = "projects.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                return int(df.tail(1)["id"].iloc[0]) + 1
        return 1

    def delete(self):
        file_path = "projects.csv"

        if not os.path.exists(file_path):
            print("projects.csv file not found.")
            return

        try:
            df = pd.read_csv(file_path)
            df = df[df["id"] != self.__id]
            df.to_csv(file_path, index=False)

            print(f"Project with ID {self.__id} deleted successfully.")

        except Exception as e:
            print(f"Error while deleting project: {e}")

    @staticmethod
    def __split_string(string, size):
        list_of_splits = []
        while True:
            if len(string) > size:
                list_of_splits.append(string[:size])
                string = string[size:]
            else:
                list_of_splits.append(string)
                break

        return list_of_splits

    def show(self):
        title_parts = Project.__split_string(str(self.__title), 15)
        details_parts = Project.__split_string(str(self.__details), 30)
        target_parts = Project.__split_string(str(self.__target_amount), 15)
        start_parts = Project.__split_string(str(self.__start_date), 10)
        end_parts = Project.__split_string(str(self.__end_date), 10)
        id_parts = Project.__split_string(str(self.__id), 4)

        max_lines = max(
            len(title_parts),
            len(details_parts),
            len(target_parts),
            len(start_parts),
            len(end_parts),
        )

        for i in range(max_lines):
            print(
                f"{(id_parts[i] if i < len(id_parts) else '').ljust(4)} | "
                f"{(title_parts[i] if i < len(title_parts) else '').ljust(15)} | "
                f"{(details_parts[i] if i < len(details_parts) else '').ljust(30)} | "
                f"{(target_parts[i] if i < len(target_parts) else '').ljust(15)} | "
                f"{(start_parts[i] if i < len(start_parts) else '').ljust(10)} | "
                f"{(end_parts[i] if i < len(end_parts) else '').ljust(10)}"
            )

    @staticmethod
    def show_projects():
        if not os.path.exists("projects.csv"):
            print("Someone deleted the projects.csv >:(")
            return

        df = pd.read_csv("projects.csv")
        all_projects = []

        for _, row in df.iterrows():
            project = Project(
                row["id"],
                row["title"],
                row["details"],
                row["target_amount"],
                row["start_date"],
                row["end_date"],
                row["creator_id"],
            )
            all_projects.append(project)

        print(
            f"{'ID'.ljust(4)} | {'Title'.ljust(15)} | {'Details'.ljust(30)} | {'Target Amount'.ljust(15)} | {'Start Date'.ljust(10)} | {'End Date'.ljust(10)}"
        )
        print("-" * 100)

        for project in all_projects:
            project.show()


if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = User.register()
        elif choice == "2":
            user = User.login()
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            print("\nWhat would you like to do?")
            print("1. Create a project")
            print("2. View your projects")
            print("3. Delete one of your projects")
            print("4. Edit one of your projects")
            print("5. View all projects")
            print("6. Logout")

            action = input("Enter your choice: ")

            if action == "1":
                user.insert_project()
            elif action == "2":
                user.show_projects()
            elif action == "3":
                user.delete_project()
            elif action == "4":
                user.edit_project()
            elif action == "5":
                Project.show_projects()
            elif action == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
                continue
