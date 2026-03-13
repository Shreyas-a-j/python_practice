import random

user_win = 0
bot_win = 0

move = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

def player_input():
    move_player = int(input("Your Move (1-rock, 2-paper, 3-scissors): "))
    if move_player in move:
        return move_player
    else:
        return player_input()

def rock_paper_scissors(user_win, bot_win):

    end_game = input("Play? (y/n): ").lower()
    if end_game != "y":
        print("You won", user_win, "times and Bot won", bot_win, "times")
        quit()

    player_move = player_input()
    bot_move = random.randint(1,3)

    print("Bot chose:", move[bot_move])

    if player_move == bot_move:
        print("Draw!")
    elif (player_move == 1 and bot_move == 3) or \
         (player_move == 2 and bot_move == 1) or \
         (player_move == 3 and bot_move == 2):
        print("You won!")
        user_win += 1
    else:
        print("You lost!")
        bot_win += 1

    return rock_paper_scissors(user_win, bot_win)

rock_paper_scissors(user_win, bot_win)