"""
List Manipulation Exercise:
Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.
"""

"""
everse and Sort a List: Create a list of numbers and:

Sort it in descending order.
Reverse the sorted list and print it.
"""


items = ["apple", "banana", "mango", "grapes", "orange"]
print("Original list:", items)
items.append("pineapple")
print("After adding item at end:", items)
items.insert(1, "cherry")
print("After adding item at second position:", items)
items.pop(2)
print("After removing third item:", items)
numbers = [5, 2, 9, 1, 7]
numbers.sort(reverse=True)
print("Sorted in descending order:", numbers)
numbers.reverse()
print("Reversed list:", numbers)