import turtle as t
t.bgcolor("red")
t.pensize(3)
t.speed(1000)
for i in range(30):#object 1 circle starts
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)#object 2 circle ends
t.bgcolor("orange")
t.pencolor("green")
t.penup()
t.goto(-400,200)
t.pendown()#object 2 circle starts
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):#object 2 circle ends
 t.circle(i*4)
t.bgcolor("yellow")
t.pencolor("red")
t.penup()
t.goto(400,200)
t.pendown()#object 3 circle starts
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)#object 3 circle ends
t.pencolor("indigo")
t.penup()
t.goto(400,-200)
t.pendown()
for i in range(30):#object 4 circle starts
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)#object 4 circle ends
t.pencolor("purple")
t.penup()
t.goto(-400,-200)
t.pendown()
for i in range(30):#object 5 circle starts
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)
for i in range(30):
 t.circle(i*4)
t.right(90)#object 5 circle ends
for i in range(30):
 t.circle(i*4)
t.right(90)
t.done()