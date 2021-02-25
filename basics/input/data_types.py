# ask for user data
print("What is your name human?")
# read user's response
name = input() 
print("How old are you (in years?)")
age = int(input())
print("How tall are you (in meters)?")
height = float(input())
print("How much you weigh (in kilograms)?")
weigh = float(input())
# calculate bmi
bmi = weigh / (height ** 2)
# offer answer to user
print(name,  "you are",  age, " years old and your bmi is {:.2f}".format(bmi))