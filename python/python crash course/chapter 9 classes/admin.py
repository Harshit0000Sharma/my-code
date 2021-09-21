class User :
    def __init__(self,first_name,last_name,gmail,user_name,location):
        self.first_name=first_name.title()
        self.last_name=last_name.title()
        self.gmail=gmail
        self.user_name=user_name
        self.location=location.title()
    
    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"username: {self.user_name}")
        print(f"gmail:{self.gmail}")
        print(f"location:{self.location}")

    def greet_user(self):
        print(f"hello,welcome back {self.user_name}")

harshit=User("harsh","sharma","h@gmail.com","h@sharma","meerut")
harshit.describe_user()
harshit.greet_user()

khushi=User("khushi","sharma","k@gmail.com","k@sharma","meerut")
khushi.describe_user()
khushi.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name, gmail, user_name, location):
        super().__init__(first_name, last_name, gmail, user_name, location)
        self.privileges=[]

    def show_privilegs(self):
        print("privilegs for admin are:")
        for privilege in self.privileges:
            print("-"+ privilege)

harshit=Admin("harsh","sharma","h@gmail.com","h@sharma","meerut")
harshit.describe_user()

harshit.privileges=[
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

harshit.show_privilegs()