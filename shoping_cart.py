#My Shoping Cart _ list Operations
#creat empty list
cart=[]
#add 5 grocery items using append()
cart.append("milk")
cart.append("bread")
cart.append("eggs")
cart.append("rice")
cart.append("sugar")
#show cart to user
print("Your Cart : ",cart)
#Remove 1 item
item_remove= input("Enter item to remove :")
cart.remove(item_remove)
print("After removing: ",cart)
#update 1 item 

old_item = input("Enter item to replace : ")
new_item = input ("Enter new item: ")
#find index of old item
index = cart.index(old_item)
cart[index]= new_item

print ("Final cart : " , cart)