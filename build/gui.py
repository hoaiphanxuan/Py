
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1203x915")
window.configure(bg = "#A9C1C0")



canvas = Canvas(
    window,
    bg = "#A9C1C0",
    height = 915,
    width = 1203,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    399.9975280761719,
    0.0,
    2002.9950866699219,
    1315.836669921875,
    fill="#000000",
    outline="")

bg = PhotoImage(file = "1.png")
  
# Show image using label
label1 = Label( window, image = bg)
label1.place(x = -0.7, y = -0.7)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    887.96435546875,
    358.375,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg='#d7e2e2',
    highlightthickness=0
)
entry_1.place(
    x=614.018798828125,
    y=329,
    width=550,
    height=58
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    887.96435546875,
    507.8249816894531,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg='#d7e2e2',
    highlightthickness=0
)
entry_2.place(
    x=614.018798828125,
    y=479,
    width=550,
    height=58
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    bg='#d7e2e2',
    activebackground='#d7e2e2',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=770.0,
    y=559.0,
    width=265.0,
    height=78.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    bg='#d7e2e2',
    activebackground='#d7e2e2',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=725.0,
    y=656.0,
    width=350.3861083984375,
    height=36.60003662109375
)
window.resizable(False, False)
window.mainloop()