"""
Tuple Operations: Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements. 
Concatenate the tuple with another tuple.
"""
t = (10, 20, 30, 40, 50)
print("Original tuples : ", t)
slice_tuple = t[1:3]
t2 = (60, 70)
new_tuple = t + t2
print("Concatenated tuple is : ", new_tuple)


"""
Set Operations:
Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
"""
my_fruits = {"mango", "apple", "banana", "kiwi"}
friends_fruits = {"grapes", "mango", "apple", "orange"}
print("My favroite fruits : ", my_fruits )
print("My friends favroite fruits : ", friends_fruits)
print("Union : ", my_fruits.union(friends_fruits))
print("Intersection : ", my_fruits.intersection(friends_fruits))
print("Difference of my and my friends favroite fruits : ", my_fruits.difference(friends_fruits))
my_fruits.add("papaya")
print("Adding new fruits : ", my_fruits)
my_fruits.remove("apple")
print("Removing a fruit : ", my_fruits)
my_fruits.discard("banana")
print("Discarding a fruit : ", my_fruits)

"""
Tuple and Set Comparison:
Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?
"""
elements = [10, 20, 30, 40, 50]
t = tuple(elements)
s = set(elements)
print("Tuples : ", t)
print("Sets : ", s)