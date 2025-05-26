import random
import time

def clear():
	print("\033[H\033[J", end = "")

def space():
  print()

f = open("Assets/left_position.txt", "r")
left_position = f.read()

f.close()

f3 = open("Assets/right_position.txt", "r")
right_position = f3.read()

f3.close()

f4 = open("Assets/user.txt", "r")
user = f4.read()

f4.close()

f5 = open("Assets/opponent.txt", "r")
opponent = f5.read()

f5.close()