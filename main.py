from customtkinter import *
from CTkMessagebox import CTkMessagebox as Messagebox
from modules.gui_core import *
from ctkdlib import *
from modules import *
from threading import Thread
import PIL

set_appearance_mode("dark")

class app(CTk):

    def __init__(self):
        super().__init__()
        self.pack_propagate(False)
        self.title("Server tasks administrator")
        self.task_creator = None
        self.task_remover = None
        self.size_x = 512
        self.size_y = 256
        self.geometry(f"{self.size_x}x{self.size_y}")

        
        bg_image = CTkImage(dark_image=PIL.Image.open("templates/server1.jpg"),size = (self.size_x,self.size_y))
        self.bg = CTkLabel(self,image=bg_image,width=self.size_x,height=self.size_y,text="")
        self.bg.pack()
        self.bg.place(y=0,x=0)
    

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

        self.info = CTkLabel(self,text="INFORMATION:")
        self.info.pack()
        self.info.place(x=0,y=30)
        self.ev_info_select = None

        Thread(target=self.bar_updater,daemon=True).start()
        Thread(target=self.updater,daemon=True).start()
        self.prog = CTkProgressBar(
            self, 
            height=20, 
            width=512 - 140,
            variable=Variable(None, 0)
        )
        self.prog.pack()
        print( self.info._current_width )
        self.prog.place(x = 0, y = 30 + 28 * 5)
        

    def get_information(self,selected):
        index = parse_event_option(selected)
        if index is None or index >= len(calendar.events):
            return
        ev = calendar.events[index]
        self.ev_info_select = ev
        self.info.configure(text = format_event_info(ev))
        self._bar_updater()

    def _bar_updater(self):
        if self.ev_info_select == None:
            return

        total = self.ev_info_select.end - self.ev_info_select.start + 1
        part  = (total - (self.ev_info_select.end - tominute(datetime.datetime.now())))
        percent = part / total 

        if (percent >= 1.0) or (not calendar.is_running(self.ev_info_select)):
            calendar.remove_old_events()
            self.ev_info_select = None
            self.info.configure(text = "INFORMATION:")
            percent = 0
        
        percent = Variable(None,percent)
        self.prog.configure( variable = percent)
    
    def bar_updater(self):
        while True:
            self._bar_updater()
            time.sleep(10)

    def update(self):
        self.currents.configure(values = build_event_option_labels(calendar.events))
    

    def remove_task(self):
        if self.task_remover != None:
            try:
                self.task_remover.destroy()
                self.task_remover = None
            except Exception as e:
                log(f"already destroyed [{e}]")
        
        self.task_remover = TaskRemover()
        self.task_remover.resizable(False,False)
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
        self.task_creator.resizable(False,False)
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

calendar.remove_old_events()
APP = app()
APP.resizable(False,False)
APP.mainloop()