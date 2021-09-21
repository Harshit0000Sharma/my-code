class Restaurant():
    def __init__(self,name,cuisene_type):
        self.name=name
        self.cuisene_type=cuisene_type

    def describe_restaurant(self):
        service=(f"{self.name} serves wonderful {self.cuisene_type}")
        print(f"\n{service}")
    
    def open_restaurant(self):
        service2=(f"{self.name} is open. you can come anytime")
        print(f"\n{service2}")

dominoes=Restaurant("dominoes","pizza")
print(dominoes.name)
print(dominoes.cuisene_type)
dominoes.describe_restaurant()
dominoes.open_restaurant()