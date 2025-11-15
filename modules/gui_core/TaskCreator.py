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

        self.begin_time.bind("<Return>", lambda event: "break")
        self.end_time.bind("<Return>", lambda event: "break")


        self.end_time.place(x=self.x_size-200,y=28)
        self.end_time_label.place(x=self.x_size-200-65,y=28)
        
        self.begin_time.insert("1.0",text=f"{start_time.replace("T"," AT ")}")
        self.end_time.insert("1.0",text=f"{start_time.replace("T"," AT ")}")
        """
        SHOW RESOURCESS THAT THIS EVENT NEED
        """
        self.tasks = CTkComboBox(self,width=280,values=self._get_tasks(),state="readonly", command=self._get_deps)
        self.tasks.set("Select a task")
        self.tasks.pack()
        self.tasks.place(x=0,y=56)

        """
        DEPENDENCY LABEL
        """
        self.dependency_label = CTkLabel(self,text="Dependencies:\n" )
        self.dependency_label.pack()
        self.dependency_label.place(x=0,y=90)


        """
        BUTTONS
        """
        self.b_add = CTkButton(self,text="Add this event",command=self.add_event)
        self.b_add.pack()
        self.b_add.place(x=70, y = self.y_size - 56)


        self.sug = CTkButton(self,text="Adjust date",command=self.adjust)
        self.sug.pack()
        self.sug.place(x=70, y = self.y_size - 56 * 2)


    def _get_deps(self,selected):
        deps = []
        print(selected,calendar.aviable_tasks)
        res = calendar.aviable_tasks[selected]["resources"]
        for t in res:
            deps.append(t["name"])
        
        A = set()
        for i in deps:
            A.add(i)
            for x in get_sources_dependency(calendar.resources,i):
                A.add(x)
        
        print(A)
        deps = []
        for i in A:
            deps.append(i)
        print(deps)
        org = self.dependency_label.cget("text").split(':')[0]
        ne = ""
        for i in deps:
            ne += f"- {i}\n"

        self.dependency_label.configure(text= org + ":\n" + ne)
        return deps

    def __sugest(self,l:int , r : int, resources :list) -> list:
        print("running...")
        L = calendar.sugest_bruteLR(l,r,resources)
        print("finded...")
        R = L + datetime.timedelta(minutes=r - l)
        return L,R

    def adjust(self):
       
        print("[SUGEST_FUNCTION]")
        begin = self.begin_time.get("1.0","19.0").replace(" AT ","T").replace("\n","")
        end = self.end_time.get("1.0","19.0").replace(" AT ","T").replace("\n","")
        valid =  CheckISODate(begin)
        valid != CheckISODate(end)
        print("intializing sugest...")
        if valid == 0:
            self.Invalid("date")
            return False
        
        begin = datetime.datetime.fromisoformat(begin)
        end = datetime.datetime.fromisoformat(end)
        
        if begin == end:
            self.Invalid("[begin == end]")
            return False

        #! get resources of the task
        res = self._get_deps(self.tasks.get())
        
        print(res)

        l,r = self.__sugest(tominute(begin),tominute(end),res)
        #! combert l,r to datetime isoformat

        print(l.isoformat())
        print(r.isoformat())
        return True
        


    def _get_tasks(self) -> list:
        tasks = []
        for x in calendar.aviable_tasks:
            tasks.append(x)
        tasks.sort()
        return tasks
    
    def Invalid(self,data):
        Messagebox(
            height=100,
            width=100,
            title="ERROR",
            message=f"Invalid {data}",
            option_1="Accept"
        )

    def _add_event(self):
        begin = self.begin_time.get("1.0","19.0").replace(" AT ","T").replace("\n","")
        end = self.end_time.get("1.0","19.0").replace(" AT ","T").replace("\n","")
        valid = CheckISODate(begin)
        valid *= CheckISODate(end)
    
        if valid == 0:
            self.Invalid("date")
            return False

        task_name = self.tasks.get()

        res = self._get_deps(task_name)

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
            return False
        elif response == "Accept":
            added = self._add_event()

        if added:
            self.destroy()
        else:
            #! process not added
            Messagebox(self,message="No added")
            return

    def sugest(self):
        pass

    def verifict(self):
        pass