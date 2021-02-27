# function cross_bridge
def cross_bridge(steps):
  # define each step
  for step in range(steps):
    print("Crossed step.")

  # display message
  if (steps > 5):
    print("The bridge is collapsing!")
  else:
    print("We must keep going!")

# call functions
cross_bridge(3)
cross_bridge(6)