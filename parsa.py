import tkinter as tk
root = tk.Tk ()
root.title("parsa zare") # the title 
root.geometry(("200x200")) # display  screen size

messages = ["پس حتما گاوی؟","ایا خری"] #the list of ...
counter = 0  # for the numver of the list

def no(): # the function of no
    global counter
    if counter < len("messages"):
        message_label.config(text=messages[counter])
        counter += 1  


 
def yes(): # teh function of yes
    message_label.config(text="افرین")

 
message_label = tk.Label(root, text="ایا خری",font = ("vazir bold", 14))
message_label.pack(pady=20)

yes_botton = tk.Button(root,text="اره ",command=yes, font=("vazir bold", 12))
yes_botton.pack(side="left", padx=12)

no_botton = tk.Button(root,text="no ",command=no, font=("vazir bold", 12))
no_botton.pack(side="right", padx=12)

root.mainloop()