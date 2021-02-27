# display message
print("Program Started!")
print("\nPlease enter a standard character:")
ch = input()

if(len(ch) == 1):
  print("The ascii code for {} is {}.".format(ch, ord(ch)))
else:
  print("\nA single character was expected.")

print("\nProgram Ended!")