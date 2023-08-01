print("+++++++ ------------------- ++++++++++")
print("+++++++ WELCOME IN THE GAME ++++++++++")

import random 

print("select 1 for ROCK")
print("                ___-___                      ")
print("              _/       \                  ")
print("             /_________-_ \           ")
print("                                             ")
print("select 2 for PAPER") 
print("       _____________                  ")
print("      |             |                    ")
print("      |             |                   ")
print("      |_____________|                   ")
print("select 3 for SCISSOR")
print("    _                         ")
print("   /  \   /                        ")
print("  |____\ /                       ")
print("   ____ X                      ")
print("  |    / \                        ")
print("   \__/   \                    ")
user=int(input("ENTER YOUR CHOICE \n"))
comp=random.randint(1,3)

def displayuser():
    if (0<user<4):
        if(user==1):
            print("USER=ROCK")
        elif(user==2):
            print("USER=PAPER")    
        elif(user==3):
            print("USER=SCISSOR")
    else:
        print("INVAILD INPUT")
        
        
def displaycomp():
    if(comp==1):
        print("COMP=ROCK")
    elif(comp==2):
        print("COMP=PAPER")    
    elif(comp==3):
        print("COMP=SCISSOR")

displayuser()
displaycomp()

if(user>comp):
    print("USER WINS")
elif(user==comp):
    print("DRAW")
elif(comp==3):
    print("USER WINS")
else:
    print("COMP WINS")