from tkinter import *

def miles_to_km():
    mile= float(miles_input.get())
    km=round(mile*1.609)
    kilometer_result_labl.config(text=f"{km}")

window=Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=20,pady=20)

miles_input=Entry(width=6, text="some text")
miles_input.grid(column=1, row=0)

miles_labl=Label(text="Miles")
miles_labl.grid(column=2, row=0)

miles_equal_to=Label(text="Equal to:")
miles_equal_to.grid(column=0, row=1)

kilometer_result_labl=Label(text="0")
kilometer_result_labl.grid(column=1, row=1)

kilometers_labl=Label(text="Km")
kilometers_labl.grid(column=2, row=1)

calculat_button=Button(text="Calculate",command=miles_to_km)
calculat_button.grid(column=1, row=2)


window.mainloop()

