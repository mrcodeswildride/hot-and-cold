import random

print()

number = random.randint(1, 100)

game_over = False
num_guesses = 0

while not game_over:
  guess = int(input("Guess a number between 1 and 100: "))
  num_guesses = num_guesses + 1
  diff = abs(number - guess)

  if diff == 0:
    game_over = True

    if num_guesses == 1:
      print("Wow, first try!")
    else:
      print(f"Congratulations, you won in {num_guesses} guesses!")
  elif diff == 1:
    print("On Fire!\n")
  elif diff < 5:
    print("Hot\n")
  elif diff < 15:
    print("Warm\n")
  elif diff < 25:
    print("Cool\n")
  elif diff < 50:
    print("Cold\n")
  else:
    print("Freezing!\n")
