from tkinter import *

window= Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=400)

def calculate_km():
    miles=float(user_entry.get())
    km=miles*1.609
    my_label.config(text=f"{km} km")

user_entry = Entry()
user_entry.grid(row=1,column=1)

calculate_button=Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2,column=1)

my_label= Label(text="KM")
my_label.grid(row=3,column=1)




window.mainloop()
