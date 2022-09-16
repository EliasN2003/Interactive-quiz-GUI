
# PERSONALITY QUIZ

from tkinter import *
from collections import Counter
import random

root = Tk()
root.title("Hollywood actor quiz")
root.iconbitmap("images/icon.ico")
root.configure(bg="#600AEF")
root.state('zoomed')


# Importing necessary images
male_symbol = PhotoImage(file="images/first_question/male_symbol.png")
female_symbol = PhotoImage(file="images/first_question/female_symbol.png")

images = [

    # Sample images used for the first time the quiz function runs
    PhotoImage(file="images/Sample image.png"),
    PhotoImage(file="images/Sample image.png"),
    PhotoImage(file="images/Sample image.png"),
    PhotoImage(file="images/Sample image.png"),
    PhotoImage(file="images/Sample image.png"),
    PhotoImage(file="images/Sample image.png"),

    PhotoImage(file="images/Jobs/diver.png"),
    PhotoImage(file="images/Jobs/actor.png"),
    PhotoImage(file="images/Jobs/salesman.png"),
    PhotoImage(file="images/Jobs/musician.png"),
    PhotoImage(file="images/Jobs/football.png"),
    PhotoImage(file="images/Jobs/teacher.png"),

    PhotoImage(file="images/Hobbies/rock_climbing.png"),
    PhotoImage(file="images/Hobbies/skydiving.png"),
    PhotoImage(file="images/Hobbies/knitting.png"),
    PhotoImage(file="images/Hobbies/dancing.png"),
    PhotoImage(file="images/Hobbies/watching_movies.png"),
    PhotoImage(file="images/Hobbies/shopping.png"),

    PhotoImage(file="images/Celeb friends/Stallone.png"),
    PhotoImage(file="images/Celeb friends/Brad.png"),
    PhotoImage(file="images/Celeb friends/Bradley.png"),
    PhotoImage(file="images/Celeb friends/Matthew.png"),
    PhotoImage(file="images/Celeb friends/Jennifer.png"),
    PhotoImage(file="images/Celeb friends/Chris.png"),

    PhotoImage(file="images/Cars/audi.png"),
    PhotoImage(file="images/Cars/bugatti.png"),
    PhotoImage(file="images/Cars/911.png"),
    PhotoImage(file="images/Cars/audi s6.png"),
    PhotoImage(file="images/Cars/porsche_carrera_s.png"),
    PhotoImage(file="images/Cars/tesla.png"),

    PhotoImage(file="images/Movie genres/crime.png"),
    PhotoImage(file="images/Movie genres/action.png"),
    PhotoImage(file="images/Movie genres/drama.png"),
    PhotoImage(file="images/Movie genres/musical.png"),
    PhotoImage(file="images/Movie genres/romance.png"),
    PhotoImage(file="images/Movie genres/sci-fi.png"),

    PhotoImage(file="images/Directors/Guy_ritchie.png"),
    PhotoImage(file="images/Directors/Christopher_m.png"),
    PhotoImage(file="images/Directors/Denis.png"),
    PhotoImage(file="images/Directors/Damien.png"),
    PhotoImage(file="images/Directors/Christopher_n.png"),
    PhotoImage(file="images/Directors/Cary.png"),

    PhotoImage(file="images/Dogs/dachshund.png"),
    PhotoImage(file="images/Dogs/labrador.png"),
    PhotoImage(file="images/Dogs/doberman.png"),
    PhotoImage(file="images/Dogs/golden_retriever.png"),
    PhotoImage(file="images/Dogs/terrier.png"),
    PhotoImage(file="images/Dogs/maltese.png"),

    PhotoImage(file="images/Cities/Shirebrook.png"),
    PhotoImage(file="images/Cities/San_Diego.png"),
    PhotoImage(file="images/Cities/Ontario.png"),
    PhotoImage(file="images/Cities/Arizona.png"),
    PhotoImage(file="images/Cities/New_York.png"),
    PhotoImage(file="images/Cities/Cuba.png"),
]

# Images for the last question
last_question_images = [
    PhotoImage(file="images/Houses/JS_house.png"),
    PhotoImage(file="images/Houses/TC_house.png"),
    PhotoImage(file="images/Houses/RG_house.png"),
    PhotoImage(file="images/Houses/ES_house.png"),
    PhotoImage(file="images/Houses/AH_house.png"),
    PhotoImage(file="images/Houses/ADA_house.png")
]

# Images for the results page
results_images = [
    PhotoImage(file="images/Actors/Statham.png"),
    PhotoImage(file="images/Actors/Tom.png"),
    PhotoImage(file="images/Actors/Ryan.png"),
    PhotoImage(file="images/Actors/Emma.png"),
    PhotoImage(file="images/Actors/Anne.png"),
    PhotoImage(file="images/Actors/Ana.png"),
]


# The questions for the quiz
questions = [
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

# The answers for the quiz
answers = [
    "", "", "", "", "", "",
    "Diver", "Actor", "Salesman", "Musician", "Footballer", "Teacher",
    "Rock climbing", "Skydiving", "Knitting", "Dancing", "Watching movies", "Shopping",
    "Sylvester Stallone", "Brad Pitt", "Bradley Cooper", "Matthew Mcconaughey", "Jennifer Lawrence", "Chris Evans",
    "Audi A8", "Bugatti Veyron", "Porsche 911", "Audi S6", "Porsche carrera S", "Tesla model S",
    "Crime", "Action", "Drama", "Musical", "Romance", "Sci-fi",
    "Guy Ritchie", "Christopher McQuarrie", "Denis Villeneuve", "Damien Chazelle", "Christopher Nolan", "Cary Fukunaga",
    "Dachshund", "Labrador", "Doberman", "Golden retriever", "Terrier", "Maltese",
    "Shirebrook", "San Diego", "Ontario", "Arizona", "New York", "Cuba"
]

# Used when printing the actor in the results page
actors_names = [
    "Jason Statham",
    "Tom Cruise",
    "Ryan Gosling",
    "Emma Stone",
    "Anne Hathaway",
    "Ana De Armas"
]

# Stores the key for each answer
answers_variables = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = 0       # Used to automate the printing process of the questions
y = 0       # Used to automate the printing process of the answers of each question

# The variable used to hold the answers
answer = IntVar()
answer.set(0)


# Stores the answer to a variable
def save_variable(value):
    answers_variables[x] = value


# Prints results/last page
def results():
    # Clears the main window to print the results page
    for widget in root.winfo_children():
        widget.grid_forget()

    # Method to print the correct actor in the results interface
    def result(value):
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        # Pushes title text lower
        title = Label(root, text="QUIZ COMPLETED!", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 65))
        title_spacer = Label(root, bg="#600AEF")
        description = Label(root, text="You are:", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 40))
        actor_image = Label(root, image=results_images[value], relief=SOLID, borderwidth=7)
        actor_name = Label(root, text=actors_names[value], font=("Berlin Sans FB Demi", 40), bg="#600AEF", fg="#FFFF00")
        play_again = Button(root, borderwidth=8, text="Play again?", bg="#600AEF", font=("Berlin Sans FB Demi", 27),
                            fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                            command=starting_interface)

        title.grid(row=0, column=0, columnspan=3, pady=20)
        title_spacer.grid(row=1, column=0, columnspan=3, pady=30)
        description.grid(row=2, column=0, columnspan=3, pady=5)
        actor_image.grid(row=3, column=0, columnspan=3)
        actor_name.grid(row=4, column=0, columnspan=3)
        play_again.grid(row=5, column=0, columnspan=3, pady=80)

    if answers_variables[0] == 7:
        # Stores the variables for comparison
        numbers_list = []
        # Counts how many times the answers have been selected
        one = answers_variables.count(1)
        two = answers_variables.count(2)
        three = answers_variables.count(3)
        # Stores the variables in the list if they have been selected at least once
        if one > 0:
            numbers_list.append(0)
        if two > 0:
            numbers_list.append(1)
        if three > 0:
            numbers_list.append(2)
        # Prints the actor that you have the most similarities with
        if one > two and one > three:
            result(0)

        elif two > one and two > three:
            result(1)

        elif three > one and three > two:
            result(2)

        # Prints an actor of the opposite gender if no actors of the same gender have been selected
        elif one + two + three == 0:
            my_counter = Counter(answers_variables)
            result(int((my_counter.most_common(1)[0][0]) - 1))

        # Prints an actor at random if they have the same number of answers
        else:
            choice = int(random.choice(numbers_list))
            result(choice)

    elif answers_variables[0] == 8:
        # Stores the variables for comparison
        numbers_list = []
        # Counts how many times the answers have been selected
        four = answers_variables.count(4)
        five = answers_variables.count(5)
        six = answers_variables.count(6)
        # Stores the variables in the list if they have been selected at least once
        if four > 0:
            numbers_list.append(3)
        if five > 0:
            numbers_list.append(4)
        if six > 0:
            numbers_list.append(5)
        # Prints the actor that you have the most similarities with
        if four > five and four > six:
            result(3)

        elif five > four and five > six:
            result(4)

        elif six > four and six > five:
            result(5)

        # Prints an actor of the opposite gender if no actors of the same gender have been selected
        elif four + five + six == 0:
            my_counter = Counter(answers_variables)
            result(int((my_counter.most_common(1)[0][0]) - 1))

        # Prints an actor at random if they have the same number of answers
        else:
            choice = int(random.choice(numbers_list))
            result(choice)


# The last question that doesn't have buttons under the images
def last_question():
    # Clears the main window to print the next question
    for widget in root.winfo_children():
        widget.grid_forget()
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=3)
    question = Label(root, text="Pick a house you would live in:", bg="#600AEF", fg="#FFFF00",
                     font=("Berlin Sans FB Demi", 53))
    question.grid(row=1, column=0, columnspan=3)
    radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
    radiobutton_spacer.grid(row=2, column=0, columnspan=3)

    # First column
    Radiobutton(root, image=last_question_images[0], variable=answer, value=1, bg="#600AEF",
                selectcolor="#4507AB", fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get())) \
        .grid(row=3, column=0)

    Radiobutton(root, image=last_question_images[1], variable=answer, value=2,
                selectcolor="#4507AB", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                activeforeground="#600AEF", indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=4, column=0, pady=92)

    radiobutton_spacer = Label(root, pady=10, bg="#600AEF")
    radiobutton_spacer.grid(row=5, column=0, columnspan=3)

    # Second column
    Radiobutton(root, image=last_question_images[2], variable=answer, value=3, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get())) \
        .grid(row=3, column=1)

    Radiobutton(root, image=last_question_images[3], variable=answer, value=4, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get())) \
        .grid(row=4, column=1)

    # Third column
    Radiobutton(root, image=last_question_images[4], variable=answer, value=5, selectcolor="#4507AB",
                bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", indicatoron=False,
                borderwidth=4, command=lambda: save_variable(answer.get())) \
        .grid(row=3, column=2)

    Radiobutton(root, image=last_question_images[5], variable=answer, value=6, bg="#600AEF",
                selectcolor="#4507AB", fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get())) \
        .grid(row=4, column=2)

    results_button = Button(root, text="Finish quiz", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                            activeforeground="#600AEF", font=("Berlin Sans FB Demi", 20), borderwidth=6,
                            command=results)
    results_button.grid(row=8, column=2, sticky=SE, pady=44, padx=10)

    previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                             activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 20),
                             borderwidth=6, command=previous)
    previous_button.grid(row=8, column=0, sticky=SW, pady=44, padx=10)


# Goes back to the previous question
def previous():
    global x
    x = x - 1
    global y
    y = y - 6
    # Clears the main window to print the next question
    for widget in root.winfo_children():
        widget.grid_forget()
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=3)
    question = Label(root, text=questions[x], bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
    question.grid(row=1, column=0, columnspan=3)
    radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
    radiobutton_spacer.grid(row=2, column=0, columnspan=3)

    # First column
    Radiobutton(root, image=images[y], variable=answer, value=1, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=3, column=0)

    Radiobutton(root, text=answers[y], variable=answer, value=1, selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=4, column=0)

    # Makes a space between the radiobuttons
    radiobutton_spacer_2 = Label(root, pady=10, bg="#600AEF")
    radiobutton_spacer_2.grid(row=5, column=0, columnspan=3)

    Radiobutton(root, image=images[y + 1], variable=answer, value=2, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=6, column=0)

    Radiobutton(root, text=answers[y + 1], variable=answer, value=2, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=7, column=0)

    # Second column
    Radiobutton(root, image=images[y + 2], variable=answer, value=3, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=3, column=1)

    Radiobutton(root, text=answers[y + 2], variable=answer, value=3, selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=4, column=1)

    Radiobutton(root, image=images[y + 3], variable=answer, value=4, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=6, column=1)

    Radiobutton(root, text=answers[y + 3], variable=answer, value=4, selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=7, column=1)

    # Third column
    Radiobutton(root, image=images[y + 4], variable=answer, value=5, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=3, column=2)

    Radiobutton(root, text=answers[y + 4], variable=answer, value=5, selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=4, column=2)

    Radiobutton(root, image=images[y + 5], variable=answer, value=6, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=6, column=2)

    Radiobutton(root, text=answers[y + 5], variable=answer, value=6, selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                command=lambda: save_variable(answer.get())) \
        .grid(row=7, column=2)

    next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                         activeforeground="#600AEF", font=("Berlin Sans FB Demi", 20), borderwidth=6, command=quiz)
    next_button.grid(row=8, column=2, sticky=SE, pady=120, padx=10)

    if x == 1:
        previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                 activebackground="#FFFF00", activeforeground="#600AEF",
                                 font=("Berlin Sans FB Demi", 20), borderwidth=6, command=first_question)
        previous_button.grid(row=8, column=0, sticky=SW, pady=120, padx=10)

    else:
        previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                 activebackground="#FFFF00", activeforeground="#600AEF",
                                 font=("Berlin Sans FB Demi", 20), borderwidth=6, command=previous)
        previous_button.grid(row=8, column=0, sticky=SW, pady=120, padx=10)


def quiz():     # Prints the rest of the quiz's questions
    try:
        global x
        x = x + 1
        global y
        y = y + 6
        # Clears the main window to print the next question
        for widget in root.winfo_children():
            widget.grid_forget()
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

        title_spacer = Label(root, bg="#600AEF")
        title_spacer.grid(row=0, column=0, columnspan=3)
        question = Label(root, text=questions[x], bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
        question.grid(row=1, column=0, columnspan=3)
        radiobutton_spacer = Label(root, pady=20, bg="#600AEF")
        radiobutton_spacer.grid(row=2, column=0, columnspan=3)

        # First column
        Radiobutton(root, image=images[y], variable=answer, value=1, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get()))\
            .grid(row=3, column=0)

        Radiobutton(root, text=answers[y], variable=answer, value=1, selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                    command=lambda: save_variable(answer.get()))\
            .grid(row=4, column=0)

        # Makes a space between the radiobuttons
        radiobutton_spacer_2 = Label(root, pady=10, bg="#600AEF")
        radiobutton_spacer_2.grid(row=5, column=0, columnspan=3)

        Radiobutton(root, image=images[y + 1], variable=answer, value=2, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get()))\
            .grid(row=6, column=0)

        Radiobutton(root, text=answers[y + 1], variable=answer, value=2, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                    command=lambda: save_variable(answer.get()))\
            .grid(row=7, column=0)

        # Second column
        Radiobutton(root, image=images[y + 2], variable=answer, value=3, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get()))\
            .grid(row=3, column=1)

        Radiobutton(root, text=answers[y + 2], variable=answer, value=3, selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                    command=lambda: save_variable(answer.get()))\
            .grid(row=4, column=1)

        Radiobutton(root, image=images[y + 3], variable=answer, value=4, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get()))\
            .grid(row=6, column=1)

        Radiobutton(root, text=answers[y + 3], variable=answer, value=4, selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                    command=lambda: save_variable(answer.get()))\
            .grid(row=7, column=1)

        # Third column
        Radiobutton(root, image=images[y + 4], variable=answer, value=5, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get()))\
            .grid(row=3, column=2)

        Radiobutton(root, text=answers[y + 4], variable=answer, value=5, selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                    command=lambda: save_variable(answer.get()))\
            .grid(row=4, column=2)

        Radiobutton(root, image=images[y + 5], variable=answer, value=6, bg="#600AEF", selectcolor="#4507AB",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    indicatoron=False, borderwidth=4, command=lambda: save_variable(answer.get()))\
            .grid(row=6, column=2)

        Radiobutton(root, text=answers[y + 5], variable=answer, value=6, selectcolor="#4507AB", bg="#600AEF",
                    fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF",
                    font=("Berlin Sans FB Demi", 23), indicatoron=False, borderwidth=4,
                    command=lambda: save_variable(answer.get()))\
            .grid(row=7, column=2)

        next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                             activeforeground="#600AEF", font=("Berlin Sans FB Demi", 20), borderwidth=6,
                             command=quiz)
        next_button.grid(row=8, column=2, sticky=SE, pady=120, padx=10)

        if x == 1:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 20), borderwidth=6, command=first_question)
            previous_button.grid(row=8, column=0, sticky=SW, pady=120, padx=10)

        else:
            previous_button = Button(root, text="Previous question", bg="#600AEF", fg="#FFFF00",
                                     activebackground="#FFFF00", activeforeground="#600AEF",
                                     font=("Berlin Sans FB Demi", 20), borderwidth=6, command=previous)
            previous_button.grid(row=8, column=0, sticky=SW, pady=120, padx=10)

    # Initiates the final question when it finishes with all the other questions
    except IndexError:
        last_question()


# Specific function for the first question
def first_question():
    # Clears the main window to print the results page
    for widget in root.winfo_children():
        widget.grid_forget()
    # Resets the variables to start counting from the start
    global x
    x = 0
    global y
    y = 0
    # Clears the main window to print the next question
    for widget in root.winfo_children():
        widget.grid_forget()
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    title_spacer = Label(root, bg="#600AEF")
    title_spacer.grid(row=0, column=0, columnspan=3)
    question = Label(root, text="Are you male or female?", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 53))
    question.grid(row=1, column=0, columnspan=3)
    radiobutton_spacer = Label(root, pady=30, bg="#600AEF")
    radiobutton_spacer.grid(row=3, column=1)

    Radiobutton(root, image=male_symbol, variable=answer, value=7, bg="#600AEF", selectcolor="#4507AB",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8, command=lambda: save_variable(answer.get()))\
        .grid(row=4, column=0, padx=137, sticky=S)

    Radiobutton(root, text="Male", variable=answer, value=7, bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8, command=lambda: save_variable(answer.get()))\
        .grid(row=5, column=0, padx=137, ipadx=41)

    Radiobutton(root, image=female_symbol, variable=answer, value=8, selectcolor="#4507AB", bg="#600AEF",
                fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8, command=lambda: save_variable(answer.get()))\
        .grid(row=4, column=2, padx=137)

    Radiobutton(root, text="Female", variable=answer, value=8, bg="#600AEF", selectcolor="#4507AB", fg="#FFFF00",
                activebackground="#FFFF00", activeforeground="#600AEF", font=("Berlin Sans FB Demi", 32),
                indicatoron=False, borderwidth=8, command=lambda: save_variable(answer.get()))\
        .grid(row=5, column=2, padx=137, ipadx=1)

    next_button_spacer = Label(root, pady=149, bg="#600AEF")
    next_button_spacer.grid(row=6, column=2)
    next_button = Button(root, text="Next question", bg="#600AEF", fg="#FFFF00", activebackground="#FFFF00",
                         activeforeground="#600AEF", font=("Berlin Sans FB Demi", 20), borderwidth=6,
                         command=quiz)
    next_button.grid(row=7, column=2, padx=10, sticky=SE)


# Creates the starting interface
def starting_interface():
    # Clears the main window to print the results page
    for widget in root.winfo_children():
        widget.grid_forget()
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    # Pushes title text lower
    title_spacer = Label(root, bg="#600AEF")
    title = Label(root, text="QUIZ GAME", bg="#600AEF", fg="#FFFF00", font=("Berlin Sans FB Demi", 70))
    # Pushes description label lower
    description_spacer = Label(root, bg="#600AEF")
    description = Label(root, text="Which Hollywood actor are you?", bg="#600AEF", fg="#FFFF00",
                        font=("Berlin Sans FB Demi", 50))
    button_spacer = Label(root, pady=27, bg="#600AEF")  # Pushes start button lower
    start_button = Button(root, borderwidth=8, text="Start quiz", bg="#600AEF", font=("Berlin Sans FB Demi", 40),
                          fg="#FFFF00", activebackground="#FFFF00", activeforeground="#600AEF", command=first_question)

    title_spacer.grid(row=0, columnspan=3, pady=40)
    title.grid(row=1, columnspan=3)
    description_spacer.grid(row=2, columnspan=3, pady=35)
    description.grid(row=3, columnspan=3, padx=99)
    button_spacer.grid(row=4, columnspan=3, pady=50)
    start_button.grid(row=5, columnspan=3)


# Runs the starting interface
starting_interface()

root.mainloop()

# Comments:
# Maybe use classes in the future?
# Fix buttons staying pressed
