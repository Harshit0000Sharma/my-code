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
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()