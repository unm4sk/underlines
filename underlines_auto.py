from time import sleep
import os
import pyperclip
from colorama import Fore, Style, init
import pyautogui
import webbrowser
from set import auto_open, auto_copy, auto_clear


def clear():
  os.system('cls' if os.name == 'nt' else 'clear') 
clear()

print('\t\tunderlines v.3.0\n')

init() # making colorama working on windows

if auto_open or input(f"Open {Fore.LIGHTBLUE_EX}Quizlet{Style.RESET_ALL} page? [y/n] ").lower() == "y":
	webbrowser.open("https://quizlet.com/latest", 1)
	print(f"{Fore.LIGHTBLUE_EX}Quizlet{Style.RESET_ALL} was opened!")

print("Select a word!")

def main():
    while True:
        pyperclip.copy("")  # clearing the clipboard
        sleep(3)  # waiting for user to start 

        try:
            pyautogui.hotkey("ctrl", "c")
        except KeyboardInterrupt:
            pass

        sleep(.01)
        word = pyperclip.paste()
        
        if word == "": continue  # result should not be empty!

        if auto_copy or input(f"Is {Fore.LIGHTGREEN_EX}{word}{Style.RESET_ALL} correct? [y/n] ").lower() == "y":
            res = []
            for letter in word.strip():
                if letter == " ":
                    res.append(" ")
                res.append("_")
            pyperclip.copy("".join(res))
            print("\n" + "".join(res) + f'\n{word}\n\nThe result was {Fore.GREEN}SUCCESSFULLY{Style.RESET_ALL} copied to clipboard!\n')
            break


def goodbye(dot='.'):	# just for aesthetical purposes
  print('Goodbye then', end='')
  for _ in range(3):
      print(dot, end='', flush=True)
      sleep(0.5)
  print()

while True:
  main()
  if input('Continue? (y or n) ').lower() != 'y':
    goodbye()
    break
  else:
    if auto_clear or input('Clear? (enter to clear) ').lower() == '':
      clear()
      print('\t\tunderlines v.3.0\n') 