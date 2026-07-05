import random 
choices=["rock","paper","scissor"]
user_choice=input("choose rock,paper,scissor:").lower().strip()
computer_choice=random.choice(choices)
print("user choice:",user_choice)
print("computer choice:",computer_choice)
if user_choice == computer_choice:
    print("Draw")
elif  user_choice== "paper" and  computer_choice=="rock" :
    print("user wins")
elif  user_choice=="rock" and  computer_choice=="scissor" :
    print("user wins")
elif  user_choice=="scissor" and  computer_choice=="paper" :
    print("user wins")
else :
   print("computer wins")
