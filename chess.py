import turtle

def main():
     t=turtle
     t.penup()
     s=30
     for column in range(0,8):
         for row in range(0,8):              
              t.goto(s+row*s,s+column*s)
              if (row+column)%2==0:
                   square(s,row,column,"black")
              

def square(s,row,column,color):
     t=turtle
     t.penup()
     t.fillcolor(color)
     t.begin_fill()
     t.penup()
     for count in range(4):
          t.pendown()
          t.forward(s)
          t.left(90)
     t.end_fill()
     t.penup()
main()
