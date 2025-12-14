import os
import turtle as t
import time
import random
import winsound  # For Windows system sounds (Beeps/Errors)
from pygame import mixer  # For background music
#music line 442
# ==========================================
# MY COOL PONG GAME + QUIZ PROJECT
# ==========================================


# Simple settings
points_to_start = 5  # Play pong for this many points first
paddle_speed = 8  # How fast the paddle moves
scroll_speed = 1  # How fast the text scrolls

# ==========================================
# THE BIG LIST OF QUESTIONS
# ==========================================
my_quiz_list = [
    {"q": "What is the capital of India?", "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "answer": 2,
     "fact": "India's capital is New Delhi."},
    {"q": "National animal of India?", "options": ["Lion", "Elephant", "Tiger", "Leopard"], "answer": 3,
     "fact": "The Royal Bengal Tiger is the national animal."},
    {"q": "Silicon Valley of India?", "options": ["Pune", "Hyderabad", "Bangalore", "Chennai"], "answer": 3,
     "fact": "Bangalore is the IT hub of India."},
    {"q": "Longest river in India?", "options": ["Yamuna", "Ganga", "Godavari", "Narmada"], "answer": 2,
     "fact": "The Ganga is the longest river."},
    {"q": "Smallest state in India?", "options": ["Goa", "Sikkim", "Tripura", "Kerala"], "answer": 1,
     "fact": "Goa is the smallest state by area."},
    {"q": "Currency of Japan?", "options": ["Yen", "Dollar", "Won", "Rupee"], "answer": 1,
     "fact": "The Yen is Japan's currency."},
    {"q": "Largest ocean in the world?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": 3,
     "fact": "The Pacific Ocean is the largest."},
    {"q": "Who discovered gravity?", "options": ["Einstein", "Newton", "Tesla", "Edison"], "answer": 2,
     "fact": "Isaac Newton formulated gravity."},
    {"q": "Gas we breathe in?", "options": ["Nitrogen", "Oxygen", "Helium", "Carbon"], "answer": 2,
     "fact": "We need Oxygen to survive."},
    {"q": "Brain of the computer?", "options": ["RAM", "CPU", "SSD", "GPU"], "answer": 2,
     "fact": "The CPU is the central processing unit."},
    {"q": "Who created Python?", "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Mark Z"], "answer": 2,
     "fact": "Guido created Python in 1991."},
    {"q": "Correct file extension?", "options": [".pt", ".py", ".pn", ".pi"], "answer": 2,
     "fact": "Python files end in .py"},
    {"q": "First man on the Moon?", "options": ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "Michael C"],
     "answer": 2, "fact": "Armstrong landed in 1969."},
    {"q": "Colors in a rainbow?", "options": ["5", "6", "7", "8"], "answer": 3,
     "fact": "There are 7 colors (VIBGYOR)."},
    {"q": "Largest organ in human body?", "options": ["Liver", "Heart", "Skin", "Brain"], "answer": 3,
     "fact": "Skin is the largest organ."},
    {"q": "Formula for water?", "options": ["HO2", "H2O", "CO2", "O2"], "answer": 2,
     "fact": "H2O is 2 Hydrogen, 1 Oxygen."},
    {"q": "Best AI Assistant?", "options": ["Gemini", "ChatGPT", "Copilot", "Claude"],"answer": 2,
     "fact": "You are talking to ChatGPT!"}

]

# ==========================================
# VARIABLES FOR THE GAME
# ==========================================
mode = "intro"
quiz_is_on = False
current_q = None
loser_side = None
p1_score = 0
p2_score = 0
ball_x_speed = 5
ball_y_speed = 5
scroll_pos = 0
buttons = {"w": False, "s": False, "Up": False, "Down": False}

# ==========================================
# SETTING UP THE SCREEN
# ==========================================
screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("#050816")
screen.title("Pong + GK Quiz")
screen.tracer(0)

# ==========================================
# MAKING THE TURTLES
# ==========================================
writer = t.Turtle()
writer.hideturtle()
writer.penup()

score_pen = t.Turtle()
score_pen.hideturtle()
score_pen.color("#00ffc6")
score_pen.penup()

middle_line = t.Turtle()
middle_line.hideturtle()
middle_line.color("#444466")
middle_line.penup()

player1 = t.Turtle("square")
player1.color("#00d1ff")
player1.shapesize(4, 1)
player1.penup()
player1.goto(-350, 0)
player1.hideturtle()

player2 = t.Turtle("square")
player2.color("#ff4b91")
player2.shapesize(4, 1)
player2.penup()
player2.goto(350, 0)
player2.hideturtle()

ball_thing = t.Turtle("circle")
ball_thing.color("#ffdd55")
ball_thing.penup()
ball_thing.goto(0, 0)
ball_thing.hideturtle()

quiz_box = t.Turtle()
quiz_box.hideturtle()
quiz_box.penup()

quiz_writer = t.Turtle()
quiz_writer.hideturtle()
quiz_writer.penup()


# ==========================================
# FUNCTIONS
# ==========================================

def start_screen():
    global mode
    mode = "intro"
    writer.clear()
    writer.goto(0, 200)
    writer.color("#00d1ff")
    writer.write("PONG + GK QUIZ", align="center", font=("Courier", 35, "bold"))

    writer.goto(0, 100)
    writer.color("white")
    writer.write("GAME RULES:", align="center", font=("Courier", 18, "bold"))

    rule_text = "1. Left: W/S | Right: Up/Down\n2. After 5 total points(+/-) Quiz Game starts\n3. Miss ball = Answer Question\n3. Correct = Save Point\n4. Wrong = Lose Point And +1 To Opponent"
    writer.goto(0, 0)
    writer.color("#dddddd")
    writer.write(rule_text, align="center", font=("Courier", 12, "normal"))

    writer.goto(0, -100)
    writer.color("white")
    writer.write("WHY PLAY THIS?", align="center", font=("Courier", 18, "bold"))
    adv_text = (
        "1. Using distraction as the tool to study\n"

        "2. Memorize facts easily\n"

        "3. Learn while having fun"
    )
    writer.goto(0, -180)
    writer.color("#dddddd")
    writer.write(adv_text, align="center", font=("Courier", 12, "italic"))

    writer.goto(0, -250)
    writer.color("#ff4b91")
    writer.write("Press ENTER to MEMORIZE FACTS", align="center", font=("Courier", 16, "bold"))
    screen.update()


def open_study_mode():
    global mode
    mode = "study"
    draw_facts()


def draw_facts():
    if mode != "study": return
    writer.clear()
    writer.goto(0, 260)
    writer.color("#00ffc6")
    writer.write("MEMORIZE THESE FACTS", align="center", font=("Courier", 22, "bold"))

    start_height = 200
    how_many_lines = 14
    global scroll_pos
    max_scroll = max(0, len(my_quiz_list) - how_many_lines)
    if scroll_pos < 0: scroll_pos = 0
    if scroll_pos > max_scroll: scroll_pos = max_scroll

    visible_stuff = my_quiz_list[scroll_pos: scroll_pos + how_many_lines]

    writer.color("white")
    y = start_height
    for i, item in enumerate(visible_stuff):
        number = scroll_pos + i + 1
        writer.goto(-350, y)
        writer.write(f"{number}. {item['fact']}", align="left", font=("Courier", 11, "normal"))
        y -= 30

    writer.goto(0, -280)
    writer.color("#ff4b91")
    writer.write("Press ENTER to START GAME", align="center", font=("Courier", 16, "bold"))
    screen.update()


def move_scroll_up():
    global scroll_pos
    if mode == "study":
        scroll_pos -= scroll_speed
        draw_facts()


def move_scroll_down():
    global scroll_pos
    if mode == "study":
        scroll_pos += scroll_speed
        draw_facts()


def play_pong():
    global mode
    mode = "playing"
    writer.clear()
    ball_thing.showturtle()
    player1.showturtle()
    player2.showturtle()
    draw_middle_line()
    update_scoreboard()


def draw_middle_line():
    middle_line.clear()
    middle_line.penup()
    middle_line.goto(0, 300)
    middle_line.setheading(270)
    middle_line.pensize(3)
    for _ in range(30):
        middle_line.pendown()
        middle_line.forward(10)
        middle_line.penup()
        middle_line.forward(10)


def update_scoreboard():
    score_pen.clear()
    score_pen.goto(-120, 230)
    score_pen.write(p1_score, align="center", font=("Courier", 35, "bold"))
    score_pen.goto(120, 230)
    score_pen.write(p2_score, align="center", font=("Courier", 35, "bold"))


def enter_key_pressed():
    if mode == "intro":
        open_study_mode()
    elif mode == "study":
        play_pong()


def game_over_screen():
    global mode
    mode = "game_over"
    ball_thing.hideturtle()
    player1.hideturtle()
    player2.hideturtle()
    quiz_box.clear()
    quiz_writer.clear()
    score_pen.clear()
    middle_line.clear()
    writer.clear()

    if p1_score > p2_score:
        msg, col = "LEFT PLAYER WINS!", "#00d1ff"
    elif p2_score > p1_score:
        msg, col = "RIGHT PLAYER WINS!", "#ff4b91"
    else:
        msg, col = "IT'S A TIE!", "white"

    writer.goto(0, 50)
    writer.color(col)
    writer.write(msg, align="center", font=("Courier", 35, "bold"))
    writer.goto(0, -20)
    writer.color("white")
    writer.write(f"Final Score: {p1_score} - {p2_score}", align="center", font=("Courier", 20, "bold"))
    screen.update()


def escape_key_pressed():
    global mode, quiz_is_on
    if mode in ["playing", "intro", "study"]:
        quiz_is_on = False
        game_over_screen()
    elif mode == "game_over":
        screen.bye()


# Button Logic
def w_down(): buttons["w"] = True


def w_up(): buttons["w"] = False


def s_down(): buttons["s"] = True


def s_up(): buttons["s"] = False


def up_arrow_press():
    if mode == "study":
        move_scroll_up()
    else:
        buttons["Up"] = True


def up_arrow_release(): buttons["Up"] = False


def down_arrow_press():
    if mode == "study":
        move_scroll_down()
    else:
        buttons["Down"] = True


def down_arrow_release(): buttons["Down"] = False


def move_paddles():
    if mode != "playing" or quiz_is_on: return
    if buttons["w"] and player1.ycor() < 250: player1.sety(player1.ycor() + paddle_speed)
    if buttons["s"] and player1.ycor() > -250: player1.sety(player1.ycor() - paddle_speed)
    if buttons["Up"] and player2.ycor() < 250: player2.sety(player2.ycor() + paddle_speed)
    if buttons["Down"] and player2.ycor() > -250: player2.sety(player2.ycor() - paddle_speed)


# QUIZ LOGIC
def make_quiz_box(loser):
    quiz_box.clear()
    quiz_writer.clear()
    quiz_box.color("white", "#111122")
    quiz_box.pensize(3)
    quiz_box.goto(-250, -150)
    quiz_box.pendown()
    quiz_box.begin_fill()
    for _ in range(2):
        quiz_box.forward(500)
        quiz_box.left(90)
        quiz_box.forward(300)
        quiz_box.left(90)
    quiz_box.end_fill()
    quiz_box.penup()

    quiz_writer.goto(0, 110)
    quiz_writer.color("#ff4b91")
    who = "LEFT" if loser == "left" else "RIGHT"
    quiz_writer.write(f"{who} MISSED!", align="center", font=("Courier", 16, "bold"))

    q = current_q
    quiz_writer.goto(0, 60)
    quiz_writer.color("white")
    quiz_writer.write(q["q"], align="center", font=("Courier", 13, "bold"))

    y = 10
    for i, opt in enumerate(q["options"], start=1):
        quiz_writer.goto(-150, y)
        quiz_writer.write(f"{i}. {opt}", align="left", font=("Courier", 12, "normal"))
        y -= 30


def trigger_quiz(loser):
    global quiz_is_on, current_q, loser_side
    quiz_is_on = True
    loser_side = loser
    current_q = random.choice(my_quiz_list)
    ball_thing.hideturtle()
    make_quiz_box(loser)


def check_answer(num):
    global p1_score, p2_score, quiz_is_on
    if not quiz_is_on or mode != "playing": return

    is_correct = (num == current_q["answer"])

    if is_correct:
        # CORRECT: Play a High Pitch "Ding" (1000Hz for 200ms)
        winsound.Beep(1000, 200)
    else:
        # WRONG: Play Windows Critical Stop / Error Sound
        winsound.MessageBeep(winsound.MB_ICONHAND)

        # Point Penalty logic
        if loser_side == "left":
            p1_score -= 1;
            p2_score += 1
        else:
            p2_score -= 1;
            p1_score += 1

    quiz_box.clear()
    quiz_writer.clear()
    ball_thing.showturtle()
    quiz_is_on = False
    update_scoreboard()


def reset_the_ball(loser):
    global ball_x_speed, p1_score, p2_score
    ball_thing.goto(0, 0)
    ball_x_speed *= -1

    if (p1_score + p2_score) < points_to_start:
        if loser == "left":
            p2_score += 1
        else:
            p1_score += 1
        update_scoreboard()
    else:
        trigger_quiz(loser)


# ==========================================
# KEYBOARD & AUDIO SETUP
# ==========================================
screen.listen()
screen.onkey(enter_key_pressed, "Return")
screen.onkey(escape_key_pressed, "Escape")
screen.onkeypress(w_down, "w")
screen.onkeyrelease(w_up, "w")
screen.onkeypress(s_down, "s")
screen.onkeyrelease(s_up, "s")
screen.onkeypress(up_arrow_press, "Up")
screen.onkeyrelease(up_arrow_release, "Up")
screen.onkeypress(down_arrow_press, "Down")
screen.onkeyrelease(down_arrow_release, "Down")
screen.onkey(lambda: check_answer(1), "1")
screen.onkey(lambda: check_answer(2), "2")
screen.onkey(lambda: check_answer(3), "3")
screen.onkey(lambda: check_answer(4), "4")


# Get the folder where the current script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(BASE_DIR, "music.mp3")  # Change path if your music is in a subfolder

try:
    mixer.init()
    mixer.music.load(music_path)
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
except Exception as e:
    print("MUSIC ERROR:", e)
    print("MUSIC ERROR: Could not find music.mp3. Playing without music.")

# START
start_screen()

while True:
    try:
        screen.update()
        time.sleep(0.015)
        if mode == "playing" and not quiz_is_on:
            move_paddles()
            ball_thing.setx(ball_thing.xcor() + ball_x_speed)
            ball_thing.sety(ball_thing.ycor() + ball_y_speed)

            if ball_thing.ycor() > 290 or ball_thing.ycor() < -290:
                ball_y_speed *= -1

            if (ball_thing.xcor() > 330 and ball_thing.xcor() < 350) and (ball_thing.distance(player2) < 50):
                ball_x_speed *= -1
            if (ball_thing.xcor() < -330 and ball_thing.xcor() > -350) and (ball_thing.distance(player1) < 50):
                ball_x_speed *= -1

            if ball_thing.xcor() > 400: reset_the_ball("right")
            if ball_thing.xcor() < -400: reset_the_ball("left")

    except t.Terminator:
        break

# ======================================================
# EXTENSION COMPATIBILITY LAYER (PHASE 1)
# DO NOT CHANGE ORIGINAL GAME LOGIC ABOVE
# ======================================================

# Global extension flags (default OFF)
EXTENSIONS_ENABLED = True

# Pause support (used later)
game_paused = False

# Music toggle support (used later)
music_muted = False

# Quiz statistics (read-only for now)
stats = {
    "quizzes_total": 0,
    "quizzes_correct": 0,
    "current_streak": 0,
    "max_streak": 0
}

# Difficulty metadata (does NOTHING yet)
difficulty_profile = {
    "name": "NORMAL",
    "ball_multiplier": 1.0,
    "paddle_multiplier": 1.0
}

# NOTE:
# - No original function is overridden
# - No original variable is touched
# - No behavior change occurs in Phase 1
