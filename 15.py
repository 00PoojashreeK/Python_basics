"""Basic Counting with while Loop:
Write a program that counts from 1 to 10 using a while
"""
i = 1
while i<=10:
    print(i)
    i = i + 1

# TO print odd and even numbers
a = 1
while a<=20:
    print(a)
    a = a + 2
b = 0
while b<=20:
    print(b)
    b = b + 2

"""
Ticket Booking Simulation:
Write a program that simulates a bus ticket booking system. 
The bus has 8 seats. Each time a seat is booked, the available seats decrease. 
When there are no seats left, the loop stops and displays a message saying "All seats are booked.
"""
seats = 8
while seats > 0 :
    print("Available seats : ", seats)
    book = input("Do you want to book a seat? [Yes/No]:")
    if book == "yes":
        seatsb = seats - 1
        print("Seat booked successfully!\n")
    else:
        print("Booking stopped.")
        break
if seats == 0:
    print("All seats are booked.")


"""
Countdown Timer:
Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" 
after the countdown is over.
"""
count = 10
while count >= 1:
    print(count)
    count = count - 1
print("Happy New Year!!")