from customtkinter import *
from CTkMessagebox import CTkMessagebox
from modules.events import *
from modules.utils import *

class EventShower(CTk):
    def __init__(self, event_list:list[event] = []):
        super().__init__()
        self.resizable(False, False)

        self.title("event shower")
        self.geometry("600x500")
        
        self.scrollable_frame = CTkScrollableFrame(master=self, width=200, height=300, label_text="events running")
        self.scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.buttons = []
        for i in range(len(event_list)):
            item = CTkButton(
                master=self.scrollable_frame, 
                text=f"{i} - {event_list[i].task}  {event_list[i].date[0]} TO {event_list[i].date[1]}", 
                command=lambda: self.button_click(event_list[i])
            )
            item.pack(pady=2, padx=2)
            self.buttons.append(item)

        self.horizontal_frame = CTkScrollableFrame(master=self, orientation="horizontal", height=50)
        self.horizontal_frame.pack(pady=10, fill="x")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def button_click(self, ev:event):
        ev_info = format_event_info(ev)
        CTkMessagebox(title="Event Information", message=ev_info)

    def on_closing(self):
        self.destroy()
