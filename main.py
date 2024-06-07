import tkinter
from tkinter import *

template = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer rutrum, orci vestibulum ullamcorper ultricies, lacus quam ultricies odio, vitae placerat pede sem sit amet enim. Et harum quidem rerum facilis est et expedita distinctio. Pellentesque sapien. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis."

window = Tk()
window.config(padx=100, pady=50, bg="#EEEEEE")
window.resizable(False, False)
window.title("Typing Speed Test 3000")

app_label = Label(window, text="Typing Speed Test 3000", fg="#686D76", bg="#EEEEEE", font=("Verdana", 22, "bold"))
app_label.grid(column=0, row=0, pady=20)

canvas = Canvas(width=400, height=229, bg="#EEEEEE", highlightthickness=0)
img = PhotoImage(file="image.png")
canvas.create_image(200, 115, image=img)
canvas.grid(column=0, row=1)

template_text = Label(window, text=template, fg="#373A40", bg="#EEEEEE", font=("Verdana", 12, "bold"), wraplength=400, justify="left")
template_text.grid(column=0, row=3, pady=20)

input_text = Entry(window, width=64)
input_text.grid(column=0, row=4, pady=20)

window.mainloop()