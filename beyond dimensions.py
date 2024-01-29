import turtle
import subprocess

# setting up the screen
bg_image_path1 = "black"
screen = turtle.Screen()
screen.title("Beyond Dimensions")
screen.bgcolor(bg_image_path1)
screen.setup(width=1500, height=900)
turtle.listen()
def setup1():
    global title1, title2, start_text, credits_text, settings_text, starting_screen
    starting_screen = 1
    # title screen stuff
    title1 = turtle.Turtle()
    title1.speed(0)
    title1.color("blue")
    title1.penup()
    title1.hideturtle()
    title1.goto(0, 300)
    title1.write("Beyond", align="center", font=("Courier", 50, "normal"))
    
    title2 = turtle.Turtle()
    title2.speed(0)
    title2.color("blue")
    title2.penup()
    title2.hideturtle()
    title2.goto(0, 200)
    title2.write("Dimensions", align="center", font=("Courier", 50, "normal"))
    
    start_text = turtle.Turtle()
    start_text.speed(0)
    start_text.color("green")
    start_text.penup()
    start_text.hideturtle()
    start_text.goto(-200, 50)
    start_text.write("START", align="center", font=("Courier", 40, "normal"))
    
    credits_text = turtle.Turtle()
    credits_text.speed(0)
    credits_text.color("red")
    credits_text.penup()
    credits_text.hideturtle()
    credits_text.goto(-400, -400)
    credits_text.write("Credits", align="center", font=("Courier", 40, "normal"))

    settings_text = turtle.Turtle()
    settings_text.color("red")
    settings_text.penup()
    settings_text.hideturtle()
    settings_text.goto(400, -400)
    settings_text.write("Settings", align="center", font=("Courier", 40, "normal"))

setup1()

def setup_start1():
    global settings, starting_screen, name_question1, what_name_start1, playername1
    what_name_start1 = 1
    settings = 0
    starting_screen = 0
    name_question1 = turtle.Turtle()
    name_question1.speed(0)
    name_question1.color("white")
    name_question1.penup()
    name_question1.hideturtle()
    name_question1.goto(0, 0)
    name_question1.write("What's your name?", align="center", font=("Courier", 30, "normal"))
    playername1 = turtle.textinput("Enter Your Character's Name", "What's Your Character's Name?")
    name1()
    print("Player's Name:", playername1)
    name2()


def name1():
    global name_question2, name_question1
    name_question2 = turtle.Turtle()
    name_question2.speed(0)
    name_question2.color("white")
    name_question2.penup()
    name_question2.hideturtle()
    name_question2.goto(0, -100)
    name_question2.write(playername1, align="center", font=("Courier", 30, "normal"))


def starting():
    global starting_screen, settings, credits1
    #to be updated


def name2():
    global name_question1, name_question2, name_question3, sure1
    name_question1.clear()
    name_question3 = turtle.Turtle()
    name_question3.speed(0)
    name_question3.color("white")
    name_question3.penup()
    name_question3.hideturtle()
    name_question3.goto(0, 0)
    name_question3.write("Are You Sure?", align="center", font=("Courier", 30, "normal"))
    sure1 = turtle.textinput("Are You Sure?", "Are You Sure?")
    if sure1.lower() == "yes" or sure1.lower() == "y":
        name_question2.clear()
        name_question3.clear()
    else:
        print("test 'no' name")



def setup_settings():
    global graphics_text1, controls_text1, audio_text1, ui_text1, save_text1, settings, starting_screen
    settings = 1
    starting_screen = 0
    graphics_text1 = turtle.Turtle()
    graphics_text1.speed(0)
    graphics_text1.color("orange")
    graphics_text1.penup()
    graphics_text1.hideturtle()
    graphics_text1.goto(-600, 400)
    graphics_text1.write("Graphics", align="center", font=("Courier", 30, "normal"))
    #control setting text
    controls_text1 = turtle.Turtle()
    controls_text1.speed(0)
    controls_text1.color("orange")
    controls_text1.penup()
    controls_text1.hideturtle()
    controls_text1.goto(-350, 400)
    controls_text1.write("Controls", align="center", font=("Courier", 30, "normal"))
    #Audio setting text
    audio_text1 = turtle.Turtle()
    audio_text1.speed(0)
    audio_text1.color("orange")
    audio_text1.penup()
    audio_text1.hideturtle()
    audio_text1.goto(-150, 400)
    audio_text1.write("Audio", align="center", font=("Courier", 30, "normal"))
    #UI setting text
    ui_text1 = turtle.Turtle()
    ui_text1.speed(0)
    ui_text1.color("orange")
    ui_text1.penup()
    ui_text1.hideturtle()
    ui_text1.goto(-25, 400)
    ui_text1.write("UI", align="center", font=("Courier", 30, "normal"))
    #Save Menu Setting Text
    save_text1 = turtle.Turtle()
    save_text1.speed(0)
    save_text1.color("orange")
    save_text1.penup()
    save_text1.hideturtle()
    save_text1.goto(160, 400)
    save_text1.write("Save Menu", align="center", font=("Courier", 30, "normal"))
    

# Function to be called when the 'Escape' key is pressed
def on_escape_key():
    print("'Escape' key pressed")
    if settings == 1:
        save_text1.clear()
        ui_text1.clear()
        audio_text1.clear()
        controls_text1.clear()
        graphics_text1.clear()
        setup1()
    elif credits1 == 1:
        setup1()
    elif what_name_start1 == 1:
        name_question1.clear()
        name_question2.clear()
        name_question3.clear()
        setup1()

turtle.onkey(on_escape_key, "Escape")


def setting_text_click():
    global credits_text, start_text, title1, title2, settings_text
    # Clear the content of the turtles
    credits_text.clear()
    start_text.clear()
    title1.clear()
    title2.clear()
    settings_text.clear()
    setup_settings()


def start_text_click():
    global credits_text, start_text, title1, title2, settings_text
    credits_text.clear()
    start_text.clear()
    title1.clear()
    title2.clear()
    settings_text.clear()
    setup_start1()

def credits_text_click():
    global credits_text, start_text, title1, title2, settings_text, credits1, settings, starting_screen
    credits1 = 1
    starting_screen = 0
    settings = 0
    credits_text.clear()
    start_text.clear()
    title1.clear()
    title2.clear()
    settings_text.clear()

def click_mechanic1(x, y):
    global starting_screen, title1 
    print("testing 1, clicked at coordinates", x, y)
    if starting_screen == 1:
        if 260 <= x <= 450 and -400 <= y <= -350:
            setting_text_click()
        elif -279 <= x <= -120 and 60 <= y <= 100:
            print("test start Successful, clicked at coordinates", x, y)
            start_text_click()
        elif -514 <= x <= -287 and -392 <= y <= -349:
            print("Test Credits Successful, clicked at coordinates", x, y)
            credits_text_click()
        

data_start1 = [
"-277.0 98.0",
"-279.0 64.0",
"-126.0 62.0",
"-120.0 100.0"]

data_credit1 = [
"testing 1, clicked at coordinates -514.0 -349.0",
"testing 1, clicked at coordinates -287.0 -353.0",
"testing 1, clicked at coordinates -288.0 -392.0",
"testing 1, clicked at coordinates -511.0 -386.0"]

screen.onscreenclick(click_mechanic1)
# keep window open
turtle.mainloop()
