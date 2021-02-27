# display message
print("Program Started!")

# ask user for an ascii code
print("\nPlease enter an ASCII code:")
code = int(input())

# chech code range
if code in range(32, 127, 1):
  print("\nThe character represented by the ASCII code {} is {}.".format(code, chr(code)))
else:
  print("\nASCII code not found.")

# display end message
print("\nProgram Ended!")