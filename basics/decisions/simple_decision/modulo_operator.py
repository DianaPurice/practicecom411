# ask user to enter a whole number
print("Please enter a whole number.")
number = int(input())

#determintae if is an even number
if (number % 2 == 0): print("\nThe number {} is an even number.".format(number))
else: print("\nThe number {} is an odd number.".format(number))