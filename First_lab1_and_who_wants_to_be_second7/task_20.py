#!/usr/bin/python3

from pyrob.api import *


@task
def task_4_3():
	move_right()
	for j in range(12):
		for i in range(27):
			fill_cell()
			move_right()
		move_down()
		move_left(27)
			
if __name__ == '__main__':
    run_tasks()
