# ask user for live cables to avoid
print("How many cables must I avoid?")
avoid_cables = int(input())

# create variable to track numbers of live cables
live_cables = 0

# display current count of live cables
while (live_cables < avoid_cables):
  print("Avoiding...", end="")
  live_cables = live_cables + 1
  print("Done! {} live cables avoided.".format(live_cables))
# diplay how many cables has been avoided
print("\n{} cables have been avoided. All live cables have been avoided.".format(live_cables))