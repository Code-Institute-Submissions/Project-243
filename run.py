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

    player_choice = input("Choose either '1', '2', '3', '4', '5': ")

    player_choice = int(player_choice)

    if player_choice not in [1,2,3,4,5]:
        print("You need to enter either '1', '2', '3', '4', '5' in order to play!")

    return game()

    computer_choice = random.choice([1,2,3,4,5])

    print(name + "goes {player_choice}, computer has gone {computer_choice}")

    if player_choice == computer_choice:
        computer_saves += 1
        print("save")
    else:
        player_goals +=1
        print("goal")
    return player_goals, computer_saves

def play_rounds(rounds):
    player_total_goals = 0
    computer_total_saves = 0

    for _ in range(rounds):
        player_goals, computer_saves = game()

        player_total_goals += player_goals
        computer_total_saves += computer_saves
        print(f"Total goals scored: {player_total_goals}")
        print(f"Total saves made: {computer_total_saves}")

if __name__ == "__main__":
    player_goals = 0
    computer_saves = 0
    game()

    for _ in range(5):
        game()

    if player_goals >= 3 or computer_saves >= 3:
        print("That's all they needed!")
        if player_goals >= 3:
            print(name + "has won it for" + nationality)
        else:
            print("Computer wins")
    else:
        game()

else:
    print("Okay")