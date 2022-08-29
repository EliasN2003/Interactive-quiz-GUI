
# PERSONALITY QUIZ

from tkinter import *

root = Tk()
root.title("Testing")
root.geometry("900x525")
root.configure(bg="#600AEF")
root.resizable(False, False)

questions = ["Pick a job you like:",
             "What is your favorite hobby?",
             "Pick an actor:",
             "Which car would you like to have?",
             "What is your favorite movie genre?",
             "Which director you prefer?",
             "Pick a dog breed you like:",
             "Pick a city you would live in:",
             ]


def quiz():
    x = 0
    for widget in root.winfo_children():        # Clears the main window to print the next question
        widget.grid_forget()
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=2)
    question = Label(root, text=questions[x], bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 43))
    root.grid_columnconfigure(0, weight=1)
    question.grid(row=1, column=0, columnspan=2)
    radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
    radiobutton_spacer.grid(row=2, column=0)
    global answer
    answer = StringVar()
    Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=3, column=0, sticky=W, padx=137)
    Radiobutton(root, text="Female", variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=4, column=0, sticky=W, padx=137, pady=5)
    Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=3, column=0, sticky=W, padx=137)
    Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=3, column=0, sticky=W, padx=137)
    Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=3, column=0, sticky=W, padx=137)
    x = x + 1


def question_1():       # Specific function for the first question
    for widget in root.winfo_children():        # Clears the main window to print the next question
        widget.grid_forget()
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=2)
    question = Label(root, text="Are you male or female?", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 43))
    root.grid_columnconfigure(0, weight=1)
    question.grid(row=1, column=0, columnspan=2)
    radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
    radiobutton_spacer.grid(row=2, column=0)
    global answer
    answer = StringVar()
    Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=3, column=0, sticky=W, padx=137)
    Radiobutton(root, text="Female", variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
        .grid(row=4, column=0, sticky=W, padx=137, pady=5)
    next_button_spacer = Label(root, bg="#600AEF")
    next_button_spacer.grid(row=5, column=1, pady=85)
    next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                         activeforeground="#600AEF", font=("Berlin Sans FB Demi", 18), borderwidth=4, command=quiz)
    next_button.grid(row=6, column=1, padx=20)


def starting_interface():  # Create the starting interface
    title_spacer = Label(root, bg="#600AEF")  # Pushes title text a little lower
    title_label = Label(root, text="QUIZ GAME", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 48))
    description_spacer = Label(root, pady=15, bg="#600AEF")  # Pushes description label a little lower
    description_label = Label(root, text="Which Hollywood actor are you?", bg="#600AEF", fg="#FFFF00",
                              font=("Berlin Sans FB Demi", 36))
    button_spacer = Label(root, pady=35, bg="#600AEF")  # Pushes start button a little lower
    start_button = Button(root, borderwidth=5, text="Start quiz", bg="#600AEF", font=("Berlin Sans FB Demi", 28),
                          fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", command=question_1)

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
# Get rid of global var (line 22)
# Maybe use classes in the future?
