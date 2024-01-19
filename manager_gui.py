# This file should contain the code for the task manager GUI
# TEST
import tkinter as tk
from tkinter import ttk

from tktimepicker import AnalogPicker, AnalogThemes
from tkcalendar import Calendar, DateEntry
import customtkinter as ctk

class ManagerGUI:
    def __init__(self):
        self.window = ctk.CTk()

        # code for window title and dimensions
        self.window.title("Kevin's To-Do List")
        self.window.geometry("400x600")

        # code for application title text and instructions
        self.app_title = ctk.CTkLabel(self.window, text="To-Do List Manager", font=("Calibri", 20))
        self.app_title.grid(row=0, column=1, columnspan=2)
        self.app_instructions = ctk.CTkLabel(self.window, text="Enter task details and click submit", font=("Calibri", 14))
        self.app_instructions.grid(row=1, column=1, columnspan=2)

        # code for first input field and corresponding label
        self.task_name_label = ctk.CTkLabel(self.window, text="Task Name")
        self.task_name_label.grid(row=3, column=0, padx=10, pady=10)
        self.task_name_field = ctk.CTkEntry(self.window)
        self.task_name_field.grid(row=3, column=1, columnspan=2)

        # code for second input field and corresponding label
        self.goal_date_label = ctk.CTkLabel(self.window, text="Goal Date")
        self.goal_date_label.grid(row=4, column=0, padx=10, pady=10)
        self.goal_date_calendar = DateEntry(self.window, width=12, font=("Calibri", 14))
        self.goal_date_calendar.grid(row=4, column=1, columnspan=2)

        # code for third input field and corresponding label
        self.goal_time_label = ctk.CTkLabel(self.window, text="Goal Time")
        self.goal_time_label.grid(row=5, column=0, padx=10, pady=10)
        self.goal_time_picker = AnalogPicker(self.window)
        self.goal_time_picker.grid(row=5, column=1, columnspan=2)

        # code for fourth input field and corresponding label


        # code for submission button
        self.submit_button = ctk.CTkButton(self.window, text="Add to list", command=self.submit_button_callback)
        self.submit_button.grid(row=6, column=2)

        # mainloop() is needed at end to show actual window. Code above mainloop is executed before opening window
        self.window.mainloop()

    def submit_button_callback(self):
        print("Task submitted")

    # def __init__(self):
    #     self.root = ctk.CTk()
    #     # code for actual GUI goes below
    #     # code for window size and title
    #     self.root.geometry('350x300')
    #     self.root.title("Kevin's To-Do List")
    #
    #     # code for mainframe of gui (like anchor pane?)
    #     self.mainframe = ctk.Frame(self.root)
    #     self.mainframe.pack(fill='both', expand=True)
    #
    #     # code for text in app window
    #     self.app_title = ttk.Label(self.mainframe, text="To-Do List Manager", font=("Calibri", 15))
    #     self.app_title.grid(row=0, column=0, columnspan=2)
    #
    #     # code for first text field (and corresponding label)
    #     self.field_1_label = ttk.Label(self.mainframe, text="Task Name", font=("Calibri", 10))
    #     self.field_1_label.grid(row=1, column=0, padx=10)
    #     self.text_field_1 = ttk.Entry(self.mainframe)
    #     self.text_field_1.grid(row=1, column=1, pady=10)
    #
    #     # code for second text field (and corresponding label)
    #     self.field_2_label = ttk.Label(self.mainframe, text="Task Due Date", font=("Calibri", 10))
    #     self.field_2_label.grid(row=2, column=0, padx=10)
    #     self.text_field_2 = ttk.Entry(self.mainframe)
    #     self.text_field_2.grid(row=2, column=1, pady=10)
    #
    #     # code for third text field (and corresponding label)
    #     self.field_3_label = ttk.Label(self.mainframe, text="Task Due Time", font=("Calibri", 10))
    #     self.field_3_label.grid(row=3, column=0, padx=10)
    #     self.text_field_3 = ttk.Entry(self.mainframe)
    #     self.text_field_3.grid(row=3, column=1, pady=10)
    #
    #     # code for fourth text field (and corresponding label)
    #     self.field_4_label = ttk.Label(self.mainframe, text="Task Description", font=("Calibri", 10))
    #     self.field_4_label.grid(row=4, column=0, padx=10)
    #     self.text_field_4 = ttk.Entry(self.mainframe)
    #     self.text_field_4.grid(row=4, rowspan=2, column=1, pady=10, sticky='NWES')
    #
    #     # mainloop() is needed at end to show actual window
    #     self.root.mainloop()
    #     return
