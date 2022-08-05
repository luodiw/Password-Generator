#!/usr/bin/env python
from random import choice
from colorama import init
from termcolor import colored
import string

init()

strength = 8

def generatePassword(strength):
  alphabets = string.ascii_letters + string.digits
  password = ""

  for alphabet in alphabets:
    strength -= 1
    
    if (strength == 0):
      break

    password += choice(alphabets)

  return password

if __name__ == "__main__":
  print(colored("""
   ____
  |  _ \ __ _ ___ ___ ___   ___  _______ ______  _____
  | |_) / _` / __/ __||  |  |  ||       ||   __ \|     \ 
  |  __/ (_| \__ \__ \|  |  |  ||   -   ||      <|  --  |
  |_|   \__,_|___/___/|________||_______||___|__||_____/ 
                      
  """, "cyan"))
  
  try:
      print(colored("How strong do you want to set your password?", "yellow"))
      strength = int(input(colored("→ ", "yellow")))

  except ValueError:
    print(colored("ERROR: Invalid input, enter a number", "red"))
    exit()

  generated = generatePassword(strength)

  print(colored(f"Password Generated: {generated}", "green"))
