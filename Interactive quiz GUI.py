
# PERSONALITY QUIZ

from tkinter import *

root = Tk()
root.title("Movie character quiz")
root.geometry("800x480")
root.configure(bg="#600AEF")
# root.resizable(False, False)

main_frame = Frame(root, bg="#600AEF")

# Create the starting interface
title_spacer = Label(main_frame, bg="#600AEF")     # Pushes title text a little lower
title_label = Label(main_frame, text="QUIZ GAME", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 48))
description_spacer = Label(main_frame, pady=15, bg="#600AEF")       # Pushes description label a little lower
description_label = Label(main_frame, text="Which movie character are you?", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 36))
button_spacer = Label(main_frame, pady=35, bg="#600AEF")        # Pushes start button a little lower
start_button = Button(main_frame, borderwidth=5, text="Start quiz", bg="#600AEF", font=("Berlin Sans FB Demi", 28), fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF")

title_spacer.pack()
title_label.pack()
description_spacer.pack()
description_label.pack()
button_spacer.pack()
start_button.pack()


main_frame.pack()

root.mainloop()
