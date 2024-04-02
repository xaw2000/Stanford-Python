"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def down():
    """
    Pre-condition: Karel is facing South, at the upper right
    Post-condition: Karel is facing South, at the lower right
    """
    while front_is_clear():
        move()


def up():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    move()
    turn_right()


def turn_right():
    """
    Karel will turn left 3 times
    """
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
