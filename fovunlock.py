import win32com.client
import keyboard
import numpy
from time import sleep
from os import system
from os import path

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

fov_counter = 90
hVal = 175
lVal = 10

def Load():
  sleep(1)
  print("Created By:  r       ")
  sleep(0.15)
  system(clear)
  print("Created By:  r c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c    8")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o298")
  sleep(0.15)
  system(clear)
  print("Created By: Cracko298")
  sleep(4)
  system(clear)
Load()

shell = win32com.client.Dispatch("WScript.Shell")
check_file = path.exists("fov_value.dat")

if check_file == True:
  with open('fov_value.dat','rb+') as hexafile:
    hexafile_read = hexafile.read(1)
    last_saved_value = int.from_bytes(hexafile_read[::-1], byteorder='big')
    hexafile.close()

if check_file != True:
  file0 = open('fov_value.dat','x')
  file0.close()


def tutorial():
  global check_file
  print("Press '-', And use the 'UP/DOWN Arrow-Keys' to set your in-game FOV. (Make Sure To Be in-game).")
  print("If it's not working, try letting go of '-' and the 'Arrow-Keys' imediately after you use them.")
  if check_file == True:
    print("Since you have used this tool before, Press '=' to set your last used FOV.")
  print(" ")
  print("Press the '?' Key to see this message again.")
  print(" ")
tutorial()

while 1==1:
  if check_file != False:
    if keyboard.is_pressed('='):
      print(f"Set FOV to {last_saved_value}.")
      sleep(0.6)
      shell.sendkeys('`')
      shell.sendkeys('f')
      shell.sendkeys('o')
      shell.sendkeys('v')
      shell.sendkeys(' ')
      shell.sendkeys(last_saved_value)
      keyboard.press_and_release('Enter')
      fov_counter = last_saved_value


  if keyboard.is_pressed('/'):
    system(clear)
    tutorial()


  if fov_counter >= 175:
    print(f"User FOV is currently: '{fov_counter}'. Resetting to FOV of: '175'.")
    print("Reason: Value is to High. High Chance of a Fatal Error.")
    sleep(0.6)
    shell.sendkeys('`')
    shell.sendkeys('f')
    shell.sendkeys('o')
    shell.sendkeys('v')
    shell.sendkeys(' ')
    shell.sendkeys(hVal)
    keyboard.press_and_release('Enter')
    fov_counter = 170
    byte_array = bytearray(fov_counter.to_bytes(1, byteorder='big'))
    reversed_array = byte_array[::-1]
    with open('fov_value.dat','rb+') as file1:
        file1.write(reversed_array)
        file1.close()
    sleep(1)
    system(clear)
    tutorial()
  
  if fov_counter <= 5:
    print(f"User FOV is currently: '{fov_counter}'. Resetting to FOV of: '10'.")
    print("Reason: Value is to Low. High Chance of a Fatal Error.")
    sleep(0.6)
    shell.sendkeys('`')
    shell.sendkeys('f')
    shell.sendkeys('o')
    shell.sendkeys('v')
    shell.sendkeys(' ')
    shell.sendkeys(lVal)
    keyboard.press_and_release('Enter')
    fov_counter = 10
    byte_array = bytearray(fov_counter.to_bytes(1, byteorder='big'))
    reversed_array = byte_array[::-1]
    with open('fov_value.dat','rb+') as file1:
        file1.write(reversed_array)
        file1.close()
    sleep(1)
    system(clear)
    tutorial()

  if keyboard.is_pressed('up') and keyboard.is_pressed('-'):
    fov_counter += 5
    print(f"Set FOV to {fov_counter}.")
    sleep(0.6)
    shell.sendkeys('`')
    shell.sendkeys('f')
    shell.sendkeys('o')
    shell.sendkeys('v')
    shell.sendkeys(' ')
    shell.sendkeys(fov_counter)
    keyboard.press_and_release('Enter')
    byte_array = bytearray(fov_counter.to_bytes(1, byteorder='big'))
    reversed_array = byte_array[::-1]
    with open('fov_value.dat','rb+') as file1:
        file1.write(reversed_array)
        file1.close()

    
  if keyboard.is_pressed('down') and keyboard.is_pressed('-'):
    fov_counter -= 5
    print(f"Set FOV to {fov_counter}.")
    sleep(0.6)
    shell.sendkeys('`')
    shell.sendkeys('f')
    shell.sendkeys('o')
    shell.sendkeys('v')
    shell.sendkeys(' ')
    shell.sendkeys(fov_counter)
    keyboard.press_and_release('Enter')
    byte_array = bytearray(fov_counter.to_bytes(1, byteorder='big'))
    reversed_array = byte_array[::-1]
    with open('fov_value.dat','rb+') as file1:
        file1.write(reversed_array)
        file1.close()