#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
	while wall_is_beneath()==0:
		move_right(1)
	while wall_is_beneath():
		move_right(1)


if __name__ == '__main__':
    run_tasks()
