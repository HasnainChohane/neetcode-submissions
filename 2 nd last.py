from abc import ABC, abstractmethod

# 2. Abstract Class
class Shape(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def calculate_area(self):
        pass

# 3. Child Classes
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width

# 4. Task Execution
if __name__ == "__main__":
    
    circle_obj = Circle("Circle", 5)          
    rectangle_obj = Rectangle("Rectangle", 10, 5) 

    # Printing results
    print(f"{circle_obj.name} Area: {circle_obj.calculate_area()}")
    print(f"{rectangle_obj.name} Area: {rectangle_obj.calculate_area()}")
