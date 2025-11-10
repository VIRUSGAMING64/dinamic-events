from customtkinter import *
from CTkMessagebox import CTkMessagebox as Messagebox
from CTkTable import CTkTable
from modules.gui_core.customGUI import *
from modules.gui_core import *
from tktimepicker import *
from ctkdlib import *
from modules import *


class app(CTk):
    def __init__(self):
        super().__init__()
        self.size_x = 1024
        self.size_y = 512
        self.geometry(f"{self.size_x}x{self.size_y}")
        self.create_task()

    def create_task(self):
        self.task_creator = TaskCreator()
        self.task_creator.mainloop()
        self.task_creator = None

    def __destructor(self):
        if self.task_creator != None:
            self.task_creator.destroy()


APP = app()
APP.mainloop()