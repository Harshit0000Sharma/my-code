class Restaurant():
    def __init__(self,name,cuisene_type):
        self.name=name
        self.cuisene_type=cuisene_type

    def describe_restaurant(self):
        service=(f"{self.name} serves wonderful{self.cuisene_type}")
        print(f"\n{service}")
    
    def open_restaurant(self):
        service2=(f"{self.name} is open. you can come anytime")
        print(f"\n{service2}")

dominoes=Restaurant("dominoes","pizza")
dominoes.describe_restaurant()

pizza_hut=Restaurant("pizza_hut","pizza")
pizza_hut.describe_restaurant()

mc_donalds=Restaurant("mc_donalds","burger")
mc_donalds.describe_restaurant()