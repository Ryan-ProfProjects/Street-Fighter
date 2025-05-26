from health import *
from files import *

op_health = 0
us_health = 0

print(left_position)

input(f'Click [Enter] to fight\n')
clear()

txt_opponnent = f"Opponent Health: {health_stages[op_health]}"

txt_user = f"Your Health: {health_stages[us_health]}"


def check_us_health():
  if us_health >= 15:
    clear()
    print(opponent)
    txt_user = f"Your Health: {health_stages[15]}"
    print(f"{txt_user} {txt_opponnent.center(80)}")
    space()
    exit('You loose.')
 
def check_op_health():
  if op_health >= 15:
    clear()
    print(user)
    txt_opponnent = f"Opponent Health: {health_stages[15]}"
    print(f"{txt_user} {txt_opponnent.center(80)}")
    space()
    exit('You win!')

def check_draw():
  if us_health == 15 and op_health == 15:
    clear()
    print(left_position)
    print(f"{txt_user} {txt_opponnent.center(80)}")
    exit('Draw.')

def check():
    check_us_health()
    check_op_health()
    check_draw()

while True:
    print(left_position)

    print(f"{txt_user} {txt_opponnent.center(80)}")
    space()
    check()
    input("Instructions: click [Enter] to push opponent.")
    check()
    clear()
    
    print(right_position)

    unch_list = [1, 2]

    health_change = random.choice(unch_list)
    
    op_health = op_health + health_change

    txt_opponnent = f"Opponent Health: {health_stages[op_health]}"
    print(f"{txt_user} {txt_opponnent.center(80)}")
    check()
    clear()
      
      
    print(right_position)
    print(f"{txt_user} {txt_opponnent.center(80)}")
    space()
    check()
    print("Waiting for opponent...")
    check()
    time.sleep(0.5)
    clear()

    print(left_position)

    unch1_list = [1, 2]

    health_change1 = random.choice(unch1_list)
    
    us_health = us_health + health_change1
    check()
    txt_user = f"Your Health: {health_stages[us_health]}"
    print(f"{txt_user} {txt_opponnent.center(80)}")
    check()
    clear()
    