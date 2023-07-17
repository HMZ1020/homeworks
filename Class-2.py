Player_1= int(input("player 1 Choose a number from 1 to 5: "))

Player_2 = int(input("player 2 Choose a number from 1 to 5: "))


import random
R = random.randrange(1, 6)


if Player_1 == R:

  print("Player 1 win")

if Player_1 != R:
  print("player 1 lose")

if Player_2== R: 
  print("player 2 win")

if Player_2 != R:
  print("player 2 lose")



