import random

print("Want to play?")
play_game = input("Can you step up? (yes/no): \n").lower()

if play_game == 'yes':
    print("please enter your name: \n")
    name = input()
    print("Please can " + name + " enter the country they represent: \n")
    nationality = input()
    print("We have " + name + " from " + nationality)

    player_goals = 0
    computer_saves = 0

    def game():
        global player_goals, computer_saves

        player_choice = input("Choose either '1', '2', '3', '4', '5': ")

        player_choice = int(player_choice)

        if player_choice not in [1, 2, 3, 4, 5]:
            print("Incorrect")
            return game()

        computer_choice = random.choice([1, 2, 3, 4, 5])

        print(f"{name} + goes {player_choice}"),
        print(f"computer goes {computer_choice}")

        if player_choice == computer_choice:
            computer_saves += 1
            print("save")
        else:
            player_goals += 1
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
        for _ in range(5):
            game()

        if player_goals >= 3 or computer_saves >= 3:
            print("That's all they needed!")
            if player_goals >= 3:
                print(name + " has won it for " + nationality)
            else:
                print("Computer wins")
        else:
            game()
else:
    print("Okay")
