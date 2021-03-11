import random

def generate():
    num = random.randrange(0, 3)
    if num == 0:
        opponent = "rock"
    elif num == 1:
        opponent = "paper"
    else:
        opponent = "scissors"
    return opponent


class RPS:
    def __init__(self, rps):
        self.rps = rps


r1 = RPS(generate())

def printResults():
    print(f"You: {option}")
    print(f"Opponent: {r1.rps}")

option = input("Enter \"rock\", \"paper\", or \"scissors\": ").lower()


if option == r1.rps:
    printResults()
    print("It's a tie.")
elif option == "rock" and r1.rps == "scissors":
    printResults()
    print("You win!")
elif option == "rock" and r1.rps == "paper":
    printResults()
    print("You lose.")
elif option == "paper" and r1.rps == "rock":
    printResults()
    print("You win!")
elif option == "paper" and r1.rps == "scissors":
    printResults()
    print("You lose.")
elif option == "scissors" and r1.rps == "paper":
    printResults()
    print("You win!")
elif option == "scissors" and r1.rps == "rock":
    printResults()
    print("You lose.")
