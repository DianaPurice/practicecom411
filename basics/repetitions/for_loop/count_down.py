# ask user for steps
print("How far are we from the cave?")
steps = int(input())

# display message
print()
for step in range(steps, 0, -1):
  print(step, "steps remaining")
print("\nWe have reached the cave!")