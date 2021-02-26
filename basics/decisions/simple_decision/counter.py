# ask user for the numbers
print("Please enter the first whole number.")
n1 = int(input())
print("\nPlease neter the second number.")
n2 = int(input())
print("\nPlease enter the third number.")
n3 = int(input())
e_n = 0
o_n = 0
if (n1 % 2 == 0): e_n = e_n + 1
else: o_n = o_n + 1
if (n2 % 2 == 0): e_n = e_n + 1
else: o_n = o_n + 1
if (n3 % 2 == 0): e_n = e_n + 1
else: o_n = o_n + 1
print("\nThere were {} even and {} odd numbers.".format(e_n, o_n))