from tkinter import *
import time
import random
import sys
import os

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

def load_texts():
    texts_path = resource_path("texts.txt")
    print(f"Trying to load file from: {texts_path}")
    if os.path.exists(texts_path):
        print(f"File {texts_path} exists.")
    else:
        print(f"File {texts_path} does NOT exist.")
    with open(texts_path, 'r') as file:
        data = file.read().strip().split("\n\n")
        return data

if __name__ == "__main__":
    base_path = os.path.dirname(resource_path("texts.txt"))


texts = load_texts()
template = random.choice(texts)
start_time = None


def start_timer(event=None):
    global start_time
    if start_time is None:
        start_time = time.time()
    check_input()


def finish():
    global start_time
    if start_time is not None:
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_minutes = elapsed_time / 60

        user_input = input_text.get("1.0", "end-1c")
        letter_count = len(user_input)
        word_count = len(user_input.split())

        lpm = letter_count / elapsed_minutes
        wpm = word_count / elapsed_minutes

        result = f"Correct words: {count_correct_words(user_input)}/{len(template.split())}\n"
        result += f"Letters per minute: {lpm:.2f}\nWords per minute: {wpm:.2f}"
        result_label.config(text=result)

        start_time = None


def count_correct_words(user_input):
    correct_words = 0
    template_words = template.split()
    user_words = user_input.split()

    for i, word in enumerate(user_words):
        if i < len(template_words) and word == template_words[i]:
            correct_words += 1
    return correct_words


def check_input(event=None):
    input_text.tag_remove("incorrect", "1.0", "end")
    user_input = input_text.get("1.0", "end-1c")

    start_index = "1.0"
    for i, char in enumerate(user_input):
        template_char = template[i] if i < len(template) else ''
        end_index = input_text.index(f"{start_index} +1c")
        if char != template_char:
            input_text.tag_add("incorrect", start_index, end_index)
        start_index = end_index


def change():
    global template
    template = random.choice(texts)
    template_text.config(text=template)
    input_text.delete("1.0", END)
    result_label.config(text="")
    global start_time
    start_time = None


window = Tk()
window.config(padx=50, pady=15, bg="#EEEEEE")
window.resizable(False, False)
window.title("Typing Speed Test 3000")

app_label = Label(window, text="Typing Speed Test 3000", fg="#686D76", bg="#EEEEEE", font=("Verdana", 22, "bold"))
app_label.grid(column=0, row=0, pady=20)

canvas = Canvas(width=400, height=260, bg="#EEEEEE", highlightthickness=0)
img = PhotoImage(file=resource_path("image.png"))
canvas.create_image(200, 130, image=img)
canvas.grid(column=0, row=1)

template_text = Label(window, text=template, fg="#373A40", bg="#EEEEEE", font=("Verdana", 12, "bold"), wraplength=400, justify="left")
template_text.grid(column=0, row=3, pady=20)

button_style = {
    'bg': '#DC5F00',
    'fg': '#373A40',
    'font': ('Verdana', 12, 'bold'),
    'activebackground': '#DC5F00',
    'activeforeground': '#EEEEEE',
    'bd': 0,
    'padx': 20,
    'pady': 10
}

change_button = Button(window, text="Change text", highlightthickness=0, command=change, justify="center", **button_style)
change_button.grid(column=0, row=4, pady=20)

input_text = Text(window, width=40, height=5, font=("Verdana", 12))
input_text.grid(column=0, row=5)
input_text.bind("<KeyRelease>", start_timer)
input_text.tag_config("incorrect", background="yellow", foreground="red")

submit_button = Button(window, text="Submit", highlightthickness=0, command=finish, justify="center", **button_style)
submit_button.grid(column=0, row=6, pady=20)

result_label = Label(window, text="", fg="#373A40", bg="#EEEEEE", font=("Verdana", 12, "bold"))
result_label.grid(column=0, row=7, pady=20)

window.mainloop()