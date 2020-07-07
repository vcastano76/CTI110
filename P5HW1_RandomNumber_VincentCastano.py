# The program generates a random number from 1-100 and asks
# the user to guess the number. If the number is too high
# then the program states "too high, try again. If too low,
# "too low, try again. The user is prompted whether they want to play
# the game or exit.
# Created on July 7, 2020
# CTI-110 P5HW1 - Random Number
# Vincent Castano

from random import randint  #To generate a random number
def game():
    rand_number = randint(0,100)   #Generates a random number
    print("\nI have selected a number between 1 to 100...")
    print("You have 6 chances to guess that number...")
    i = 1
    r = 1
    while i<7:  #6 Chances to the user
        user_number = int(input('Enter your number: ')) 
        if user_number < rand_number:
            print("\nToo high, try again")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif user_number > rand_number:
            print("\nToo low, try again")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif user_number == rand_number:
            print("\nCongratulations!! You have guessed the correct number!")
            r = 0;
            break
        else:
            print("This is an invalid number. Please try again")
            print("you now have " + str(6-i)+ " chances left" )
            continue
    if r==1:
        print("Sorry you lost the game!!")
        print("My number was = " + str(rand_number))

def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break
main()
print("\nEnd of the Game! Thank you for playing!")
