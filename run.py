import random

print("Want to play?")
play_game = input("Can you step up? (yes/no): ").lower()

if play_game == 'yes':
    print("please enter your name: ")
    name = input()
    print("Please can " + name + " enter the country they represent: ")
    nationality = input()
    print("We have " + name + " from " + nationality + " stepping up for their nation!")
    print("You have 5 shots, you need to score 3 or more to bring home the World Cup")
    print("However if the computer saves 3 or more you let your country down!")
    print("You will pick a number between 1-5, if you and the computer pick different numbers you score")
    print("If you and the computer match numbers then the computer makes the save!")



    player_goals = 0
    computer_saves = 0


def game():
    global player_goals, computer_saves

    player_choice = input("Choose either '1', '2', '3', '4', '5'")

    player_choice = int(player_choice)

    if player_choice not in [1,2,3,4,5]:
        print("You need to enter either '1', '2', '3', '4', '5' in order to play!")

    return game()

    computer_choice = random.choice([1,2,3,4,5])

    print(f + name + "goes {player_choice}, computer has gone {computer_choice}")

if __name__ == "__main__":
    start_game()

else:
    print("Okay")