from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=400)
# added pad x and pad y
window.config(padx=10, pady=10)

# Label
my_labl =Label(text="I am a label", font=("Arial", 24))
my_labl["text"] = "New Text"
my_labl.config(text= "new text")
# postion text on top column and row
my_labl.grid(column=0, row=0)
my_labl.pack()

# Button
def button_clicked():
  print("i got clicked")
  my_text=input.get()
  my_labl.config(text=my_text)


button=Button(text="click me",command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

# spinbox
def spinbox_used():
  print(spinbox.get())
spinbox=Spinbox(from_=0, to=10, width=9, command=spinbox_used)
spinbox.pack()

# scale
def scale_used(value):
  print(value)
scale=Scale(from_=0, to=10, command=scale_used)
scale.pack()

# entries
entry= Entry(width=30)

entry.insert(END, string="some text")
print(entry.get())
entry.pack()

# text
text=Text(height=5, width=30)
# put curser in textbox
text.focus()
# add some text to begin with
text.insert(END, "Example of multi-line text entry")
# get's current value in textbox at line 1, character
print(text.get("1.0", END))
text.pack()

# add a checkbox
def check_buttonUsed():
# prints 1 if on, 0 if off
  print(check_state.get())
# variable to hold on to checked status
check_state=IntVar()
check_button= Checkbutton(text="is on?", variable=check_state, command=check_buttonUsed)
check_state.get()
check_button.pack()


window.mainloop()
