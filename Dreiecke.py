from turtle import *

def small_triangle():
    begin_fill()
    for i in range(3):
        forward(10)
        left(120)
    end_fill()
    forward(10)

def bigger_triangle():
    for i in range(4):
        small_triangle()
    left(120)
    forward(10)
    for i in range(2):
        for i in range(3):
            small_triangle()
        left(120)
        forward(10)
        
def very_big_triangle():
    for i in range(2):
        bigger_triangle()
        forward(30)
    left(120)
    forward(40)
    bigger_triangle()
    right(180)
    forward(50)
    right(60)

def very_very_big_triangle():
    for i in range(3):
        very_big_triangle()
        right(120)
        forward(80)
    forward(160)
    for i in range(3):
        very_big_triangle()
        right(120)
        forward(80)
    penup()
    left(90)
    forward(140)
    left(90)
    forward(80)
    right(180)
    pendown()
    for i in range(3):
        very_big_triangle()
        right(120)
        forward(80)
    
        
   
    
    
speed(0)
very_very_big_triangle()
    





