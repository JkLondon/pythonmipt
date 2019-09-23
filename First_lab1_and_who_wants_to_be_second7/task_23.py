#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    j=0
    while wall_is_on_the_right()==0:
        move_right()
        if wall_is_above()==0:
            i=0
            while wall_is_above()==0:
                move_up()
                fill_cell()
                i+=1
            move_down(i)
        if wall_is_beneath()==0:
            i=0
            while wall_is_beneath()==0:
                move_down()
                fill_cell()
                i+=1
            move_up(i)
        j+=1
    move_left(j)


if __name__ == '__main__':
    run_tasks()
