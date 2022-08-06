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
