
# PERSONALITY QUIZ

from tkinter import *

root = Tk()
root.title("Hollywood actor quiz")
root.geometry("900x525")
root.configure(bg="#600AEF")
root.resizable(False, False)


def start_quiz():
    for widget in root.winfo_children():
        widget.grid_forget()
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=2)
    question = Label(root, text="Are you male or female?", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 43))
    question.grid(row=1, column=0, padx=135)
    r = StringVar()
    r.get()
    Radiobutton(root, text="Male", variable=r, value="male", font=("Berlin Sans FB Demi", 20), bg="#600AEF", fg="#FFFF00", activebackground="#600AEF", activeforeground="#FFFF00", command=lambda: clicked(r.get()))\
        .grid(row=2, column=0, sticky=W, padx=137, pady=50)
    Radiobutton(root, text="Female", variable=r, value="female", font=("Berlin Sans FB Demi", 20), bg="#600AEF", fg="#FFFF00", activebackground="#600AEF", activeforeground="#FFFF00", command=lambda: clicked(r.get()))\
        .grid(row=3, column=0, sticky=W, padx=137)

    def clicked(value):
        label = Label(root, text=value)
        label.grid(row=4, column=0)


def starting_interface():  # Create the starting interface
    title_spacer = Label(root, bg="#600AEF")  # Pushes title text a little lower
    title_label = Label(root, text="QUIZ GAME", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 48))
    description_spacer = Label(root, pady=15, bg="#600AEF")  # Pushes description label a little lower
    description_label = Label(root, text="Which Hollywood actor are you?", bg="#600AEF", fg="#FFFF00",
                              font=("Berlin Sans FB Demi", 36))
    button_spacer = Label(root, pady=35, bg="#600AEF")  # Pushes start button a little lower
    start_button = Button(root, borderwidth=5, text="Start quiz", bg="#600AEF", font=("Berlin Sans FB Demi", 28),
                          fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", command=start_quiz)

    title_spacer.grid(row=0, column=0)
    title_label.grid(row=1, column=0)
    description_spacer.grid(row=2, column=0)
    description_label.grid(row=3, column=0, padx=99)
    button_spacer.grid(row=4, column=0)
    start_button.grid(row=5, column=0)


starting_interface()

root.mainloop()

# Comments:
# Change icon
# Got rid of main_frame because it wasn't needed, used root instead
