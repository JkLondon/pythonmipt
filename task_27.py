#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i=0
    move_right()
    while wall_is_on_the_right()==0:
        fill_cell()
        i+=1
        for j in range(i):
            if wall_is_on_the_right():
                break
            else:
                move_right()
    
if __name__ == '__main__':
    run_tasks()
