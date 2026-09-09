import random
from turtle import reset
from colorama import Fore, Style, init
init(autoreset=True)
AI_choice=['rock','paper','scissors']
Ai_choice=random.choice(AI_choice)
print(Fore.CYAN+"Welcome to Rock Paper Scissors Game!"+Style.RESET_ALL)
print(Fore.MAGENTA+"Please choose one of the following options:")
player_choice = input(Fore.LIGHTBLUE_EX+"1. Rock\n2. Paper\n3. Scissors\nEnter your choice (rock, paper, scissors): ")

if Ai_choice==player_choice:
        print(Fore.YELLOW+"It's a tie!"+Style.RESET_ALL)
elif player_choice=="rock" or player_choice=="1":
            if Ai_choice=="scissors":
                print(Fore.GREEN+"Rock smashes scissors! You win!"+Style.RESET_ALL)
            else:
                print(Fore.RED+"Paper covers rock! You lose."+Style.RESET_ALL)
elif player_choice=="paper" or player_choice=="2":
            if Ai_choice=="rock":
                print(Fore.GREEN+"Paper covers rock! You win!"+Style.RESET_ALL)
            else:
                print(Fore.RED+"Scissors cuts paper! You lose."+Style.RESET_ALL)
elif player_choice=="scissors" or player_choice=="3":
            if Ai_choice=="paper":
                print(Fore.GREEN+"Scissors cuts paper! You win!"+Style.RESET_ALL)
            else:
                print(Fore.RED+"Rock smashes scissors! You lose."+Style.RESET_ALL)
reset=input(Fore.YELLOW+"Do you want to play again? (yes/no): ")
if reset.lower()=="yes":
    import Rock_paper_scisor
elif reset.lower()=="no":
    print(Fore.CYAN+"Thank you for playing!"+Style.RESET_ALL)
