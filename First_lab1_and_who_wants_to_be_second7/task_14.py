#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
	while 1==1:
		if wall_is_above()==0:
			move_up(1)
			fill_cell()
			move_down(1)
		if wall_is_beneath()==0:
			move_down(1)
			fill_cell()
			move_up(1)
		if wall_is_above()==1 and wall_is_beneath()==1:
			fill_cell()
		if wall_is_on_the_right()==0:
        		move_right(1)
		else:
			break



if __name__ == '__main__':
    run_tasks()
