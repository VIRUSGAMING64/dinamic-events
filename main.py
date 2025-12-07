from customtkinter import *
from CTkMessagebox import CTkMessagebox as Messagebox
from modules.gui_core import *
from ctkdlib import *
from modules.gui_core.EventDeffiner import EventCreator
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

        self.button_res_adder = CTkButton(self,text="Add Resource",command=self.open_res_adder)
        self.button_res_adder.pack()
        self.button_res_adder.place(
            x=self.size_x - self.button_res_adder._current_width,
            y=60
        )

        self.button_ev_adder = CTkButton(self,text="Define new event",command=self.open_event_creator)
        self.button_ev_adder.pack()
        self.button_ev_adder.place(
            x=self.size_x - self.button_ev_adder._current_width,
            y=90
        )
        self.ev_creator = None
        self.res_adder = None
        self.currents = CTkComboBox(self,width=512 - 140,command=self.get_information,state="readonly")
        self.currents.set("Select current a task")
        self.currents.pack()
        self.currents.place(x=0,y=0)

        self.info = CTkLabel(self,text="INFORMATION:")
        self.info.pack()
        self.info.place(x=0,y=30)
        self.ev_info_select = None

        self.prog = CTkProgressBar(
            self, 
            height=20, 
            width=512 - 140,
            variable=Variable(None, 0)
        )
        self.prog.pack()
        print( self.info._current_width )
        self.prog.place(x = 0, y = 30 + 28 * 5)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        

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
            try:
                self._bar_updater()
                time.sleep(10)
            except Exception as e:
                log(str(e) + " in bar updater ")

    def update(self):
        try:
            self.currents.configure(values = build_event_option_labels(calendar.events))    
        except Exception as e:
            log(str(e) + " in bar updater ")

    def open_event_creator(self):
        if self.ev_creator != None:
            try:
                self.ev_creator.destroy()
                self.ev_creator = None
            except Exception as e:
                log(f"already destroyed [{e}]")
            
        self.ev_creator = EventCreator()
        self.ev_creator.resizable(False,False)

    def open_res_adder(self):
        if self.res_adder != None:
            try:
                self.res_adder.destroy()
                self.res_adder = None
            except Exception as e:
                log(f"already destroyed [{e}]")
        self.res_adder = RessAdder()
        self.res_adder.resizable(False,False)

    def remove_task(self):
        if self.task_remover != None:
            try:
                self.task_remover.destroy()
                self.task_remover = None
            except Exception as e:
                log(f"already destroyed [{e}]")
        
        self.task_remover = TaskRemover()
        self.task_remover.resizable(False,False)

    def create_task(self):
        if self.task_creator != None:
            try:
                self.task_creator.destroy()
                self.task_creator = None
            except Exception as e:
                log(f"already destroyed [{e}]")
            
        self.task_creator = TaskCreator()
        self.task_creator.resizable(False,False)

    def run_daemon(self):
        self.t1 = Thread(target=self.bar_updater,daemon=True)
        self.t2 = Thread(target=self.updater,daemon=True)
        self.t1.start()
        self.t2.start()

    def updater(self):
        while True:
            self.update()
            time.sleep(3)

    def on_closing(self):
        if self.task_creator is not None:
            try:
                self.task_creator.destroy()
            except:
                pass
        if self.task_remover is not None:
            try:
                self.task_remover.destroy()
            except:
                pass
        if self.ev_creator is not None:
            try:
                self.ev_creator.destroy()
            except:
                pass
        if self.res_adder is not None:
            try:
                self.res_adder.destroy()
            except:
                pass
        self.destroy()
        import sys
        sys.exit(0)


calendar.remove_old_events()
APP = app()
APP.resizable(False,False)
APP.run_daemon()
APP.mainloop()
print("don't end application")