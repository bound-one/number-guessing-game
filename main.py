import random
print("welcome")
print("rules /The computer randomly select a number between 1 and 100.")
print("you need to guess the number")
diff = int(input("select a diffculty "/ "1 = easy" /"2= mid" /"3=hard"))
if diff =  1:
  chance = 10
elif diff = 2:
  chance= 5  
else diff = 3:
  chance= 3
while chance > 0 :
  no = random.randint(1, 100)
  guess = int(input(your guess))
  if no = guess :
    print ("you win")
  else no > guess:
    print("greater")
  else no < guess:
    print("less")  
  chance = chance - 1



  
