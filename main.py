import time
import re
from os import system, name
from color import Colors

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def reboot():
  for reboot in range(3) :
    for i in range(4) :
      print('Rebooting'+'.'*i)
      time.sleep(0.5)
      clear()
  tetra_console()    

def shutdown():
  clear()
  for i in range(4) :
    print('Shutdown'+'.'*i)
    time.sleep(0.5)
    exit()

all_commands = ['reboot', 'shutdown', 'help', 'cls', 'ls', ]
all_files = ['bit_blocks', ]
bit_blocks_win_status = False


def bit_blocks () :

  global bit_blocks_win_status
  global all_files

  while True :

    console_input = input('bit_blocks > ')

    if console_input == 'test' :
      print('its work')
    
    elif console_input == 'back' :
      break
    
    # this is when u have to make rule to win the game
    elif console_input == 'win' :
      print('yey u win')
      bit_blocks_win_status = True
      all_files.append('game2')

    else :
      pass
    

def tetra_console () :

  global all_commands
  global all_files

  print(r"""Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
  """)
  time.sleep(0.5)
  print(r"""Welcome to Tetra-Corps GIGA Computing
Last login: Sat Oct  2 03:59:02 2049 from 192.168.0.1
Type "help" to show help.
  """)
  time.sleep(0.5)

  run = True

  while run :

    console_input = input('> ')

    if console_input == 'shutdown':
      shutdown()

    elif console_input == 'test' :
      print('fuck you')

    elif console_input == 'help' :
      print("You're now hacking the Tetra Corps a top global computing system.\n")
      print("Tetra Corps is a large company based in creating New tree advanced technology.")
      print("Human not longer needed to take care of plants, this technology already solve human need of O2.")
      print("But Tetra Corps is getting greedy, they want to burn all the old tree (natural one) and start monopolize human need of O2.\n")
      print("Your objective is to cancel a program called Old-Tree-Destruction\n\nTo see all comands type 'commands'\n")

    elif console_input == 'cls' :
      clear()

    elif console_input == 'commands' :
      print(', '.join(all_commands))

    elif console_input == 'reboot' :
      reboot()

    elif console_input == 'ls' :
      print(' '.join(all_files))       

    elif bool(re.compile('cd ').match(console_input)) :
      cd_input = console_input.split(' ')
      if cd_input[1] == 'bit_blocks' :
        bit_blocks()

    else :
      pass
  
reboot()

