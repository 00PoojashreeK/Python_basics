#Dictionaries
birthday = {
    "pooja" : "21-10-2006",
    "neha" : "25-10-2006",
    "thrisha" : "28-12-2005"
}
birthday["sudeep"] = "02-09-1973" #adding an extra element to the list.
print(birthday)
print(type(birthday))
print("Updating...") # To update 
birthday["pooja"] = "21-10-2026"

x = birthday.pop("thrisha") #To remove an element 
print(x) #only key will delete not value

print(birthday)
print(birthday.keys())
print(birthday.values())
print(birthday.items()) # key value pairs will be given in the form of tuples
new_dict = {"amrutha": "raksha"}
birthday.update(new_dict)
print(birthday) # To update the dictionary

meaning = {
    "bat" : "used to hit",
    "ball" : "this is hit",
    "wicket" : "to be hit"
}
print(meaning)

karnataka_food = {
    "Bengaluru" : "Bisi bele bath",
    "Mysuru" : "Mysore pak",
    "Mangaluru" : "Neer dose"
}

#Accessing dictionary elements
print(karnataka_food["Mysuru"]) 
print(birthday["pooja"])
print(birthday.get("neha", "Not found"))
print(birthday.get("sudeep", "Not found")) #Safe access

d = {
    "str" : "str",
    "st" : 123,
    "f" : 10.12,
    "is" : True,
    (1) : "dtfysg",
    12 : 123,
    "friends" : [1,2,3,4]
}
print(d)

#to create a structured dictionary
item1 = {
    "name" : "milk",
    "weight" : 1,
    "price" : 50
}
item2 = {
    "name" : "sugar",
    "weight" : 2,
    "price" : 100
}
items = [item1 , item2, ]
print(items)
print(f"Total Weight : {item1["weight"] + item2["weight"]}kg")