#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    i=0
    j=0
    n=0
    while wall_is_beneath()==0:
        move_down()
        n+=1
    move_up(n)
    for i in range(n+1):
        for j in range(n):
            if i!=j and i+j!=n:
                fill_cell()
            move_right()
        if i!=n and i+n!=n:
            fill_cell()
        move_left(n)
        if wall_is_beneath():
            break
        move_down()

if __name__ == '__main__':
    run_tasks()
