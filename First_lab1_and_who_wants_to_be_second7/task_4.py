#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
	r=wall_is_on_the_right()
	l=wall_is_on_the_left()
	u=wall_is_above()
	d=wall_is_beneath()
	if d==0:
		move_down(1)
	elif r==0:
		move_right(1)
	elif l==0:
		move_left(1)
	else:
		move_up(1)

if __name__ == '__main__':
    run_tasks()
