# This file should contain the class for tasks
class Task:

    # constructor
    def __init__(self, title, goaldate, goaltime, description):
        self.title = title
        self.goaldate = goaldate
        self.goaltime = goaltime
        self.description = description

    # print method (for testing)
    def print_task(self):
       print(f'Task: {self.title}\nDate: {self.goaldate}\nTime: {self.goaltime}\nDescription: {self.description}')
