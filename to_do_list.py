# This file should contain the class for the to-do list
from queue import PriorityQueue
class ToDoList:

    # constructor (no other args)
    def __init__(self):
        self.todolist = PriorityQueue()

    # add a task to the Priority Queue created by the constructor based on the datetime value passed
    def add_task(self, task):
        self.todolist.put((task.dtvalue, task))

    def print_priority_list(self):
        while not self.todolist.empty():
            print(self.todolist.get())
