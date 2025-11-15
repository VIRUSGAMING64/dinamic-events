import tkinter as tk
from customtkinter import *
import datetime
from modules import *
from CTkMessagebox import CTkMessagebox as Messagebox

class TaskRemover(CTk):
    def __init__(self):
        super().__init__()
        self.x_size = 256
        self.y_size = 128
        self.title("Task Remover")
        self.geometry(f"{self.x_size}x{self.y_size}")
        #TODO create selector of events
        self.ElimButton = CTkButton(self,text="remove this event", command=self.remove)
        self.ElimButton.pack()
        self.ElimButton.place(
            x = (self.x_size - self.ElimButton._current_width)//2,
            y = self.y_size - self.ElimButton._current_height
        )

    def remove(self):
        #! get selected event
        #id is the index of the event in calendar.events
        calendar.remove(id)
        pass

    def get_currents(self):
        return calendar.list_events()

