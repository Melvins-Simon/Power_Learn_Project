# Base class
class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life  # Battery life in hours
        self.is_on = False  # Default state is off

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def get_info(self):
        return f"📱 {self.brand} {self.model} - ${self.price}, Battery: {self.battery_life} hrs"

# Derived class with additional features
class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, battery_life, camera_megapixels):
        super().__init__(brand, model, price, battery_life)
        self.camera_megapixels = camera_megapixels  # Additional attribute

    def take_photo(self):
        if self.is_on:
            print(f"📸 Taking a photo with {self.camera_megapixels}MP camera on {self.brand} {self.model}.")
        else:
            print(f"⚠️ Cannot take a photo, {self.brand} {self.model} is OFF.")

    def get_info(self):
        return super().get_info() + f", Camera: {self.camera_megapixels}MP"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S23", 999, 24)
phone2 = SmartPhoneWithCamera("Apple", "iPhone 15", 1099, 20, 48)

print(phone1.get_info())  # Basic smartphone info
print(phone2.get_info())  # Smartphone with camera info

phone2.power_on()
phone2.take_photo()
phone2.power_off()
