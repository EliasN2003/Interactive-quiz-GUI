
# PERSONALITY QUIZ

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Personality quiz")
root.geometry("700x400")


# Starting function
def start():
    return


# Creation of the main frame
main_frame = Frame(root, pady=10, padx=10)


# Creation of the starting labels and start button
title_font = ("Berlin Sans FB Demi", 25)
description_label_font = ("Berlin Sans FB Demi", 21)
start_button_font = ("Berlin Sans FB Demi", 18)
title_label = Label(main_frame, text="Discover your personality type")
image = ImageTk.PhotoImage(Image.open("C:/Users/ilias/Desktop/GitHub/Interactive quiz GUI/Images/1.JPG"))
description_label = Label(main_frame, text="Get to know yourself", pady=50)
start_button = Button(main_frame, text="Start the quiz", command=start, borderwidth=7)


# Configuring the font and placing the starting texts on the screen
title_label.configure(font=title_font)
title_label.grid(row=0, column=0)
description_label.configure(font=description_label_font)
description_label.grid(row=1, column=0)
start_button.configure(font=start_button_font)
start_button.grid(row=2, column=0)


# The main frame(title,description,start button)
main_frame.pack()

root.mainloop()
