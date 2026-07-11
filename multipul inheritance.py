class Camera:
    def capture_photo(self):
        print("Taking a photo")

class Phone:
    def make_call(self):
        print("Making a call")

class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the web")

# Creating an object
my_phone = Smartphone()
my_phone.capture_photo()
my_phone.make_call()
my_phone.browse_internet()
