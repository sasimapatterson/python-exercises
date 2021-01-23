#Write a Python program to guess a number between 1 to 9.
import random

user_choice = int(input("Guess the number between 1 to 9: "))

if user_choice > 9 or user_choice < 1:
    print("Please enter number between 1 to 9 only")
else:
    computer_choice = random.randint(1, 9)
    print(f"The number is: {computer_choice}")
    
    
    if user_choice == computer_choice:
        print("Well guessed!")
    else:
        print("Try again!")
        
#Keep working on this to make the program keeps prompting the user for new number.