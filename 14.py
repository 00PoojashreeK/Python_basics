#While loop
is_failed = True
i = 1 #attempt
while is_failed and i<=100 :
    if i % 2 != 0: # is not even
        i = i + 1
        continue # next written code will not run
    print(f"Try {i}")
    i = i + 1
    if i > 100:
        break
print("I gave up!!")

# Nested while loops
a = 0
while a <= 10:
    x = 0
    while x<a :
        print("Pooja", end ="-")
        x = x + 1
    print("-")
    print(a)
    a = a + 1 # or a += 1

#Taking user input and print ATM
pin = "1234"
trials = 0
while trials<=3:
    input_pin = input("Trial-{trials} | PIN >> ")
    trials = trials + 1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
