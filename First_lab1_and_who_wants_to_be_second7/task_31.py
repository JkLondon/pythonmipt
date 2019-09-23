#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    n=0
    while 1==1:
        if wall_is_beneath()==0:
            move_down()
        else:
            if wall_is_on_the_left()==0:
                move_left()
                n+=1
            else:
                move_right(n)
                x=False
                while wall_is_on_the_left()==0:
                    if wall_is_beneath()==0:
                        x=True
                    move_left()
                move_right(n)
                if not x:
                    break
                n=0
    move_left(n)

if __name__ == '__main__':
    run_tasks()
