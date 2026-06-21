import random 

num = random.randint(1,9)
reward  = 40 
chance =4
a = 1
while a <=  chance:
    ch = int(input("Guess the Number: "))
    if num == ch:
        print("Your Guess is Correct you won Reward: ",reward)
        break
    else:
        if a ==3:
            print("This is you last chance for Guessing so please think Calmly...")
        a +=1
        reward -=10
        print("Your Guess is wrong please Try again....")
else:
    print("Sorry You Lost..")
