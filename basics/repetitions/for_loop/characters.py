# ask user for characters
print("What strange markings do you see?")
characters = input()

# display position
print("\nIdentifying...\n")

for character in range(0, len(characters), 1):
  print("Index", character, ":", characters[character])
print("\nDone!")