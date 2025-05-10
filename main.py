import pandas as pd
import os


# User class to handle registration, login, and project management
class User:
    def __init__(self,id, first_name, last_name, email, password, phone):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__projects = []

        #السلام عليكم .. كل فنكشن في الكلاس دا  عبارة عن خيارات القائمة اللي هتظهر اول ما تشغل البرنامج ..
        # عايزك تروح تبص بس على اساميهم وتيجي هنا تاني .. بس تاني فنكشن دي مش خيار ها ***
        #   في الاول المستخدم هيختار بس register ولا login وبعدها تظهرله باقي الاختيارات
        # كل اختيار بتختاره المفروض انه هيطلب منك تدخلله حاجات معينة وكدا ..يعني مثلا الregistration هيطلب منك الاسم وا وا ..
        # فانت بتـprompt اليوزر انه يدخل الحاجة الفلانية وتعمل عليها validation وكدا

    @staticmethod
    def register():

        # الفنكشن دي اللي هتشتغل لما المستخدم يختار register  .. هي هتقعد تاخد منه المدخلات واحدة واحدة وتتشيك صحتها بلووب وكدا
        # الفنكشن دي static method فكأنها اشبه بميثود متعرفة في الهوا .. فرق ان احنا لما هنستدعيها هنقول User.register() بس
        # (وبالمرة وانت بتتشيك صحة كل انبوت ..تشيك لو الانبوت عبارة عن كلمة EXIT مثلا يخرج خلاص يريترن..هتبقى قايل للمستخدم على الموضوع دا يعني .. انه لو دخل EXIT يبقى عايز يكنسل)
        # لو خلاص كل الانبوتس تمام ..  تسجل البيانات دي كيوزر في ملف اليوزرز
        # فمبدئيا هتعمل id لليوزر
        # .. فلازم تشوف الفايل وتشوف اخر id وتزود عليه 1 وكدا وبعدين تسجل النيو يوزر دا في الملف .. ثم تاخد بقى البيانات دي كلها كدا بالid وتعمل بيها اوبجكت من النوع يوزر وتريترنه.. دي الطريقة اللي في دماغي يعني





        pass

    @staticmethod
    # (((((((دي مش خيار دي ها))))))
    def __generate_user_id():
        file_path = 'users.csv'
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                return int(df.tail(1)['id'].iloc[0]) + 1
        return 1

    @staticmethod
    def login():
        # .دي برده نفس الكلام .. الفرق انها بتبحث في فايل اليوزرز.. ولو لقته بتعمل اوبجكت ببيانته وترجع الاوبجكت .. خلي بالك ان بياناته دي هتشمل بيانات اليوزر نفسه من فايل اليوزر وكل المشاريع اللي تبعه في فايل المشاريع (هنا استخدام حتة الid) .. المشاريع هتتحط في ليستة ال__projects .. هتتحط كاوبجكتس من النوع بروجكت .. يعني كل مشروع يتكريته بروجكت ببياناته ويتضاف لليست

        # السطرين الجايين مش لازم تقراهم
        #  براحتك في حوار المشاريع دا .. ممكن تسيب الليستة فاضية لغاية ما يتطلب انها تتجاب
        # بس الاحسن تجيبهم دلوقت عشان لما يقرر يكريت بروجكت ونحطه في الفايل ما نضطرش نروح نجيبهم من الاول وجديد .. لا احنا نزود الجديد على الليستة اللي جايبينها وخلاص

        pass


    #تقدر تعمل  في الكلاس فنكشنز تستعملها جوا الفنكشنز دي .. يعني مثلا تعمل فنكشن اسمها __validate_phone تاخد الرقم وترجع bool وتستخدمها وكدا.. لنضافة الكود بس ..وخليها فنكشنز برايفت بقى __


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

            # ومعلش قبل اي حاجة حط السطرين دول
        print(
            f"{'ID'.ljust(4)} | {'Title'.ljust(15)} | {'Details'.ljust(30)} | {'Target Amount'.ljust(15)} | {'Start Date'.ljust(10)} | {'End Date'.ljust(10)}")
        print("-" * 100)

        
        pass

    def delete_project(self):
        #  دي هتطلب id البروجكت وتدور عليه في الليست ولما تلاقيه هتمسكه وتشغل منه فنكشن delete ..ديليت دي بقى هتدلته من فايل البروجكتس ..مالناش دعوة ازاي دلوقت
        #project.delete()
        #  ثم تشيله من الليستة باستخدام remove
        #    self.__projects.remove(project)

        # ولو ما لقيتهوش  اصلا تقولله مالقتش حاجة

        pass

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
    def __init__(self, title, details, target_amount, start_date, end_date, creator_id):
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
        # هنا هتاخد الid وتروح تشيل الريكورد بتاعه من الفايل بس وخلاص يا احمد يا ابراهيم
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

        print(title_parts,details_parts)
        max_lines = max(len(title_parts), len(details_parts), len(target_parts), len(start_parts), len(end_parts))

        for i in range(max_lines):
            print(f"{(id_parts[i] if i < len(id_parts) else '').ljust(4)} | "
                  f"{(title_parts[i] if i < len(title_parts) else '').ljust(15)} | "
                  f"{(details_parts[i] if i < len(details_parts) else '').ljust(30)} | "
                  f"{(target_parts[i] if i < len(target_parts) else '').ljust(15)} | "
                  f"{(start_parts[i] if i < len(start_parts) else '').ljust(10)} | "
                  f"{(end_parts[i] if i < len(end_parts) else '').ljust(10)}")





    # لو عايز تعمل edit معقد .. غالبا هتحتاج setters




# Main function to run the console app
if __name__ == "__main__":
    next_id = User._User__generate_user_id()
    print(next_id)
    #هنا انت هتساله register ولا login
    # على حسب اللي هيختاره هتشغلله الفنكشن .. الاتنين بيرجعوا اوبجكت يوزر
    # فمثلا
    # user = login()
    # بعد كدا هتساله بقى على باقي الخيارات .. فمثلا اختار ديليت بروجكت
    # user.delete_project()

    pass
