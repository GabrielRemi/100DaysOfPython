import time
from turtle import Screen, Turtle

def main():
    turtle = Turtle()
    turtle.shape("turtle")
    screen = Screen()

    screen.listen()
    screen.onkey(lambda: turtle.forward(10), "d")
    screen.onkey(lambda: turtle.backward(10), "a")
    screen.onkey(lambda: turtle.right(10), "s")
    screen.onkey(lambda: turtle.left(10), "w")
    screen.onkey(turtle.clear, "c")

    screen.exitonclick()



if __name__ == '__main__':
    main()