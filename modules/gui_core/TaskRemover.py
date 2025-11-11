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
        #TODO create selector

    def get_currents():
        return calendar.list_events()

