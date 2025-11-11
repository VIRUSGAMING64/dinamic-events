import tkinter as tk
from customtkinter import *
import datetime
from modules import *
from CTkMessagebox import CTkMessagebox as Messagebox

class TaskCreator(CTk):
    def __init__(self):
        super().__init__()
        self.title("TASK ADDER")
        self.x_size = 280
        self.y_size = 300
        self.geometry(f"{self.x_size}x{self.y_size}")
        
        """
            TIME LAVELS AND TEXTSBOXS
        """        
        self.begin_time_label = CTkLabel(self,text="Begin time:")
        self.end_time_label = CTkLabel(self,text="End time:")
        
        self.begin_time = CTkTextbox(self,height=28,border_color="blue")      
        self.end_time = CTkTextbox(self,height=28,border_color="blue")  

        start_time = datetime.datetime.now().isoformat().rsplit(":",1)[0]
        print(start_time)

        self.begin_time.pack(pady=20)
        self.end_time.pack(pady=20)
        self.begin_time_label.pack(pady=0)
        self.end_time_label.pack(pady=0)

        self.begin_time.place(x=self.x_size-200,y=0)
        self.begin_time_label.place(x=self.x_size-200-75,y=0)

        self.end_time.place(x=self.x_size-200,y=28)
        self.end_time_label.place(x=self.x_size-200-65,y=28)
        
        self.begin_time.bind("<Return>", lambda event: "break")
        self.end_time.bind("<Return>", lambda event: "break")

        self.begin_time.insert("1.0",text=f"{start_time.replace("T"," AT ")}")
        self.end_time.insert("1.0",text=f"{start_time.replace("T"," AT ")}")
        """
        BUTTONS
        """
        self.b_add = CTkButton(self,text="Add this event",command=self.add_event)
        self.b_add.pack()
        self.b_add.place(x=70, y = self.y_size - 56)

    def CheckDate(self,date:str): 
        try:
            print(date)
            date = date.split("-")
            year = int(date[0])
            mo = int(date[1])
            print(year,mo)
            if int(mo) > 12 or int(mo) <= 0:
                return 0
            d_h = date[2].split("T")
            h = d_h[1]
            d = int(d_h[0])
            h = h.split(':')

            print(h,d,mo,year)

            if int(h[0]) >= 24 or int(h[0]) < 0:
                return 0
            if int(h[1]) >= 60 or int(h[1]) < 0:
                return 0
            
            d31 = [1,3,5,7,8,10,12]
            d28 = [2]
            d30 = [4,6,9,11]

            if d <= 0:
                return 0

            if mo == 2 and d > 28:
                return 0
            if mo in d31 and d > 31:
                return 0
            if mo in d30 and d > 30:
                return 0
            
            return 1


        except Exception as e:
            log.log(f"error checking date [{e}]")
            return 0

    def _get_tasks(self) -> list:
        tasks = []
        for x in calendar.aviable_tasks:
            tasks.append(x)
        tasks.sort()
        return tasks
    
    def Invalid(self,data):
        message = Messagebox(
            height=100,
            width=100,
            title="ERROR",
            message=f"Invalid {data}",
            option_1="Accept"
        )

    def _add_event(self):
        begin = self.begin_time.get("1.0","19.0").replace(" AT ","T").replace("\n","")
        end = self.end_time.get("1.0","19.0").replace(" AT ","T").replace("\n","")
        valid = self.CheckDate(begin)
        valid *= self.CheckDate(end)

        if valid == 0:
            self.Invalid("date")
            return

        task_name = None
        #! get name of the task to do

        res = []
        #! get resources of this task

        new = event(
            {
                "name": task_name,
                "time-range": [
                    tominute(datetime.datetime.fromisoformat(begin)),
                    tominute(datetime.datetime.fromisoformat(end))
                ],
                "resources": res,
                "date-range": [begin,end]
            }
        )
        if new.start == new.end:
            message = Messagebox(
                height=100,
                width=100,
                title="ERROR",
                message="The end of the task is equal to the begin !",
                option_1="Accept"
            )
            message.get()
            return False
        
        added = calendar.add_event(new)
        if added:
            calendar.save_json_datas()
        print(f"added: [{added}]")
        return added

    def add_event(self):
        message = Messagebox(
            height=100,
            width=100,
            title="Adding event",
            message="Add this event?",
            option_1="Accept",
            option_2="Cancel"
        )
        response = message.get()
        if response == "Cancel":
            print("User canceled the event addition.")
        elif response == "Accept":
            added = self._add_event()

        if added:
            self.destroy()
        else:
            #! process not added
            Messagebox(self,message="No added")
            return

    def remove_event(self):
        pass

    def sugest(self):
        pass

    def verifict(self):
        pass

    def ShowCalendar(self):
        pass
