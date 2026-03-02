#Lists
item1 = "Bru"
item2 = "Sugar"
item3 = "Milk"
print(item1, item2, item3)

items = ["Bru", "Sugar", "Milk", "Bru"]
items.pop() # to remove last element
items.pop(0) # to remove specific element
items.append("Oreo") #To add an element at last
items.remove("Sugar") #TO remove an element
items.insert(1, "Spoon")# To add an element in the specific position
items[0] = "Coffee_Powder"
items.clear() # to remove all elements from the list
print(items)

l = ["Bru", 1, 0.8, 'C', "True"]
print(l[2])

# Slicing the list.
list = ['a', 'b', 'c', 'd', 'e']
print(list)
print(list[1])
print(list[0:3:1])
print(list[0:2])
print(list[1:])
print(list[0: :2])

#Copy lust to l2.
l2 = list[0:3]
print(l2)

#Functions of list.
print(len(list))

l1 = [1, 23, 24, 56, 22, 63]
print(sorted(l1)) #sorted
print(sum(l1)) #sum
print(l1.index(23)) #index

#To print sorted list or inplace operator
sorted_items = sorted(l1)
rev = sorted_items.reverse()
print(sorted_items)
l1.sort()
print(l1)

#Matrix
m = [[1, 2], [3, 4], [4, 5]]
print(m[0] [1]) # to print 2
print(m[1] [1]) # to print 4
print(m[2] [0]) # to print 4
print(m) # nesting
print(type(m))