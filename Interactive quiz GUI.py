
# PERSONALITY QUIZ

from tkinter import *

root = Tk()
root.title("Hollywood actor quiz")
root.configure(bg="#600AEF")
root.state('zoomed')


# Importing necessary images
male_symbol = PhotoImage(file="images/male_symbol.png")
female_symbol = PhotoImage(file="images/female_symbol.png")

images = [
    PhotoImage(file="images/diver.png"),
    PhotoImage(file="images/actor.png"),
    PhotoImage(file="images/salesman.png"),

    PhotoImage(file="images/rock_climbing.png"),
    PhotoImage(file="images/skydiving.png"),
    PhotoImage(file="images/knitting.png"),

    PhotoImage(file="images/stallone.png"),
    PhotoImage(file="images/brad.png"),
    PhotoImage(file="images/bradley.png"),

    PhotoImage(file="images/audi.png"),
    PhotoImage(file="images/bugatti.png"),
    PhotoImage(file="images/911.png"),

    PhotoImage(file="images/crime.png"),
    PhotoImage(file="images/action.png"),
    PhotoImage(file="images/drama.png"),

    PhotoImage(file="images/denis.png"),
    PhotoImage(file="images/guy_ritchie.png"),
    PhotoImage(file="images/christopher.png"),

    PhotoImage(file="images/dachshund.png"),
    PhotoImage(file="images/labrador.png"),
    PhotoImage(file="images/doberman.png"),

    PhotoImage(file="images/shirebrook.png"),
    PhotoImage(file="images/san_diego.png"),
    PhotoImage(file="images/ontario.png"),

    PhotoImage(file="images/JS_house.png"),
    PhotoImage(file="images/TC_house.png"),
    PhotoImage(file="images/RG_house.png"),
]


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


answers = [         # The answers for the quiz
    "", "", "",
    "Diver", "Actor", "Salesman",
    "Rock climbing", "Skydiving", "Knitting",
    "Sylvester Stallone", "Brad Pitt", "Bradley Cooper",
    "Audi A8", "Bugatti Veyron", "Porsche 911",
    "Crime", "Action", "Drama",
    "Guy Ritchie", "Christopher McQuarrie", "Denis Villeneuve",
    "Dachshund", "Labrador", "Doberman",
    "Shirebrook", "San Diego", "Ontario"
]

x = 0       # Used to automate the printing process of the questions
y = 0       # Used to automate the printing process of the answers of each question
z = 0       # Used to automate the printing process of the images


def previous():     # Goes back to the previous question
    global x
    x = x - 1
    global y
    y = y - 3
    global z
    z = z - 6
    for widget in root.winfo_children():  # Clears the main window to print the next question
        widget.grid_forget()
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=2)
    question = Label(root, text=questions[x], bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
    question.grid(row=1, column=0, columnspan=2)
    radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
    radiobutton_spacer.grid(row=2, column=0, columnspan=2)
    global answer
    answer = StringVar()
    Radiobutton(root, image=images[0], variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4) \
        .grid(row=3, column=0, sticky=W, padx=130)

    Radiobutton(root, text=answers[y + 1], variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4) \
        .grid(row=4, column=0, sticky=W, padx=130, pady=5)

    Radiobutton(root, text=answers[y + 2], variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4) \
        .grid(row=3, column=1, sticky=N, padx=50)

    next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                         activeforeground="#600AEF", font=("Berlin Sans FB Demi", 28), borderwidth=6, command=quiz)
    next_button.grid(row=6, column=1, sticky=E, padx=20, pady=196)

    if x == 1:
        previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                 activebackground="#FFFF00", activeforeground="#600AEF",
                                 font=("Berlin Sans FB Demi", 28), borderwidth=6, command=question_1)
        previous_button.grid(row=6, column=0, padx=20, sticky=W)

    else:
        previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                 activebackground="#FFFF00", activeforeground="#600AEF",
                                 font=("Berlin Sans FB Demi", 28), borderwidth=6, command=previous)
        previous_button.grid(row=6, column=0, padx=20, sticky=W)


def quiz():     # Prints the rest of the quiz's questions
    try:
        global x
        x = x + 1
        global y
        y = y + 3
        global z
        z = z + 6
        for widget in root.winfo_children():        # Clears the main window to print the next question
            widget.grid_forget()
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        title_spacer = Label(root, bg="#600AEF")
        title_spacer.grid(row=0, column=0, columnspan=2)
        question = Label(root, text=questions[x], bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
        question.grid(row=1, column=0, columnspan=2)
        radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
        radiobutton_spacer.grid(row=2, column=0, columnspan=2)
        global answer
        answer = StringVar()
        Radiobutton(root, image=images[0], variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
            .grid(row=3, column=0, sticky=W, padx=130)

        Radiobutton(root, text=answers[y + 1], variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
            .grid(row=4, column=0, sticky=W, padx=130, pady=5)

        Radiobutton(root, image=images[0], variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
            .grid(row=3, column=0, sticky=W, padx=130)

        Radiobutton(root, text=answers[y + 2], variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4)\
            .grid(row=3, column=1, sticky=N, padx=50)

        next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                             activeforeground="#600AEF", font=("Berlin Sans FB Demi", 28), borderwidth=6, command=quiz)
        next_button.grid(row=6, column=1, sticky=E, padx=25, pady=350)

        if x == 1:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 28), borderwidth=6, command=question_1)
            previous_button.grid(row=6, column=0, padx=20, sticky=W)

        else:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 28), borderwidth=6, command=previous)
            previous_button.grid(row=6, column=0, padx=20, sticky=W)

    except IndexError:      # Doubles as the ending/results interface
        label = Label(root, text="End", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
        label.grid(row=0, column=0, columnspan=2)


def question_1():       # Specific function for the first question
    global x
    x = 0
    global y
    y = 0
    global z
    z = 0
    for widget in root.winfo_children():        # Clears the main window to print the next question
        widget.grid_forget()
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=2)
    question = Label(root, text="Are you male or female?", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
    root.grid_columnconfigure(0, weight=1)
    question.grid(row=1, column=0, columnspan=2)
    radiobutton_spacer = Label(root, pady=30, bg="#600AEF")
    radiobutton_spacer.grid(row=3, column=1)
    global answer
    answer = StringVar()

    Radiobutton(root, image=male_symbol, variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8)\
        .grid(row=4, column=0, padx=137, sticky=S)

    Radiobutton(root, text="Male", variable=answer, value="male", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8)\
        .grid(row=5, column=0, padx=137, ipadx=41)

    Radiobutton(root, image=female_symbol, variable=answer, value="female", selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8)\
        .grid(row=4, column=1, padx=137)

    Radiobutton(root, text="Female", variable=answer, value="female", bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8)\
        .grid(row=5, column=1, padx=137, ipadx=1)

    next_button_spacer = Label(root, pady=131, bg="#600AEF")
    next_button_spacer.grid(row=6, column=1)
    next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                         activeforeground="#600AEF", font=("Berlin Sans FB Demi", 28), borderwidth=6, command=quiz)
    next_button.grid(row=7, column=1, padx=25, sticky=SE)


def starting_interface():  # Create the starting interface
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    title_spacer = Label(root, bg="#600AEF")  # Pushes title text a little lower
    title_label = Label(root, text="QUIZ GAME", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 65))
    description_spacer = Label(root, pady=25, bg="#600AEF")  # Pushes description label lower
    description_label = Label(root, text="Which Hollywood actor are you?", bg="#600AEF", fg="#FFFF00",
                              font=("Berlin Sans FB Demi", 40))
    button_spacer = Label(root, pady=35, bg="#600AEF")  # Pushes start button a little lower
    start_button = Button(root, borderwidth=8, text="Start quiz", bg="#600AEF", font=("Berlin Sans FB Demi", 35),
                          fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", command=question_1)

    title_spacer.grid(row=0, columnspan=2, pady=20)
    title_label.grid(row=1, columnspan=2)
    description_spacer.grid(row=2, columnspan=2)
    description_label.grid(row=3, columnspan=2, padx=99)
    button_spacer.grid(row=4, columnspan=2, pady=50)
    start_button.grid(row=5, columnspan=2)


starting_interface()

root.mainloop()

# Comments:
# Change icon
# Get rid of global var (line 22)
# Maybe use classes in the future?
