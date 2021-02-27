# ask user for number of bars
print("How many bars should be charged?")
bars = int(input())

# create variable to track number of bars charger
bars_charged = 0

# use while loop 
while (bars_charged < bars):
  bars_charged = bars_charged + 1
  print("Charging:", "■ " * bars_charged)

# display final message
print("\nThe battery is fully charged.")