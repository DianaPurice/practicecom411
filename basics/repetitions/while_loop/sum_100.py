# display message
print("Calculating the sum of the first 100 numbers...")

#declare a control variable
number = 1

# calculate the sum of the first 100 numbers
total = 0

while (number <= 100):
  total = total + number
  number = number + 1

#display result
print("...Done! The answer is {}".format(total))