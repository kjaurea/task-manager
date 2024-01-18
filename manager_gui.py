# This file should contain the code for the task manager GUI
# TEST
import tkinter as tk
from tkinter import ttk


class ManagerGUI:
    def __init__(self):
        self.root = tk.Tk()
        # code for actual GUI goes below
        # code for window size and title
        self.root.geometry('350x300')
        self.root.title("Kevin's To-Do List")

        # code for mainframe of gui (like anchor pane?)
        self.mainframe = tk.Frame(self.root)
        self.mainframe.pack(fill='both', expand=True)

        # code for text in app window
        self.app_title = ttk.Label(self.mainframe, text="To-Do List Manager", font=("Calibri", 15))
        self.app_title.grid(row=0, column=0, columnspan=2)

        # code for first text field (and corresponding label)
        self.field_1_label = ttk.Label(self.mainframe, text="Task Name", font=("Calibri", 10))
        self.field_1_label.grid(row=1, column=0, padx=10)
        self.text_field_1 = ttk.Entry(self.mainframe)
        self.text_field_1.grid(row=1, column=1, pady=10)

        # code for second text field (and corresponding label)
        self.field_2_label = ttk.Label(self.mainframe, text="Task Due Date", font=("Calibri", 10))
        self.field_2_label.grid(row=2, column=0, padx=10)
        self.text_field_2 = ttk.Entry(self.mainframe)
        self.text_field_2.grid(row=2, column=1, pady=10)

        # code for third text field (and corresponding label)
        self.field_3_label = ttk.Label(self.mainframe, text="Task Due Time", font=("Calibri", 10))
        self.field_3_label.grid(row=3, column=0, padx=10)
        self.text_field_3 = ttk.Entry(self.mainframe)
        self.text_field_3.grid(row=3, column=1, pady=10)

        # code for fourth text field (and corresponding label)
        self.field_4_label = ttk.Label(self.mainframe, text="Task Description", font=("Calibri", 10))
        self.field_4_label.grid(row=4, column=0, padx=10)
        self.text_field_4 = ttk.Entry(self.mainframe)
        self.text_field_4.grid(row=4, rowspan=2, column=1, pady=10, sticky='NWES')

        # mainloop() is needed at end to show actual window
        self.root.mainloop()
        return
