import random

def game():
    print("You are playing the game  ...")
    score=random.randint(1,62)
    # fetch the high score
    with open(r"C:\Users\pc\OneDrive\Desktop\CWD python course\ch=9\highscore.txt") as f:
        highscore = f.read()
        if highscore == "":
            highscore = 0
        else:
            highscore = int(highscore)
    print(f"Your score is {score} and the high score is {highscore}")
    if score > highscore:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    return score

game()