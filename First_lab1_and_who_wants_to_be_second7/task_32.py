#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    d=0
    fill_cell()
    while wall_is_on_the_right()==0:
        move_right()
        if not wall_is_above():
            if wall_is_on_the_right():
                break
            i=0
            while not wall_is_above():
                move_up()
                if not cell_is_filled():
                    fill_cell()
                else:
                    d+=1
                i+=1
            move_down(i)
        else:
            fill_cell()
    mov('ax',d)

if __name__ == '__main__':
    run_tasks()
