import turtle
import random

screen = turtle.Screen()
screen.bgcolor("PaleTurquoise")
screen.title("Catch The Turtle")

text_font = ('Arial', 25, 'italic')
countdown_text_font = ('Arial', 15, 'normal')

score_text = turtle.Turtle()

countdown_turtle = turtle.Turtle()

def setup_score_text():
    global score_text
    score_text.hideturtle()
    score_text.penup()

    score_text.color("dark blue")

    top_height = screen.window_height() / 2
    y = top_height * 0.85
    score_text.setpos(0, y)

    score_text.write(arg= "Score: 0", move= False, align= "center", font= text_font)

grid_size = 15

turtle_list = []

score = 0

game_over = False

def create_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        global score_text
        score += 1
        score_text.clear()
        score_text.write(arg= f"Score: {score}", move= False, align= "center", font= text_font)
        #print(x, y)

    t.onclick(handle_click)

    t.penup()

    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")

    t.goto(x * grid_size, y * grid_size)

    turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            create_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_random_turtles():
    hide_turtles()
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_random_turtles, 500)

def countdown(time):
    global countdown_turtle
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()

    countdown_turtle.color("black")

    top_height = screen.window_height() / 2
    y = top_height * 0.78
    countdown_turtle.setpos(0, y)

    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg= f"Time: {time}", move= False, align= "center", font= countdown_text_font)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg= f"Game Over!", move= False, align= "center", font= countdown_text_font)

def start_game_up():
    turtle.tracer(0)

    setup_score_text()
    setup_turtles()
    hide_turtles()
    show_random_turtles()
    countdown(10)

    turtle.tracer(1)

start_game_up()

turtle.mainloop()