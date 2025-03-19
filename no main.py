
import random
print("welcome")
print("rules /The computer randomly select a number between 1 and 100.")
print("you need to guess the number")
   
diff = int(input("Select a difficulty: 1 = easy, 2 = mid, 3 = hard: "))
chance= 0
if diff ==  1:
  chance = 10
elif diff == 2:
  chance= 5
elif diff == 3:
  chance= 3
else:
  print("enter a number between 1 and 3")
  exit()
print("you have" , chance )
while chance >= 0 :
  no = random.randint(1, 100)
  guess = int(input("your guess"))
  if no == guess :
    print ("you win")
  elif no > guess:
    print("greater")
  elif no < guess:
    print("less")
    
  else:
    print("enter a number ")  
  chance = chance - 1
  



  
