from customtkinter import *
from CTkMessagebox import CTkMessagebox as Messagebox
from CTkTable import CTkTable
from modules.customGUI import *
from tktimepicker import *
from ctkdlib import *
from modules import *

class app(CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter App")
        self.geometry("1024x512")

        self.button = CTkButton(self, text="Add event", command=self.add_event,width=300)
        self.tasks  = CTkComboBox(self,width=300,values=self._get_tasks())
        self.calendar = CTkCalendar(self,height=150,width=300)
        self.TimeSelector = TimeSelector(self,width=16)
        self.DurationInput = CTkTextbox(self,width=300,height=28)

        self.button.pack(pady=0)
        self.tasks.pack(pady=0)
        self.calendar.pack(pady=0)
        self.TimeSelector.pack(pady=0)
        self.DurationInput.pack(pady=0)

        self.button.place(x=724)
        self.tasks.place(x=724, y=28)
        self.calendar.place(x=724, y=56)
        self.TimeSelector.place(x=724, y=206)
        self.DurationInput.place(x=724, y=234)
      
      
    def _get_tasks(self) -> list:
        tasks = []
        for x in calendar.aviable_tasks:
            tasks.append(x)
        tasks.sort()
        return tasks


    def add_event(self):
        message = Messagebox(
            height=100,
            width=100,
            title="Adding event",
            message="Add this event??",
            option_1="Accept",
            option_2="Cancel"
        )
        response = message.get()
        if response == "Cancel":
            print("User canceled the event addition.")
        elif response == "Accept":
            print("Event added successfully.")


    def remove_event(self):
        pass

    def sugest(self):
        pass

    def verifict(self):
        pass

    def ShowCalendar(self):
        pass

app().mainloop()