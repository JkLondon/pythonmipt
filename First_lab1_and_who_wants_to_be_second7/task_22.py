#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
	x=0
	y=0
	if wall_is_beneath() and wall_is_on_the_right():
		fill_cell()
		return
	while wall_is_beneath()==0:
		x+=1
		move_down()
	while wall_is_on_the_right()==0:
		y+=1
		move_right()
	move_up(x)
	move_left(y)
	for i in range(x):
		for j in range(y):
			fill_cell()
			move_right()
		fill_cell()
		if wall_is_beneath()==1:
			for i in range(y):
				fill_cell()
				move_right()
			fill_cell()
			move_left(y)
		else:
			move_down()
			move_left(y)
	for i in range(y):
		fill_cell()
		move_right()
	fill_cell()
	move_left(y)	
if __name__ == '__main__':
    run_tasks()
