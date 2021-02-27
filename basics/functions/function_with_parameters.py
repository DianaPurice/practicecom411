# fuction climb ladder with 2 parameters
def climb_ladder(steps_remaining, steps_crossed):
  if (steps_remaining > steps_crossed):
    print("Still some way to go!")
  else:
    print("We are almost there!")

# calls function
climb_ladder(5, 2)
climb_ladder(2, 5)