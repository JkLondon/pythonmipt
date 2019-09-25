#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
	while wall_is_on_the_left()==0:
		move_left(1)
	while wall_is_above() and wall_is_beneath() and wall_is_on_the_right()==0:
		move_right(1)
	if wall_is_above()==0:
		while wall_is_above()==0:
			move_up(1)
		while wall_is_on_the_left()==0:
			move_left(1)		

if __name__ == '__main__':
    run_tasks()
