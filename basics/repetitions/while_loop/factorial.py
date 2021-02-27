# ask user for number
print("Please enter a number:")
number = int(input())

# calculating the factorial of user input
count = 0
total = 1

while ( count < number ):
  count = count + 1
  total = total * count

# display result
print("The factorial is", total)