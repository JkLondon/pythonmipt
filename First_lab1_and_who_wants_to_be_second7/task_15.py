#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	l=wall_is_on_the_left()
	u=wall_is_above()
	if l:
		while wall_is_on_the_right()==0:
			move_right(1)
	else:
		while wall_is_on_the_left()==0:
			move_left(1)
	if u:
		while wall_is_beneath()==0:
			move_down(1)
	else:
		while wall_is_above()==0:
			move_up(1)




if __name__ == '__main__':
    run_tasks()
