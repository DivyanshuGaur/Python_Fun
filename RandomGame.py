
import random


def game():
    computer_no=random.randint(1,50)
    print('WELCOME TO RANDOM GAME ')
    c=0
    while(1):
           user_no=int(input("GUESS NUMBER  \n"))

           if(user_no == computer_no):
               print("You Guessed it Right  ")
               break
           if(user_no > computer_no):
               print('Try Lesser Number  ')
           if(user_no < computer_no):
               print('Try Greater Number   ')
           c+=1

           if(c==5):
               print('Sorry , You Loose ')
               break
           print('Your Limit is ' , 5-c)

    choice = input("Play Again \n")

    if(choice == "yes"):
        game()


game()