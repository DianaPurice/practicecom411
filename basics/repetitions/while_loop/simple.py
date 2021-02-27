# ask user how many cables to remove
print("How many cables should I remove?")
cables_to_remove = int(input())

# declare a control variable
cables_removed = 0

# remove cables
print()

while (cables_removed < cables_to_remove):
  print("""...
Removed cable.""")
  cables_removed += 1