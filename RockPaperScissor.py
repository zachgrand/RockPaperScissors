from multiprocessing import RLock
from multiprocessing.connection import wait
import random
import time

answers = [
    "rock",
    "paper",
    "scissors",
]

while True:
    rpc_game = input("Do you want to play Rock, Paper, Scissors? ").lower()
    if rpc_game == 'yes': 
        print("Okay lets play! ")
        time.sleep (2)
        while True:
         user_input = input("What are you picking? ")
         time.sleep (1)
         if user_input == random.choice(answers):
            print("You win ")
         elif user_input != random.choice(answers):
            print("You loose")
            play_again = input("want to play again? ")
            break

    elif rpc_game == 'no':
        print("Maybe next time then ")
        break
    else:
        print("Thats not an answer ")