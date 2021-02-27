# as user for brightness level
print("What level of brightness is required?")
br_desired = int(input())

#adjust brightness
print("\nAdjusting brightness...\n")

for br in range(2, br_desired + 1, 2):
  print("Beep's brightness level:", "*" * br)
  print("Bop's brightness level:", "*" * br)

print("\nAdjusments complete!")