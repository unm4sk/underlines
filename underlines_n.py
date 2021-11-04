from time import sleep
import os
import pyperclip
from colorama import Fore, Style, init

def clear():
  os.system('cls' if os.name == 'nt' else 'clear') 
clear()

print('\t\tunderlines v.3.0\n')

init() # making colorama working on windows

def main():
  words = input('Enter the text: ')
  while True:
    if words.split() == []:
      words = input('The input shouldn\'t be empty! Please enter the text: ') # checking for a plain text
    else:
      break
  words_sep = words.split() # splitting words to a list to iterate

  symbol_ask = input('Enter the symbol that replaces letters in words (enter for default "_"): ')

  if symbol_ask == '': # default
    symbol = '_'
  else:
    symbol = symbol_ask

  while len(symbol_ask) > 1 or symbol_ask == '' and symbol != '_' or symbol_ask.count(' ') != 0 or symbol_ask.count('	') != 0: # checking for a symbol
    symbol_ask = input('Enter a symbol: (shouldn\'t be a space) ')
    if len(symbol_ask) == 1 and symbol_ask != ' ' and symbol_ask != '	':
      symbol = symbol_ask
      break

  changed_words = []
  i = 0 
  for word in words_sep: # for each word in the whole text
    i = 0 # for each new word reset counter
    for letter in word: # for each symbol in the word
      i += 1
    underlines = symbol * i
    changed_words.append(underlines)
  str_for_copy = ' '.join(changed_words) # space between words
  pyperclip.copy(str_for_copy)
  print(str_for_copy + f'\n\nThe result was {Fore.GREEN}SUCCESSFULLY{Style.RESET_ALL} copied to clipboard!\n')

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
    if input('Clear? (enter to clear) ').lower() == '':
      clear()
      print('\t\tunderlines v.3.0\n')