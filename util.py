import os
import time

def clear_screen():
    """
    Clears the terminal screen using os.name.
    Works on Windows, macOS, and Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_not_empty_string(prompt) -> str: 
    """
    Prompts the user for input until a non-empty string is provided.
    Args: 
        prompt (str): The prompt to display to the user.
    Returns: 
        str: The first non-empty string entered by the user.
    """
    while True:
        value = input(prompt).strip()
        # Checks if string is non-empty after stripping whitespace
        if value:  
            return value


def get_yes_no_answer(prompt: str) -> bool:
    """
    Prompts the user for a yes/no answer until valid input is received.
    Args:
        prompt (str): The prompt to display to the user.
    Returns:
        bool: True for yes/y, False for no/n
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please answer 'yes' or 'no'")

def get_positive_integer(prompt: str, ) -> int:
    """
    Prompts the user until a valid positive integer is entered.
    
    Args:
        prompt (str): The prompt to display to the user.
    
    Returns:
        int: A positive integer (greater than 0)
    """
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
            if number > 0:
                return number
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid positive number.")

def animation():
    clear_screen()
    print(f"{CGREEN}{CBOLD}Connecting to Loughborough car rental shop{CEND}", end="")
    for i in range(10):
        print(f"{CGREEN}{CBOLD}.{CEND}", end="", flush=True)
        time.sleep(0.1)
    print(f"{CEND}")
    print()





# Definition of colours using ANSI standard
CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'