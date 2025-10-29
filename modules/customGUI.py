import tkinter as tk

class TimeSelector(tk.Frame):
    def __init__(self, parent,width = 28):
        super().__init__(parent,width=width)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=width)
        self.minstr=tk.StringVar(self,'30')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=width)
        self.hour.grid()
        self.min.grid(row=0,column=1)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()