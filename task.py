# This file should contain the class for tasks
from datetime import *


class Task:

    # constructor (includes dtvalue used for priority)
    def __init__(self, title, goaldate, goaltime, description):
        self.title = title
        self.goaldate = goaldate
        self.goaltime = goaltime
        self.dtvalue = datetime.combine(goaldate, goaltime)
        self.description = description

    def __repr__(self):
        return f'Title={self.title} | Goal date={self.goaldate} | Goal time={self.goaltime} | ' \
               f'Description={self.description}'

    # print method (for testing)
    def print_task(self):
        print(f'Task: {self.title}\nDate: {self.goaldate}\nTime: {self.goaltime}\nDescription: {self.description}')

    def print_attribute(self, attributename):
        if attributename == "description":
            print(f'{self.title} description: {self.description}')
        elif attributename == "dtvalue":
            print(f'{self.title} datetime: {self.dtvalue}')
