import pandas as pd
import os
import re


class User:
    def __init__(self, id, first_name, last_name, username, email, password, phone,projects=[]):
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
                print('Registration Cancelled')
                return
            if not re.match(r'^[a-zA-Z]+$', inputFirstName):
                print("Invalid name. Only letters are allowed.")
                continue  
            else:   
                break
            
        while True:
            inputLastName = input("Enter your last name: ")
            if inputLastName.lower() == "exit":
                print('Registration Cancelled')
                return
            if not re.match(r'^[a-zA-Z]+$', inputLastName):
                print("Invalid name. Only letters are allowed.")
                continue  
            else:   
                break

        while True:
            inputUsername = input("Enter your username: ")
            if inputUsername.lower() == "exit":
                print('Registration Cancelled')
                return
            if not re.match(r'^[a-zA-Z]+[0-9]*$', inputUsername):
                print("Invalid username. Only letters and numbers are allowed.")
                continue  
            else:   
                break

        while True:
            inputEmail = input("Enter your email: ")
            if inputEmail.lower() == "exit":
                print('Registration Cancelled')
                return
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', inputEmail):
                print("Invalid email.")
                continue  
            else:   
                break

        while True:
            inputPassword = input("Enter your password: ")
            if inputPassword.lower() == "exit":
                print('Registration Cancelled')
                return
            if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$'
, inputPassword):
                print("Invalid password. Password must be at least 8 characters long and contain at least one letter and one number and one special character")
                continue  
            else:   
                break

        while True:
            inputConfirmPassword = input("Confirm your password: ")
            if inputConfirmPassword.lower() == "exit":
                print('Registration Cancelled')
                return
            if inputPassword != inputConfirmPassword:
                print("Passwords do not match.")
                continue  
            else:   
                break

        while True:
            inputPhone = input("Enter your phone number: ")
            if inputPhone.lower() == "exit":
                print('Registration Cancelled')
                return
            if not re.match(r'^01[0125][0-9]{8}$', inputPhone):
                print('Invalid Egyptian Phone')
                continue  
            else:   
                break
        
        id = User.__generate_user_id()

        

        user = User(id, inputFirstName, inputLastName, inputUsername, inputEmail, inputPassword, inputPhone)
        user.save_to_file()
        return user



    @staticmethod
    def __generate_user_id():
        file_path = 'users.csv'
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                return int(df.tail(1)['id'].iloc[0]) + 1
        return 1
    
    def save_to_file(self):
        file_path = 'users.csv'

        user_data = {
            'id': [self.__id],
            'first_name': [self.__first_name],
            'last_name': [self.__last_name],
            'username': [self.__username],
            'email': [self.__email],
            'password': [self.__password],
            'phone': [self.__phone]
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

            df = pd.read_csv('users.csv')

            user_data = df[(df['username'] == inputUsername) & (df['password'] == inputPassword)]

            if user_data.empty:
                print("Invalid username or password.")
            else:
                user = user_data.iloc[0]

                projects_df = pd.read_csv('projects.csv')
                user_projects_data = projects_df[projects_df['creator_id'] == user['id']]
                user_projects = []

                for _, project in user_projects_data.iterrows():
                    project_obj = Project(
                        project['id'],
                        project['title'],
                        project['details'],
                        project['target_amount'],
                        project['start_date'],
                        project['end_date'],
                        project['creator_id']
                    )
                    user_projects.append(project_obj)

                return User(user['id'], user['first_name'], user['last_name'], user['username'], user['email'], user['password'], user['phone'],user_projects)





    def insert_project(self): #create project I mean..
    #هنا برده هتاخد بيانات المشروع واحدة واحدة من اليوزر
    # البيانات هي title, details, target_amount, start_date, end_date (ادي بصة على كلاس بروجكت تحت)
    # هتاخدهم وتعمل بيهم اوبجكت من النوع بروجكت (ادي بصة على كلاس بروجكت تحت)
    # الاوبجكت دا هياخد منك بقى زيادة عليهم الid بتاع اليوزر اللي مستدعي الفنكشن اللي احنا فيها دي

    # وغالبا هنضطر كمان نديله id للبروجكت ذات نفسه عشان نتعامل مع البروجكت بعدين .. فبرده هنشوف اخر id في فايل البروجكتس ونزود عليه 1 ونديهوله
    # بس الid دا خلي اوبجكت البروجكت بقى هو اللي مسؤول يعملها
    # هي مش ضرورية لحظة انشاء اوبجكت بروجكت .. هي ضرورية لحظة الinsert
    # project = Project(title, details, target_amount, start_date, end_date, self.__id) فالمهم هنكريت بس كدا دلوقت

    # اوبجكت البروجكت فيه فنكشن insert اسمها  .. انسرت دي بقى هي هتحط بيانات الاوبكت دا على فايل البروجكتس .. مالناش دعوة ازاي دلوقت لما نجيلها.. المهم هتستخدمها على طول
    #project.insert()
    #  ويدوب بقى زود البروجكت  في الليستة
    #self.__projects.append(project)



    # خدت بالي اننا لازم نعمل validation على التاريخ ..
    # برده يفضل يكون الvalidation فنكشن منفصلة __validate_date
    # وتقعد تعمل لوب لغاية ما تطلع valid وكدا

        pass

    def show_projects(self):



            #دي هتمسك الليست وتعرضها
            # لاحظ ان  الليست بتحتوي اوبجكتس من النوع بروجكت  ..
            # الاحسن نعمل فنكشن جوا البروجكت اسمها show ونلوب ونستخدمها لكل واحد منهم
        print(
            f"{'ID'.ljust(4)} | {'Title'.ljust(15)} | {'Details'.ljust(30)} | {'Target Amount'.ljust(15)} | {'Start Date'.ljust(10)} | {'End Date'.ljust(10)}")
        print("-" * 100)


        for project in  self.__projects:
            project.show()



        
        pass

    def delete_project(self):
        if not self.__projects:
            print("You have no projects to delete.")
            return
        try:
            project_id = int(input("Enter the ID of the project you want to delete: "))
            
            for project in self.__projects:
                if hasattr(project, '_Project__id') and project._Project__id == project_id:
                    project.delete()  
                    self.__projects.remove(project)  
                    print("Project deleted successfully.")
                    return

            print("Project not found.")

        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    def edit_project(self):
        #دي هتطلب id البروجكت وتدور عليه في الليست ولما تلاقيه..
        # مش عارف بقى في كذا طريقة
        # أروق طريقة في دماغي انك تروح مشغل فنكشن insert_project وخلاص xD
        # وبعدها تشغل delete_project على القديم
        # شغلله بس show قبلها عشان يشوف البروجكت اللي هو بيعدله وخلاص

        pass


    def show_projects_by_date(self):
        #هتاخد التاريخ وتدور جوا الليستة برده وكدا وتعرض
        pass




        # ملحوظة .. المفروض الاختيارات بتاعة القائمة دي يتعمللها كلاس لوحدها اسمه المينيو مثلا وكل مسؤوليته انه بيجمع البيانات زي ما قلنا
        # وبعد ما يجمع مثلا بيانات الregistration يروح يبعتها لفنكشن register اللي في كلاس User (هتكون بتاخد انبوتس بقى) وهي تبقى مسؤوليتها انها تكريت نيو يوزر وتحطه في الفايل وكدا
        # بس انا خليت كله هنا عشان ما نتحولش


# Project class to handle project creation, editing, deletion, and viewing
class Project:
    def __init__(self,id, title, details, target_amount, start_date, end_date, creator_id):
        self.__id = id
        self.__title = title
        self.__details = details
        self.__target_amount = target_amount
        self.__start_date = start_date
        self.__end_date = end_date
        self.__creator_id = creator_id

    def insert(self):
        # دي هتجيب id بس الاول وبعدين تحط البيانات كلها بقى بالid بكله في الفايل
        # يعني قصدي هتعمل self.__id = id عشان هنحتاجه طبعا
        # وبعدين تحط كل البيانات دي كبروجكت في فايل البروجكتس مرة واحدة


        try:
            self.__id = Project.__generate_project_id()
            new_project = {
                'id': self.__id,
                'title': self.__title,
                'details': self.__details,
                'target_amount': self.__target_amount,
                'start_date': self.__start_date,
                'end_date': self.__end_date,
                'creator_id': self.__creator_id
            }

            file_path = 'projects.csv'

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
    def __generate_project_id():
    #خلي جزء جلب اخر id + 1 دا هنا
    # واستخدمه في الفنكشن اللي فوق .. نضافة كود مش اكتر

        file_path = 'projects.csv'
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                return int(df.tail(1)['id'].iloc[0]) + 1
        return 1


    def delete(self):
        # هنا هتاخد الid وتروح تشيل الريكورد بتاعه من الفايل بس وخلاص
        # .. لقطة حلوة انك تdestruct الاوجكت بعدها
        pass

    @staticmethod
    def __split_string(string, size):
        list_of_splits = []
        while(True):
            if len(string)>size:
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

        max_lines = max(len(title_parts), len(details_parts), len(target_parts), len(start_parts), len(end_parts))

        for i in range(max_lines):
            print(f"{(id_parts[i] if i < len(id_parts) else '').ljust(4)} | "
                  f"{(title_parts[i] if i < len(title_parts) else '').ljust(15)} | "
                  f"{(details_parts[i] if i < len(details_parts) else '').ljust(30)} | "
                  f"{(target_parts[i] if i < len(target_parts) else '').ljust(15)} | "
                  f"{(start_parts[i] if i < len(start_parts) else '').ljust(10)} | "
                  f"{(end_parts[i] if i < len(end_parts) else '').ljust(10)}")





    # لو عايز تعمل edit معقد .. غالبا هتحتاج setters



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
            print("3. Delete a project")
            print("4. Edit a project")
            print("5. Logout")

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
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
                continue
