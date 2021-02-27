# fuction climb ladder with 2 parameters
print("how many steps have we crossed?")
steps_crossed = int(input())
print("\nhow many steps remain?")
steps_remaining = int(input())

def climb_ladder(steps_remaining, steps_crossed):
  if (steps_remaining > steps_crossed):
    print("\nStill some way to go!")
  else:
    print("\nWe are almost there!")

# calls function
climb_ladder(steps_remaining, steps_crossed)
