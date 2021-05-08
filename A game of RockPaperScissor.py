
import random
N_GAME=3
def main():
    """
    Rock Paper Scissor Game
    
    Game:
    Each player chooses a move simultaneously from the choices:
    Rock Paper Scissors

    if they choose the same move its a tie
    rock beats scissor
    scissor beats paper
    paper beats rock

    In this game human plays against the computer.
    The game is repeated N_Games times if it is a win 1 pt.If the player loses -1.
    if both chose the same move its a tie.

    """
    welcome()
    total_score=0
    # let's get the ai move
    for i in range(N_GAME):
        ai_move=get_ai_move()
        # let's get the human move
        human_move=get_human_move()

        # decide the winner
        winner=get_winner(ai_move,human_move)
        total_score = update_score(winner,total_score)
        print("AI move is ",ai_move)
        print("The winner is",winner)
        print("total score is: ",total_score)
        print("")


def update_score(winner,total_score):
    if winner=="ai":
        total_score -=1
    if winner=="human":
        total_score +=1
    if winner=="tie":
        total_score=0
    return total_score


def get_ai_move():
    """
    This function returns the move of the AI
    """
    number=random.randint(1,3)
    if number==1:
        return "rock"
    if number==2:
        return "paper"
    if number==3:
        return "scissor"
def get_human_move():
    """
    This function returns the move of human
    """
    while True:
        human_move=input("Enter your move: ")
        if valid_move(human_move):
            return human_move
        print("invalid move")
    return human_move

def valid_move(human_move):
    """
    This function validates  if user input is either rock paper or scissor
    returns a boolean value
    >>> valid_move("rock")
    True
    >>> valid_move("paper")
    True
    >>> valid_move("scissor")
    True
    >>> valid_move("unicorn")
    False
    """
    if human_move=="rock":
        return True
    if human_move=="paper":
        return True
    if human_move=="scissor":
        return True
    else:
        return False


def get_winner(ai_move,human_move):
    """
    >>> get_winner("rock","scissor")
    "ai"
    >>> get_winner("paper","scissor")
    "human"

    >>> get_winner("rock","rock")
    "tie"
    """
    if ai_move==human_move:
         return "tie"
    if ai_move=="rock":
        if human_move=="paper":
            return "human"
        return "ai"
    if ai_move=="paper":
        if human_move=="scissor":
            return "human"
        return "ai"
    if ai_move=="scissor":
        if human_move=="rock":
            return "human"
        return "ai"







def welcome():
    print("Welcome to the exciting game of Rock Paper Scissor")
    print("You will play",str(N_GAME),"games against the AI")
    print("Rock beats Scissor")
    print("Scissor beeats paper")
    print("Paper beats Rock")
    print("-----------------------------------------------------")
    print("")












if __name__ == '__main__':
    main()
