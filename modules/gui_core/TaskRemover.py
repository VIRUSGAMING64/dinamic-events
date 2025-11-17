from threading import Thread
from customtkinter import *
from modules import *
from CTkMessagebox import CTkMessagebox as Messagebox

class TaskRemover(CTk):
    selected = None

    def __init__(self):
        super().__init__()
        self.x_size = 256
        self.y_size = 400
        self.title("Task Remover")
        
        self.geometry(f"{self.x_size}x{self.y_size}")
        
        self.eventos = CTkComboBox(self,200,command=self.update_label)
        self.eventos.pack()
        self.eventos.place()
        
        self.remove_button = CTkButton(self, text="Remove this event", command=self.remove)
        self.remove_button.pack()
        self.remove_button.place(
            x = (self.x_size - self.remove_button._current_width)//2,
            y = self.y_size - self.remove_button._current_height
        )
        
        self.info = CTkLabel(self,text="INFORMATION")
        self.info.pack()
        self.info.place(y = 28 , x = 0)


        self.update_thread = Thread(target = self.update_combo, daemon = True).start()


    def update_combo(self):
        try:

            while True:
                print("updating remover")
                labels = build_event_option_labels(calendar.events)
                self.eventos.configure(values = labels)
                time.sleep(3)

        except Exception as e:
            log(f"eror in update_combo [{e}]")

    def remove(self):
        if self.selected == None:
            Messagebox(
                self, 300, 300, "[ERROR] Select one event"
            )
            return
        calendar.remove(self.selected)
        Messagebox(self,300,300,"REMOVED", F"TASK [{self.selected}] REMOVED")
        calendar.save_json_data()
    

    def update_label(self,selected):
        idx = parse_event_option(selected)
        if idx is None or idx >= len(calendar.events):
            self.selected = None
            return
        self.selected = idx
        ev = calendar.events[idx]
        self.info.configure(text = format_event_info(ev))