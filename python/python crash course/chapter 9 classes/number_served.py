class Restaurant():
    def __init__(self,name,cuisene_type):
        self.name=name
        self.cuisene_type=cuisene_type
        self.number_served=0

    def describe_restaurant(self):
        service=(f"{self.name} serves wonderful {self.cuisene_type}")
        print(f"\n{service}")
    
    def open_restaurant(self):
        service2=(f"{self.name} is open. you can come anytime")
        print(f"\n{service2}")

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant=Restaurant("dominoes","pizza")
print(restaurant.name)
print(restaurant.cuisene_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))