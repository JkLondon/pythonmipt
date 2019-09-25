#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    while 1==1:
                if ( wall_is_above() or wall_is_beneath() )==1:
                        fill_cell()
                if wall_is_on_the_right()==0:
                        move_right(1)
                else:
                        break



if __name__ == '__main__':
    run_tasks()
