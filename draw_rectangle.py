
############################################################
# Daniel Jensen 6 July, 2022                               #
# Draw Rectangle is a program to draw a rectangle using    #
# user defined length and width.  The Canvas and Terminal  #
# scribe classes are from the Python Essential Training    #
# course on linkedIn Learning.                             #
# This was a practice challenge to write a function that   #
# draws a shape on the screen.  The draw_rectangle function# 
# and user input code are my own work.                     #
############################################################
import os
import time 
from termcolor import colored 

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)

# This Function draws a square based on user input
# Width and Height parameters
# Input: Width and Height input by user
# Output:  A drawing of a rectangle with the user entered dimensions 
def user_def_rectangle(width, height):
    # Draw the top of the rectangle
    for num in range(0,width):
        scribe.right()
    # Draw the right side of the rectangle
    for num in range(0, height):
        scribe.down()
    # Draw the bottom of the rectangle
    for num in range(0, width):
        scribe.left()
    # Draw the left side of the rectangle 
    for num in range(0,height):
        scribe.up()    

# Take user input in the form of a string
user_input = input("Input Height and width separated by a space: ")
user_list = user_input.split()  # Split by spaces

# Loop over the two values and type convert from string to int
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# Call the draw square function and pass in the user generated width and height
user_def_rectangle(user_list[0], user_list[1])







