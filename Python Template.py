def main_notes():   # to collapse the text below in the IDE  
    """
    Project Name By Besser

    REMEMBER TO SAVE AS NEW DOC, DON'T EDIT THIS FILE

    Date

    
    https://github.com/besser435?tab=repositories
    """

version = "v1.0"
date = "Month 2022"


import random
import time 
import sys
import os  

from colorama import init   # pip install colorama
init()
from colorama import Fore, Back, Style
init(autoreset=True)


# options
debug = 0

# storage


def cc():   # shortens this long command to just cc()
    os.system("cls" if os.name == "nt" else "clear")    # clears terminal


def main():
    pass







def debug():
    if debug:
        pass


def main_menu():    
    print(" By Besser")
    print(version)
    print(date)
    
    if debug:
        pass
    print(Fore.CYAN + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(Fore.LIGHTGREEN_EX + "Options:")
    print("1: ")
    print("2: ")
    print("3: ")
    print("Q: Quit")
  
    which_option = input("What would you like to do? ")

    if "1" == which_option:
        cc()
        
        
    elif "2" == which_option:
        cc()
        

    elif "3" == which_option:
        cc()


    elif "q" == which_option:
        sys.exit()
    

    elif "a" == which_option:  # shortcut to current work
        pass 

    else:
        cc()
        print(Fore.RED + "Invalid input")
        main_menu()
main_menu()




main()
