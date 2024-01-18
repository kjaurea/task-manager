from task import Task
from to_do_list import ToDoList
from datetime import *
import tkinter as tk

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    sample_task = Task(title="Closet Case", goaldate=date(2024, 1, 18), goaltime=time(17, 30),
                       description="Clean the dang closet")

    sample_task2 = Task("Make pasta", date(2024, 1, 17), time(17, 00), "Make butternut pasta for dinner")
    sample_task3 = Task("Play Grounded", date(2024, 1, 17), time(21, 00), "Kill more stinkbugs")

    newlist = ToDoList()
    newlist.add_task(sample_task)
    newlist.add_task(sample_task2)
    newlist.add_task(sample_task3)
    print("\n")
    newlist.print_priority_list()
    print("\n")
    sample_task.print_attribute("description")

# create task manager
# create a class for tasks, in its own file
# create a class for the to-do list, in its own file
# create a GUI  using tkinter, in its own file
# connect files by importing
