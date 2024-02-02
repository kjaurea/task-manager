# This file should contain the code for the task manager GUI
# TEST
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from datetime import *
from tkcalendar import Calendar, DateEntry
import customtkinter as ctk
from customtkinter import StringVar


class ManagerGUI:
    def __init__(self):
        self.window = ctk.CTk()

        # code for window title and dimensions
        self.window.title("Kevin's To-Do List")
        self.window.geometry("450x350")

        # code for application title text and instructions
        self.app_title = ctk.CTkLabel(self.window, text="To-Do List Manager", font=("Calibri", 20))
        self.app_title.grid(row=0, column=1, columnspan=2)
        self.app_instructions = ctk.CTkLabel(self.window, text="Enter task details and click submit",
                                             font=("Calibri", 14))
        self.app_instructions.grid(row=1, column=1, columnspan=2)

        # code for first input field and corresponding label (Task Name)
        self.task_name_label = ctk.CTkLabel(self.window, text="Task Name")
        self.task_name_label.grid(row=3, column=0, padx=10, pady=10)
        self.task_name_field = ctk.CTkEntry(self.window, width=250, border_color="black", border_width=2)
        self.task_name_field.grid(row=3, column=1, columnspan=3)

        # code for second input field and corresponding label (Goal Date)
        self.goal_date_label = ctk.CTkLabel(self.window, text="Goal Date")
        self.goal_date_label.grid(row=4, column=0, padx=10, pady=10)
        self.goal_date_calendar = DateEntry(self.window, width=12, border_color="black", border_width=2,
                                            font=("Calibri", 14))
        self.goal_date_calendar.grid(row=4, column=1, columnspan=2)
        self.goal_date_calendar.grid(row=4, column=1, columnspan=2)
        # TODO: fix the date thing...no customTKinter version????

        # code for third input field and corresponding label (Goal Time)
        self.goal_time_label = ctk.CTkLabel(self.window, text="Goal Time")
        self.goal_time_label.grid(row=5, column=0, padx=10, pady=10)
        self.goal_time_hour = ctk.CTkComboBox(self.window,
                                              values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                                              width=65, font=("Calibri", 14))
        self.goal_time_hour.grid(row=5, column=1)
        self.goal_time_minute = ctk.CTkComboBox(self.window, values=["00", "15", "30", "45"], width=80,
                                                font=("Calibri", 14))
        self.goal_time_minute.grid(row=5, column=2)
        self.goal_ampm_frame = ctk.CTkFrame(self.window)
        self.goal_ampm_frame.grid(row=5, column=3)
        self.radio_var = StringVar()
        self.goal_time_am = ctk.CTkRadioButton(self.goal_ampm_frame, variable=self.radio_var, radiobutton_width=15,
                                               radiobutton_height=15,
                                               border_width_unchecked=3, border_width_checked=4, text="A.M.",
                                               value="am", font=("Calibri", 12))
        self.goal_time_am.pack(pady=(2, 0), padx=4)
        self.goal_time_pm = ctk.CTkRadioButton(self.goal_ampm_frame, variable=self.radio_var, radiobutton_width=15,
                                               radiobutton_height=15,
                                               border_width_unchecked=3, border_width_checked=4, text="P.M.",
                                               value="pm", font=("Calibri", 12))
        self.goal_time_pm.pack(pady=(0, 2), padx=4)
        self.radio_var.set("am") #TODO: need to set am as default? It keeps thinking PM selected....

        # code for fourth input field and corresponding label (Description)
        self.task_desc_label = ctk.CTkLabel(self.window, text="Task Description")
        self.task_desc_label.grid(row=6, column=0, padx=10, pady=10)
        self.task_desc_field = ctk.CTkTextbox(self.window, width=300, height=80, wrap="word", border_color="black",
                                              border_width=2, font=("Calibri", 12))
        self.task_desc_field.grid(row=6, column=1, columnspan=3, pady=(20, 0))

        # code for submission button
        self.submit_button = ctk.CTkButton(self.window, text="Add Task", command=self.submit_button_callback)
        self.submit_button.grid(row=7, column=1, columnspan=2, pady=10)

        # mainloop() is needed at end to show actual window. Code above mainloop is executed before opening window
        self.window.mainloop()

    def submit_button_callback(self):
        new_task_name = self.task_name_field.get()
        new_task_date = self.goal_date_calendar.get()
        # new_task_date = datetime.strptime(self.goal_date_calendar.get(), '%m/%d/%Y').date() #TODO: doesn't work. Datepicker already returns date type???
        new_task_desc = self.task_desc_field.get(1.0,
                                                 "end-1c")  # TODO: finish converting datetime date and datetime time...
        new_task_hour = int(self.goal_time_hour.get())
        if self.goal_time_pm:
            print("PM selected")
            new_task_hour += 12
            print(new_task_hour)
        new_task_minute = int(self.goal_time_minute.get())
        new_task_time = time(hour=new_task_hour, minute=new_task_minute, second=0)

        print(new_task_name)
        print(new_task_date)
        print(new_task_desc)
        print(new_task_time)

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
