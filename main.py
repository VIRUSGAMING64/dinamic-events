from customtkinter import *
from CTkMessagebox import CTkMessagebox as Messagebox
from CTkTable import CTkTable
from modules.gui_core import *
from tktimepicker import *
from ctkdlib import *
from modules import *
from threading import Thread

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


        self.currents = CTkComboBox(self,width=512 - 140,command=self.get_information,state="readonly")
        self.currents.set("Select current a task")
        self.currents.pack()
        self.currents.place(x=0,y=0)


        self.info = CTkLabel(self,text="INFORMATION:\n")
        self.info.pack()
        self.info.place(x=0,y=30)
        Thread(target=self.updater,daemon=True).start()



    def get_information(self,selected):

        base = "INFORMATION:\n"

        id = selected.split("]")[0][1:]
        id = int(id)
        ev = calendar.events[id]
        base += f"Task name: {ev.task}\n"
        base += f"Date range: {ev.date[0]} TO {ev.date[1]}\n"
        base += f"Time range: {ev.time[0]} TO {ev.time[1]}\n"
        base += f"Resources needed: {', '.join(ev.need_resources)}\n"
        base += f"Notes: {ev.notes}\n"

        self.info.configure(text = base)


    def update(self):
        L = []
        for i in range(len(calendar.events)):
            id = i
            ev = calendar.events[i]
            L.append(f"[{id}] {ev.task} FROM {ev.date[0]} TO ...")

        self.currents.configure(values = L)
    

    def remove_task(self):
        if self.task_remover != None:
            try:
                self.task_remover.destroy()
                self.task_remover = None
            except Exception as e:
                log(f"already destroyed [{e}]")
        
        self.task_remover = TaskRemover()
        self.task_remover.mainloop()
        self.task_remover = None

    def create_task(self):
        if self.task_creator != None:
            try:
                self.task_creator.destroy()
                self.task_creator = None
            except Exception as e:
                log(f"already destroyed [{e}]")
            
        self.task_creator = TaskCreator()
        self.task_creator.mainloop()
        self.task_creator = None

    def __destructor(self):
        if self.task_creator != None:
            self.task_creator.destroy()
        if self.task_remover != None:
            self.task_remover.destroy()

    def updater(self):
        while True:
            self.update()
            time.sleep(3)

APP = app()
APP.mainloop()