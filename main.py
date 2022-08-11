import os 
import time
import threading
import colorama
import sys
import random
import socket
import string
colorama.init()

def stringo(y):
    return ''.join(random.choice(string.ascii_letters)for x in range(y))

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)

print("Leef's Sample gen")
print("discord.gg/creditcardfraud")
print("Your IP is: "+IPAddr)
print("---------------------------")
print("""
[1] Adding sums
[2] Generating random characters
""")
options = input("Choose >: ")

if options == '1':
  os.system('clear') #for windows it would be cls instead of clear
  def sum(a, b):
    return (a + b)

  a = int(input('Enter 1st number: '))
  b = int(input('Enter 2nd number: '))

  print(f'Sum of {a} and {b} is {sum(a, b)}')

if options == '2':
  os.system('clear')
  print("""
  [1] Generate 1 line
  [2] Generate Endless
  """)
  opt = input("Choose: ")
if opt == '1':
  os.system('clear') #for windows it would be cls instead of clear
  threads = [99]
  print(stringo(99)), print(stringo(99))#99 = How many characters are going to be generated

if opt == '2':
  threads = [99]
  os.system('clear') #for windows it would be cls instead of clear
  print(stringo(99)), print(stringo(99))
  while True:
    print(stringo(99)), print(stringo(99))
