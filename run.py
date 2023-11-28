import random

print("Want to play?")
play_game = input("Can you step up? (yes/no): \n").lower()

if play_game == 'yes':
    print("please enter your name: \n")
    name = input()
    print("Please can " + name + " enter the country they represent: \n")
    nationality = input()
    print("We have " + name + " from " + nationality)
    print("Aim is to pick a number different to the computer to score. If you both match the computer saves,")
    print("you can go 1 = top left, 2 = bottom left, 3 = middle, 4 = top right and 5 = bottom right.")
    print("Please don't let your country down. Don't be a Harry Kane!")
    print("Lets start with " + nationality + " vs Germany in a penalty shootout!!!")

    player_goals = 0
    computer_saves = 0

    def game():
        global player_goals, computer_saves

        player_choice = input("Choose either '1', '2', '3', '4', '5': ")

        player_choice = int(player_choice)

        if player_choice not in [1, 2, 3, 4, 5]:
            print("Come on mate just pick a number between 1-5")
            return game()

        computer_choice = random.choice([1, 2, 3, 4, 5])

        print(f"{name} has gone for {player_choice}"),
        print(f"computer dives to {computer_choice}")

        if player_choice == computer_choice:
            computer_saves += 1
            print("Keeper with the SAVVVVEEEE!!!!!!!!")
        else:
            player_goals += 1
            print(f"{name} with the GGGOOOOOAALLLLL")
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
        for _ in range(5):
            game()

        if player_goals >= 3 or computer_saves >= 3:
            print("That's all they needed!")
            if player_goals >= 3:
                print(name + " has won it for " + nationality + " what a legend")
            else:
                print("Computer breaks the hearts of " + nationality)
        else:
            game()


else:
    print("Can't handle the heat get out of the kitchen!")
