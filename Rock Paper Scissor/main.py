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


def user_input():
    user_choice = input("Enter your choice: ").lower().strip()
    if user_choice not in choices:
        print("Please only choose from the Available choices!")
        user_input()
    return user_choice


def get_winner(user, comp):

    if user == 'rock':
        if comp == 'paper':
            return 'Computer'
        elif comp == 'scissors':
            return 'user'
    elif user == 'paper':
        if comp == 'rock':
            return 'Computer'
        elif comp == 'scissors':
            return 'user'
    elif user == 'scissors':
        if comp == 'rock':
            return 'Computer'
        elif comp == 'paper':
            return 'user'
    

def exit_game():
    choice = input("Do You wanna keep playing? (y/n): ")
    if choice == 'n':
        print("Exiting game...")
        return False
    else: return True


def play():
    
    running = True

    while running:
        print('Round begins!')
        user_choice = user_input()
        comp_choice = random.choice(choices)
        print("Computer chooses:", comp_choice)
        if user_choice == comp_choice:
            print("Tie")
            running = exit_game()
        else:
            winner = get_winner(user= user_choice, comp=comp_choice)
            print("Winner:", winner)
            running = exit_game()


def display_score():
    
    print(f'Player: {user_score} | Computer: {comp_score}')


def display_menu():

    running = True

    while running:
        print("1) Play\n2) Score\n3)Exit")

        def choose():
            choice = input("Enter your option: ")
            if choice == '1': play()
            elif choice == '2': display_score()
            elif choice == '3': running = False
            else:
                print("Invalid Option!!!")
                choose()

        choose()


def main():
    display_menu()


if __name__ == '__main__':
    main()