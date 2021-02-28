# display box funtion
def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("|  {}  |".format(word))
    print("-" * num_dashes)

# display lower case funtion
def lower_case(word):
    print(word.lower())

# display upper case funtion
def upper_case(word):
    print(word.upper())

# display mirrored function
def mirrored(word):
    m = ""
    for letter in reversed(word):
      m += letter
    print("{} | {}".format(word, m))

# repeat filter
def repeat(word):
    print("How many times should i be displaying?")
    reps = int(input())
    for rep in range(reps):
      # even
      if (rep % 2 == 0):
        print(lower_case(word))
      else:
        print(upper_case(word))

# run function
def run():
    # ask for a word
    print("Please enter a word:")
    word = input()

    # create variable for the user answer
    answer = 0

    while (answer != 6):
      # get user option
      print("What would you like to do with this word?")
      print("[1] Display in a box")
      print("[2] Display lower-case")
      print("[3] Display upper-case")
      print("[4] Display mirrored")
      print("[5] Display repeated")
      print("[6] Quit")

      answer = int(input())

      # determinate and execute action
      if (answer == 1):
        display_box(word)
      elif (answer == 2):
        lower_case(word)
      elif(answer == 3):
        upper_case(word)
      elif (answer == 4):
        mirrored(word)
      elif (answer == 5):
        repeat(word)
      elif (answer == 6):
        break
      else:
        print("Unkown option.")

run()