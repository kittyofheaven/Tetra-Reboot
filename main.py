import time
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

def shutdown():
  clear()
  for i in range(4) :
    print('Shutdown'+'.'*i)
    time.sleep(0.5)
    exit()

def tetra_console () :
  print(r"""Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
  """)
  time.sleep(0.5)
  print(r"""Welcome to Tetra-Corps GIGA Computing
Last login: Sat Oct  2 03:59:02 2049 from 192.168.0.1
Type "help" to show all commands available.
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
      print("Your objective is to cancel a program called Old-Tree-Destruction\n\nAll commands :\nreboot, shutdown, help, cls, ")

    elif console_input == 'cls' :
      clear()

    else :
      pass

reboot()
tetra_console()
