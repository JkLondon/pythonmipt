#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    ch=0
    while wall_is_on_the_right()==0:
        if cell_is_filled():
            ch+=1
        else:
            ch=0
        if ch==3:
            break
        move_right()

if __name__ == '__main__':
    run_tasks()
