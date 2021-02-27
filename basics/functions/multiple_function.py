# function display_ladder with 1 parameter
def display_ladder(steps):
  # display each spet
  for step in range(steps):
    print("|  |\n****")

  # display botoom of ladder
  print("|  |")

# function create_ladder
def create_ladder():
  print("How many steps remain?")
  steps = int(input())
  display_ladder(steps)

create_ladder()