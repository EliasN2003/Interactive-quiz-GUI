
# PERSONALITY QUIZ

from tkinter import *

root = Tk()
root.title("Hollywood actor quiz")
root.geometry("900x525")
root.configure(bg="#600A00")
root.resizable(False, False)

questions = [       # The questions for the quiz
    "",
    "Pick a job you like:",
    "What is your favorite hobby?",
    "Pick an actor:",
    "Which car would you like to have?",
    "What is your favorite movie genre?",
    "Which director you prefer?",
    "Pick a dog breed you like:",
    "Pick a city you would live in:",
]

answers = [     # The text for the radiobuttons
    "Diver", "Actor", "Lawyer",
    "Rock climbing", "Skydiving", "Surfing",
    "Sylvester Stallone", "Brad Pitt", "Jason R. Moore",
    "Audi A8", "Bugatti Veyron", "BMW 735i",
    "Crime", "Action", "Drama",
    "Guy Ritchie", "Christopher McQuarrie", "Steve Lightfoot",
    "Dachshund", "Labrador", "Pit bull",
    "Shirebrook", "San Diego", "Washington",
]

x = 0


def previous():     # Goes back to the previous question
    try:
        global x
        x = x - 1
        for widget in root.winfo_children():  # Clears the main window to print the next question
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
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4) \
            .grid(row=3, column=0, sticky=W, padx=137)

        Radiobutton(root, text="Female", variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4) \
            .grid(row=4, column=0, sticky=W, padx=137, pady=5)

        Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4) \
            .grid(row=5, column=0, sticky=W, padx=137)

        Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4) \
            .grid(row=6, column=0, sticky=W, padx=137)
        Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4) \
            .grid(row=7, column=0, sticky=W, padx=137)

        next_button_spacer = Label(root, bg="#600AEF")
        next_button_spacer.grid(row=5, column=1, pady=85)

        next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                             activeforeground="#600AEF", font=("Berlin Sans FB Demi", 18), borderwidth=4, command=quiz)
        next_button.grid(row=6, column=1, padx=20)

        if x == 1:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 18), borderwidth=4, command=question_1)
            previous_button.grid(row=6, column=0, padx=20, sticky=W)

        else:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 18), borderwidth=4, command=previous)
            previous_button.grid(row=6, column=0, padx=20, sticky=W)

    except IndexError:  # Doubles as the ending/results interface
        label = Label(root, text="End", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 23))
        label.grid(row=0, column=0)


def quiz():     # Prints the rest of the quiz's questions
    try:
        global x
        x = x + 1
        for widget in root.winfo_children():        # Clears the main window to print the next question
            widget.grid_forget()
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        title_spacer = Label(root, bg="#600AEF")
        title_spacer.grid(row=0, column=0, columnspan=2)
        question = Label(root, text=questions[x], bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 43))
        question.grid(row=1, column=0, columnspan=2)
        radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
        radiobutton_spacer.grid(row=2, column=0, columnspan=2)
        global answer
        answer = StringVar()
        Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
            .grid(row=3, column=0, sticky=W, padx=130)

        Radiobutton(root, text="Female", variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
            .grid(row=4, column=0, sticky=W, padx=130, pady=5)

        Radiobutton(root, text="Other", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4)\
            .grid(row=3, column=1, sticky=N, padx=50)

        Radiobutton(root, text="Test", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                    activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                    indicatoron=False, borderwidth=4)\
            .grid(row=4, column=1, sticky=N, padx=50)

        next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                             activeforeground="#600AEF", font=("Berlin Sans FB Demi", 18), borderwidth=4, command=quiz)
        next_button.grid(row=6, column=1, sticky=E, padx=20, pady=196)

        if x == 1:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 18), borderwidth=4, command=question_1)
            previous_button.grid(row=6, column=0, padx=20, sticky=W)

        else:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 18), borderwidth=4, command=previous)
            previous_button.grid(row=6, column=0, padx=20, sticky=W)

    except IndexError:      # Doubles as the ending/results interface
        label = Label(root, text="End", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 23))
        label.grid(row=0, column=0)


def question_1():       # Specific function for the first question
    global x
    x = 0
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
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                indicatoron=False, borderwidth=4)\
        .grid(row=3, column=0, sticky=W, padx=137)

    Radiobutton(root, text="Female", variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 23),
                indicatoron=False, borderwidth=4)\
        .grid(row=4, column=0, sticky=W, padx=137, pady=5)

    next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                         activeforeground="#600AEF", font=("Berlin Sans FB Demi", 18), borderwidth=4, command=quiz)
    next_button.grid(row=6, column=1, padx=20, pady=196, sticky=SE)


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
# Get rid of global var (line 22)
# Maybe use classes in the future?
