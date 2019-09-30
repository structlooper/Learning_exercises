class Laptop:
    disscount_percent = 10
    count_object = 0 #class_variable
    def __init__(self,brand_name,model_number,price):
        Laptop.count_object += 1
        self.brand_name = brand_name
        self.model_number = model_number  
        self.price = price
        self.full_name = brand_name + " " + model_number
    @classmethod
    def from_string(cls,string):
        brand,model,price = string.split(",")
        return cls(brand,model,int(price))

    def apply_disscount(self):
        off_price = ((self.disscount_percent/100)*self.price)
        return f"new price of {self.full_name} is {self.price - off_price} by appling {self.disscount_percent}%"

    
    
laptop1 = Laptop("compaq","CQ57", 20000)
laptop2 = Laptop('hp','IEF57', 48000)
Laptop.disscount_percent = 20

# print(laptop1.brand_name,laptop1.price)
# print(laptop1.apply_disscount())
# print(Laptop.count_object)

laptop3 = Laptop.from_string(input("Enter the brand_name model_no and price of Laptop : "))
print(laptop3.apply_disscount())