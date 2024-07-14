import turtle
import argparse

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

def snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    parser = argparse.ArgumentParser(description="Draw Koch snowflake with specified recursion level.")
    parser.add_argument("level", type=int, help="Recursion level for the Koch snowflake.")
    args = parser.parse_args()

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    level = args.level
    length = 400

    snowflake(t, length, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
