import turtle
import time
import random

delayTime = 0.1
score = 0
highScore = 0

screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("pink")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(["red", "blue", "purple"])
shapes = random.choice(["square", "circle", "triangle"])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

penScore = turtle.Turtle()
penScore.speed(0)
penScore.shape("square")
penScore.color("black")
penScore.penup()
penScore.hideturtle()
penScore.goto(0, 250)
penScore.write("Score: 0  High Score: 0", align="center", font=("sans serif", 24, "normal"))


def goUp():
    if snake.direction != "down":
        snake.direction = "up"

def goDown():
    if snake.direction != "up":
        snake.direction = "down"

def goLeft():
    if snake.direction != "right":
        snake.direction = "left"

def goRight():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

screen.listen()
screen.onkeypress(goUp,"w")
screen.onkeypress(goDown, "s")
screen.onkeypress(goLeft, "a")
screen.onkeypress(goRight, "d")

segments = []

while True:
    screen.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        penScore.clear()
        penScore.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if snake.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delayTime -= 0.001
        score += 10
        if score > highScore:
            high_score = score
        penScore.clear()
        penScore.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            penScore.clear()
            penScore.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delayTime)

wn.mainloop()