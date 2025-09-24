# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class (Inheritance)


class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")

    def charge(self):
        print(f"🔋 Charging {self.device_info()}... Battery at {self.battery}%")

    def __str__(self):
        return f"Smartphone({self.brand}, {self.model}, {self.storage}GB, {self.battery}% battery)"


# Create objects
phone1 = Smartphone("Apple", "iPhone 17 Pro", 256, 85)
phone2 = Smartphone("Samsung", "Galaxy S25", 512, 60)

# Test methods
print(phone1)
phone1.make_call("0790215069")
phone1.charge()

print(phone2)
phone2.make_call("07981670383")
phone2.charge()
