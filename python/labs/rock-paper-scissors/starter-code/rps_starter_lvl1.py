import random


def get_player_move():
    """Asks the user to enter a move as 'r', 'p', or 's', and return it"""
    return input("Choose your move [r|p|s]: ").lower()


def get_computer_move():
    """Randomly generates the computer's move and
    returns it in the form of 'r', 'p', or 's'"""
    return "rps"[random.randint(0,2)]


def determine_winner(player_move, comp_move):
    """Takes in a player move and computer move each as 'r', 'p', or 's',
    and returns the winner as 'player', 'computer', or 'tie'"""
    if player_move == comp_move:
        return "tie"
    elif (player_move == "r" and comp_move == "s") or \
         (player_move == "s" and comp_move == "p") or \
         (player_move == "p" and comp_move == "r"):
        return "player"
    else:
        return "computer"


def print_scoreboard(player_wins, comp_wins, ties):
    """Prints out the scoreboard neatly.  Returns nothing."""
    print("Player Score: %s" % player_wins)
    print("Computer Score: %s" % comp_wins)
    print("Ties: %s" % ties)


def get_move_name(short_move):
    """Takes in 'r', 'p', or 's', and returns 'Rock', 'Paper, or
    'Scissors' respectively. Use this to neatly print move choices"""
    if short_move == 'r':
        return "Rock"
    elif short_move == 'p':
        return "Paper"
    else:
        return "Scissors"


# Write your code below - make RPS happen using the functions above!
