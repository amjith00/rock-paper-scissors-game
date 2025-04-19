import random
user = int(input("enter your number : 0for raock 1for paper 2for scissors"))
computer = random.randint(0,2)

if user == computer:
  print("draw")
elif user > computer:
  print("you lose")
elif user < computer:
  print("you win")
elif user == 2 and computer == 0:
  print("you lose")
elif user == 0 and computer == 2:
  pirnt("you win")


print("Game over")