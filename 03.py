# Taking input from user

age = input("Age: ")
print(age)

#Concatination

boy_name = input("Boy Name : ")
girl_name = input("Girl Name : ")
print(boy_name + " meets " + girl_name)

#Formated string

boy_name = input("Boy Name : ")
boy_age = int(input("Boy age : "))
girl_name = input("Girl Name : ")
girl_age = int(input("Girl age : "))
age_diff = abs(boy_age - girl_age)
print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")
print(boy_name + " meets " + girl_name + ". Age Difference is " + str(age_diff))
