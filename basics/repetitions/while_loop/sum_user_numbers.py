# ask user for how many numbers to add up
print("How many numbers should I sum up?")
number_to_sum = int(input())

# declare a control variable
summed = 1
print()
# diplay blank line

# sum numbers
total = 0

while (summed <= number_to_sum):
  print("Please enter number", summed, "of", number_to_sum, ":" )
  number = int(input())
  total = total + number
  summed = summed +1

# display result
print("\nThe answer is {}.".format(total))