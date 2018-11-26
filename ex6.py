Name = input("What is your name?")
Age = input("What is your age?")
Height = input("What is your height in inches?")
Weight = input("What is your weight in pounds?")
EyeColour = input("What is your eye colour?")
HairColour = input("What is your hair colour?")

if Age >= str(46):
  print("You're older than most")
elif Age <= str(45):
  print("You're younger than most")
else:
  print("Invalid input")

if Height > str(69):
  print("You're above average height for an adult male")
elif Height == str(69):
  print("You are the average height for an adult male")
elif Height < str(69):
  print("You are below average height for an adult male")
else:
  print("Invalid input")

if Weight < str(185):
  print("You're weight is above average")
elif Weight == str(185):
  print("You are the average weight")
elif Weight > str(185):
  print("You weight is below average")
else:
  print("Invalid input")