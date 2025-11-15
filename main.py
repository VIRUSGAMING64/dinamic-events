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
        self.task_creator = None
        self.task_remover = None
        self.size_x = 512
        self.size_y = 256

        self.geometry(f"{self.size_x}x{self.size_y}")


        self.ButtonTaskCreator = CTkButton(self,text="Create new task",command=self.create_task)
        self.ButtonTaskCreator.pack()
        self.ButtonTaskCreator.place(x=self.size_x - self.ButtonTaskCreator._current_width)


        self.ButtonTaskRemover = CTkButton(self,text="Remove existing task",command=self.remove_task)
        self.ButtonTaskRemover.pack()
        self.ButtonTaskRemover.place(
            x=self.size_x - self.ButtonTaskRemover._current_width,
            y=30
        )

    def remove_task(self):
        if self.task_remover != None:
            try:
                self.task_remover.destroy()
                self.task_remover = None
            except Exception as e:
                log.log(f"already destroyed [{e}]")

        
        self.task_remover = TaskRemover()
        self.task_remover.mainloop()
        self.task_remover = None

    def create_task(self):
        if self.task_creator != None:
            try:
                self.task_creator.destroy()
                self.task_creator = None
            except Exception as e:
                log.log(f"already destroyed [{e}]")
            
        self.task_creator = TaskCreator()
        self.task_creator.mainloop()
        self.task_creator = None

    def __destructor(self):
        if self.task_creator != None:
            self.task_creator.destroy()
        if self.task_remover != None:
            self.task_remover.destroy()

APP = app()
APP.mainloop()