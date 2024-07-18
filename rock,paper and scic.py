import random
comp= random.randint(1,3)



option={ 1:"rock" ,2:"scissors", 3:"paper"}


welcome=input("enter your username: ")
print(f"welcome {welcome} ")

user=int(input("1 for rock,2 for scissors,and 3 for paper ;"))
#ERROR HANDLING WILL GO HERE
print(f"Computer chose {option[comp]}")
print(f"User chose {option[user]}")

if user==comp:
    print("draw")
elif user==1 and comp==2:
    print("user win")
elif user==2 and comp==3:
    print(" user win")
elif user==3 and comp==1:
    print(" user win")

else:
    print("computer won")

print("thankyou for playing")

