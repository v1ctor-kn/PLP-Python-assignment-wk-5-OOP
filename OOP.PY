class Smartphone:
    pass
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def specs(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

phone1 = Smartphone("Samsung", "Galaxy A14", 128)
phone2 = Smartphone("Apple", "iPhone 13", 256)

print(phone1.specs())  # Samsung Galaxy A14 with 128GB storage
print(phone2.specs())  # Apple iPhone 13 with 256GB storage

class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def specs(self):
        base = super().specs()
        return f"{base}, Camera: {self.camera_megapixels}MP"
    
SmartphoneWithCamera("Google", "Pixel 6", 128, 50)
phone3 = SmartphoneWithCamera("Google", "Pixel 6", 128, 50)
print(phone3.specs())  # Google Pixel 6 with 128GB storage, Camera: 50MP
 