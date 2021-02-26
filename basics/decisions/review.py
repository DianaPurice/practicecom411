# review bit
# beep wants to go for a trip
print("How is the weather?")
weather = input()
if ((weather == "sunny") or (weather == "nice") or (weather == "warm")):
  print("That's great.I will go for a trip. \nBut where should I go? Perhaps to the...")
  trip = input()
  if (trip == "sea"):
    print("Great ideea! I will go to the {}. ".format(trip))
    print("...Finaly I arrived at the {}. Now what should I do?".format(trip))
    sea1 = input()
    sea2 = input()
    if (((sea1 == "swim") or (sea1 == "sunbathe")) and (sea2 == "swim") or (sea2 == "sunbathe")):
      print("What a wonderfull ideea. I will {} ".format(sea1) +  "and then I will {}." .format(sea2))
    else:
      print("This would take to long and is almost down. I will go for a short walk and than to sleep.")
    
  elif (trip == "lake"):
    print("Great ideea! I will go to the {}. ".format(trip))
    print("...Finaly I arrived at the {}. Now what should I do first?".format(trip))
    lake1 = input()
    lake2 = input()
    if (((lake1 == "fish") or (sea1 == "ride a boat")) and (lake2 == "fish") or (sea2 == "ride a boat")):
      print("What a wonderfull ideea. I will {} ".format(lake1) + "and then I will {}".format(lake2))
    else:
      print("This would take to long and is almost down. I will go for a short walk and than to sleep.")
  else:
    print("Great ideea! I will go to the {}. ".format(trip))
    print("...Finaly I arrived at the {}. It took a long time to get here and I am tiered. I will go and rest first.".format(trip))
else:
  print("I was thinking about going for a trip but the weater is not nice so I will stay home and study instead.")