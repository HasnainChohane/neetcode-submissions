class Laptop:
    def __init__(self, brand, processor, ram, storage):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def show_specs(self):
        return f"Brand: {self.brand}, Processor: {self.processor}, RAM: {self.ram}, Storage: {self.storage}"
lap1 = Laptop("Dell", "Intel Core i7", "16GB", "512GB SSD")
lap2 = Laptop("Apple", "M3 Chip", "8GB", "256GB SSD")
lap3 = Laptop("Lenovo", "AMD Ryzen 7", "32GB", "1TB SSD")

# Displaying specs
print(lap1.show_specs())
print(lap2.show_specs())
print(lap3.show_specs())
