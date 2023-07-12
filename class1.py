X = int(input("Choose a number from 1 to 5: "))

import random
R = random.randrange(1, 6)


if X == R: 
  print("wow! good job")

else: 
  print("Try again!")

