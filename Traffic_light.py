#input Traffic light color
Color = str(input("Enter light color : "))
if (Color == "red"):
    print("Stop")
elif(Color == "yellow"):
    print("Get ready")
elif(Color =="green"):
    print("go")
else:
    print("Invalid color")