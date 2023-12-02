import random

print(
    """
████████▄   ███    █▄   ▄█   ▄████████    ▄█   ▄█▄
███    ███  ███    ███ ███  ███    ███   ███ ▄███▀
███    ███  ███    ███ ███▌ ███    █▀    ███▐██▀
███    ███  ███    ███ ███▌ ███         ▄█████▀
███    ███  ███    ███ ███▌ ███        ▀▀█████▄
███    ███  ███    ███ ███  ███    █▄    ███▐██▄
███  ▀ ███  ███    ███ ███  ███    ███   ███ ▀███▄
 ▀██████▀▄█ ████████▀  █▀   ████████▀    ███   ▀█▀
                                         ▀
   ▄████████  ▄█     ▄████████    ▄████████
  ███    ███ ███    ███    ███   ███    ███
  ███    █▀  ███▌   ███    ███   ███    █▀
 ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀  ▄███▄▄▄
▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀
  ███        ███  ▀███████████   ███    █▄
  ███        ███    ███    ███   ███    ███
  ███        █▀     ███    ███   ██████████
                    ███    ███
   ▄███████▄    ▄████████ ███▄▄▄▄      ▄████████
  ███    ███   ███    ███ ███▀▀▀██▄   ███    ███
  ███    ███   ███    █▀  ███   ███   ███    █▀
  ███    ███  ▄███▄▄▄     ███   ███   ███
▀█████████▀  ▀▀███▀▀▀     ███   ███ ▀███████████
  ███          ███    █▄  ███   ███          ███
  ███          ███    ███ ███   ███    ▄█    ███
 ▄████▀        ██████████  ▀█   █▀   ▄████████▀
    """)


def game():
    global player_goals, computer_saves

    player_choice = input("Choose either '1', '2', '3', '4', '5': \n")

    player_choice = int(player_choice)

    if player_choice not in [1, 2, 3, 4, 5]:
        print("Come on mate just pick a number between 1-5 \n")
        return game()

    computer_choice = random.choice([1, 2, 3, 4, 5])

    print(f"{name} has gone for {player_choice} \n"),
    print(f"computer dives to {computer_choice} \n")

    if player_choice == computer_choice:
        computer_saves += 1
        print("Keeper with the SAVVVVEEEE!!!!!!!! \n")
    else:
        player_goals += 1
        print(f"{name} with the GGGOOOOOAALLLLL \n")
    return player_goals, computer_saves


def play_rounds(rounds):
    player_total_goals = 0
    computer_total_saves = 0

    for _ in range(rounds):
        player_goals, computer_saves = game()
    print("That's all they needed! \n")
    if player_goals >= 3:
        print(name + """ has won it for """
              + nationality + " what a legend")
    else:
        print("Computer breaks the hearts of " + nationality)


play_game = input("Can you step up? (yes/no): \n").lower()

while play_game not in ['yes', 'no']:
    print("We can progess unless you type yes or no!")
    play_game = input("Can you step up? (yes/no): \n").lower()

if play_game == 'yes':
    print("please enter your name: \n")
    name = input()
    print("Please can " + name + " enter the country they represent: \n")
    nationality = input()
    print("We have " + name + " from " + nationality + "\n")
    print("""
    Aim is to pick a number different to the computer in order to score.
    """)
    print("""
    If you and the computer both have the same number
    the computer makes the saves.
    """)
    print("""
    However if you and the computer both pick different
    numbers then you score.
    """)
    print("""
    Example if you type 2 and computer types 3
    you've scored a goal however if you type 1 and the
    computer types 1 then the computer makes the save.
    """)
    print("""
    you can go 1 = top left, 2 = bottom left,
    3 = middle, 4 = top right and 5 = bottom right.
    """)
    print("Please don't let your country down. Don't be a Harry Kane! \n")
    print("Lets start with "
          + nationality + " vs Germany in a penalty shootout!!! \n")
    play_again = True
    while play_again:
        player_goals = 0
        computer_saves = 0
        play_rounds(5)
        play_again = input("Fancy another go? (yes/no)") == 'yes'.lower()
    print("Thank you for playing")

elif play_game == 'no':
    print("Okay then enjoy your day")
    exit()
