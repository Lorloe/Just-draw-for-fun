from turtle import *
wn = Screen()
t = Turtle()
color("red")
begin_fill()
pensize(14)
left (50)
forward(133)
circle (50, 200)
right (140)
circle (50, 200)
forward (133)
def write (mess, pos):
    x,y = pos
    t.penup()
    t.goto(x,y);
    t.color("red")
    style= ('Stencil std', 18, 'italic')
    t.write(mess, font=style)
write('A',(-80,115))
write('B',(80,-115))
write('X',(0,0))
write('N',(-65,115))
write('H',(-50,115))
write('i',(-10,115))
write('u',(-5,115))
write('E', (35,115))
write('M', (50,115))
wn.mainloop();
end_fill();