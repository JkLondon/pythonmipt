#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_4():
    while 1==1:
        
        while 1==1:
            move_right(1)
            move_down(1)
            fill_cell()
            move_right()
            fill_cell()
            move_left(2)
            fill_cell()
            move_right()
            move_down()
            fill_cell()
            move_up(2)
            fill_cell()
            move_left()
            move_right(2)
            if wall_is_on_the_right():
                move_left(2)
                break
            else:
                move_right(2)
        while wall_is_on_the_left()==0:
            move_left()
        move_down(2)
        if wall_is_beneath()==0:
            move_down(2)
        else:
            move_up(2)
            break
    


if __name__ == '__main__':
    run_tasks()
