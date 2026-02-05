import time
from turtle import Turtle
from player import Player







screen = Screen()
screen.setup(width = 600, height= 600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")
