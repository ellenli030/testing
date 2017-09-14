Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

t.circle(10)

t.penup()
t.goto(0, -50)
t.pendown()
t.circle(60)

t.penup()
t.goto(0, -100)
t.pendown()
t.circle(110)

t.penup()
t.goto(0, -150)
t.pendown()
t.circle(160)

t.penup()
t.goto(-250, 10)
t.pendown()
t.forward(500)

t.penup()
t.goto(0, 250)
t.pendown()
t.setheading(270)
t.forward(500)

t.penup()
t.goto(-250, 220)
t.pendown()
t.setheading(320)
t.forward(700)

t.penup()
t.goto(250, 220)
t.pendown()
t.setheading(220)
t.forward(700)
SyntaxError: multiple statements found while compiling a single statement
>>> Visit http://www.python.org/download/mac/tcltk/ for current information.
SyntaxError: invalid syntax
>>> Visit http://www.python.org/download/mac/tcltk/ for current information.



