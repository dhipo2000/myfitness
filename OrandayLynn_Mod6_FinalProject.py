import tkinter as tk
from tkinter import Toplevel, messagebox

class todo:
    def __init__(self, root):
        self.root = root
        #Windows design/mess around
        root.title("Tod.oM")
        root.geometry("500x300")

        #The box outline/input+display guidelines
        self.frame = tk.Frame(root)
        self.frame.grid()
        self.box = tk.Listbox(self.frame, width = 50, height = 12, selectmode = "multiple")
        self.box.grid(row = 2, column = 1, pady = 10, columnspan = 2, sticky = "n")

        #Todo list input/tk.Entry
        self.entry = tk.Entry(self.frame, width = 30)
        self.entry.grid(row = 0, column = 1, pady = 10, columnspan=2, sticky = "n")

        #Buttons
        self.addButton = tk.Button(self.frame, text = "Add task", width = 10, command = self.addTask)
        self.addButton.grid(row = 1, column = 0, sticky = "n")
        self.deleteButton = tk.Button(self.frame, text = "Delete tasks", width = 10, command = self.deleteTasks)
        self.deleteButton.grid(row = 1, column = 1, sticky = "n")
        self.clearButton = tk.Button(self.frame, text = "Clear all", width = 10, command = self.clearTask)
        self.clearButton.grid(row = 1, column = 2, sticky = "n")
        self.settingButton = tk.Button(self.frame, text = "Settings", width = 10, command = self.settingsWindow)
        self.settingButton.grid(row = 1, column = 3, sticky = "n")

    def addTask(self):
        task = self.entry.get()
        if task != "":
            self.box.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    
    def clearTask(self):
        self.box.delete(0, tk.END)
    
    def deleteTasks(self):
        try:
            index = self.box.curselection()
            for i in reversed(index):
                self.box.delete(i)
        except ModuleNotFoundError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")#Refix this later

    def settingsWindow(self):
        top = Toplevel()
        top.geometry("500x300")
        top.title("Settings")
        
    

#Creates wwondow
root = tk.Tk()
window = todo(root)
root.mainloop()