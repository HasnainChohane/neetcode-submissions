#Create tuple for Karachi coordinates
location = (24.8607, 67.0011)
#Get latitude - index 0
latitude = location[0]
print("Latitude:", latitude)
#Get longitude - index 1
longitude = location[1]
print("Longitude:", longitude)
# Count dimensions using len()
total_items = len(location)
print("Total dimensions in tuple:", total_items)