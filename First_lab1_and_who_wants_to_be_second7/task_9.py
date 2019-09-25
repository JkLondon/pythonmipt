#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
	while 1==1:
		if ( wall_is_above() and wall_is_beneath() )==0:
			fill_cell()
		if wall_is_on_the_right()==0: 
			move_right(1) 
		else:
			break


if __name__ == '__main__':
    run_tasks()
