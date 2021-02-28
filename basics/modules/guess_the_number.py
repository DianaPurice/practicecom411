# import random
import random

def play_guess_the_number():

  # retrive user data
  print("Please enter the minimum value:")
  minimum_value = int(input())

  print("\nPlease enter the maximum value:")
  maximum_value = int(input())

  random_number = random.randrange(minimum_value, maximum_value, 1)


  print("I am thinking of a number between {} and {}.\nCan you guess what it is?".format(minimum_value, maximum_value))

  guess = 0
  while (guess != random_number):
    print("Please enter a number:")
    guess = int(input())

    if (guess == random_number):
      print("Congratulations! You guessed my number!")

    elif(guess < random_number):
      print("Your guess is too low.\nTry again.")

    elif(guess > random_number):
      print("Your guess is too high.\nTry again.")

play_guess_the_number()
