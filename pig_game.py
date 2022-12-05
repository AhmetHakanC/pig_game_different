import random


def roll_two_dice():
    dices = [random.randint(1, 6), random.randint(1, 6)]
    return dices


def get_lucky_number():
    while True:
        lucky_number = input("Lucky number--> ")
        try:
            lucky_number = int(lucky_number)
        except:
            print("Invalid number")
            continue
        if lucky_number < 4 or lucky_number > 12:
            print("Invalid number")
            continue
        else:
            return lucky_number


def get_player_answer():
    while True:
        print("Do you want to keep or continue?")
        ans = input("Answer(Y or N)-->")
        ans = ans.capitalize()
        if ans != "Y" and ans != "N":
            print("İnvalid input")
            continue
        else:
            return ans


def one_roll(die1, die2, luck_number):
    if die1 == 1 and die2 != 1:
        return 1
    elif die1 != 1 and die2 == 1:
        return 1
    elif die1 == 1 and die2 == 1:
        return 2
    elif die1 + die2 == luck_number:
        return 3
    else:
        return 4


def one_turn(lucky_number, current_score):
    temp = 0
    while True:
        two_dice = []
        two_dice.extend(roll_two_dice())
        dice1 = two_dice[0]
        dice2 = two_dice[1]

        print("Dice rolled: ", dice1, " and ", dice2)
        rule = one_roll(dice1, dice2, lucky_number)

        if rule == 1:
            print("Rule 1 applied")
            return current_score
        elif rule == 2:
            print("Rule 2 applied")
            return 0
        elif rule == 3:
            print("Rule 3 applied")
            temp += (2 * current_score) - current_score
        else:
            print("Rule 4 applied")
            temp += dice1 + dice2
            ans = get_player_answer()
            if ans == "Y":
                continue
            else:
                return current_score + temp


# This function prints the current scores.
def scores(name1, name2, score1, score2):
    print("--------------------")
    print(name1, "Score-->  ", score1)
    print(name2, "Score-->  ", score2)
    print("--------------------")


def play_pig():
    # Variables.
    # Flag, checks if game is over.
    # Turn, for check whose turn.
    # lucky_number, current player's lucky number.
    # player1_score, player2_score, players score.
    flag = False
    turn = 1
    lucky_number = player1_score = player2_score = 0

    # All game
    print("Welcome to the game!")
    while True:
        if flag:  # Checks if game is over.
            break

        # Gets players names.
        name1 = input("Player 1's name--> ")
        if name1 == "":
            name1 = "Player 1"
        name2 = input("Player 2's name--> ")
        if name2 == "":
            name2 = "Player 2"

        # Game.
        while True:
            scores(name1, name2, player1_score, player2_score)

            # this if statement for checks if one of the players reach the points limit.
            if player1_score >= 100:
                print("Player 1 wins!")
                flag = True
                break
            elif player2_score >= 100:
                print("Player 2 wins!")
                flag = True
                break

            # Checks the turn. And plays.
            if turn == 1:
                print("{}" 's turn...'.format(name1))
                lucky_number = get_lucky_number()
                player1_score = one_turn(lucky_number, player1_score)
                turn = 2

            else:
                print("{}" 's turn...'.format(name2))
                lucky_number = get_lucky_number()
                player2_score = one_turn(lucky_number, player2_score)
                turn = 1


play_pig()
