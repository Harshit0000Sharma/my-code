class User :
    def __init__(self,first_name,last_name,gmail,user_name,location):
        self.first_name=first_name.title()
        self.last_name=last_name.title()
        self.gmail=gmail
        self.user_name=user_name
        self.location=location.title()
        self.login_attempts=0
    
    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"username: {self.user_name}")
        print(f"gmail:{self.gmail}")
        print(f"location:{self.location}")

    def greet_user(self):
        print(f"hello,welcome back {self.user_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

harshit=User("harsh","sharma","h@gmail.com","h@sharma","meerut")
harshit.describe_user()
harshit.greet_user()

khushi=User("khushi","sharma","k@gmail.com","k@sharma","meerut")
khushi.describe_user()
khushi.greet_user()

print("\nMaking 3 login attempts...")
harshit.increment_login_attempts()
harshit.increment_login_attempts()
harshit.increment_login_attempts()
print("  Login attempts: " + str(harshit.login_attempts))

print("Resetting login attempts...")
harshit.reset_login_attempts()
print("  Login attempts: " + str(harshit.login_attempts))