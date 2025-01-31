import tkinter as tk
root = tk.Tk ()
root.title("parsa zare") # the title 
root.geometry(("200x200")) # display  screen size

messages = [
    "Will you marry me?","Do you love me?","You are a bit all of right, aren't you?","Are you in the mood for fun?"
,"A romatic dinner at restaurant or a great Netflix and Chill",
 "Your ex or me?" ] #the list of ...
counter = 0  # for the numver of the list

def no(): # the function of no
    global counter
    if counter < len("messages"):
        message_label.config(text=messages[counter])
        counter += 1  


 
def yes(): # teh function of yes
    message_label.config(text="I love you my pretty girlfriend, call me now")

 
message_label = tk.Label(root, text="Will you marry me?",font = ("vazir bold", 14))
message_label.pack(pady=20)

yes_botton = tk.Button(root,text="YES",command=yes, font=("vazir bold", 12))
yes_botton.pack(side="left", padx=12)

no_botton = tk.Button(root,text="NO",command=no, font=("vazir bold", 12))
no_botton.pack(side="right", padx=12)

root.mainloop()
