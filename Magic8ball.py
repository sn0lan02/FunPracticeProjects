# This code will immitate a magic 8 ball
# this is a practice from codeacademy


import random

print("hello! Welcome to the magic 8 ball simulator, what is you're name?")
name = input("")

print("hello,", name, "the magical 8 ball knows the answer to all of yoor questions.")
question = input("what will you ask the magic 8 ball?: ")

print("magic 8 balls answer: ")
random_number = random.randint(1,9)


if random_number == 1:
  print("Yes - definitely")
elif random_number == 2:
  print("it is decidedly so")
elif random_number == 3:
  print("Without a doubt")
elif random_number == 4:
  print("Reply hazy, try again")
elif random_number == 5:
  print("Ask again later")
elif random_number == 6:
  print("Better not tell you now")
elif random_number == 7:
  print("My sources say no")
elif random_number == 8:
  print("Outlook not so good")
elif random_number == 9:
  print("Very doubtful")
else:
  random_number = "Error: Something went wrong :/"


