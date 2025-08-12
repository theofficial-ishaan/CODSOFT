#  User Input: Prompt the user to choose rock, paper, or scissors.
#  Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
#  Game Logic: Determine the winner based on the user's choice and the computer's choice.
#  Rock beats scissors, scissors beat paper, and paper beats rock.
#  Display Result: Show the user's choice and the computer's choice.
#  Display the result, whether the user wins, loses, or it's a tie.
#  Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
#  Play Again: Ask the user if they want to play another round.
#  User Interface: Design a user-friendly interface with clear instructions and feedback

import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
comp_score = 0
tie = 0

 
def user_input():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
        if user_choice in choices:
            return user_choice
        print("Please only choose from the Available choices!")


def get_winner(user, comp):

    if user == 'rock':
        if comp == 'paper': return 'Computer'
        elif comp == 'scissors': return 'User'
    elif user == 'paper':
        if comp == 'rock': return 'User'
        elif comp == 'scissors': return 'Computer'
    elif user == 'scissors':
        if comp == 'rock': return 'Computer'
        elif comp == 'paper': return 'User'
    

def exit_game():
    choice = input("Do You wanna keep playing? (y/n): ")
    if choice == 'y': 
        return True
    elif choice == 'n':
        print("Exiting match!!...")
        return False


def play():
    
    running = True

    while running:
        global user_score, comp_score, tie

        print('Round begins!')
        user_choice = user_input()
        comp_choice = random.choice(choices)
        print("Computer chooses:", comp_choice)
        if user_choice == comp_choice:
            tie += 1
            print("It's a Tie")
            running = exit_game()
        else:
            winner = get_winner(user= user_choice, comp=comp_choice)
            if winner == 'User': 
                user_score += 1
                print("You Win! ")
            elif winner == 'Computer': 
                comp_score += 1
                print("You Lose :( ")
            running = exit_game()


def display_score():
    print(f'==================================\nPlayer: {user_score} | Computer: {comp_score} | Ties: {tie}\n==================================')


def choose_option():
  return input("Enter your option (1,2,3): ")


def main_menu():

    print("==================================\n=======ROCK PAPER SCISSORS!=======\n==================================")
    running = True

    while running:
        print("1) Play\n2) Score\n3) Exit")

        choice = choose_option()
        if choice == '1': play()
        elif choice == '2': display_score()
        elif choice == '3': 
            print("Thanks for playing!!!")
            running = False
        else:
            print("Invalid Option!!!")


if __name__ == '__main__':
    main_menu()