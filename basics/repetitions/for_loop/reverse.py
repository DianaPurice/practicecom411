# ask user
print("What phrase do you see?")
phrase = input()
print()
# reverse phrase 
print("Reversing...\n\nThe phrase is: ", end="")

# displaying result
for p in range(len(phrase) -1, -1, -1):
  print(phrase[p], end="")
  