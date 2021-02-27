# ask user for rows
print("How many rows should I have?")
rows = int(input())

# ask user for columns
print("\nHow many columns shold I have?")
columns = int(input())

# display result using for
for row in range(0, rows, 1):
  for column in range(0, columns, 1):
    print(":-)", end="")
  print()
print("\nDone!")
