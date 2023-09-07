# Import turtule object, functions and the random package.
import turtle
from turtle import *
import random

# Hide the turtle for a *fancy* design and make it faster beacause we can
hideturtle()
turtle.speed(0)


# Print a square, the base of the dice.
def square(length):

    # Go to the center of the screen
    turtle.up()
    turtle.goto(-(length/2),-(length/2))

    turtle.down()

    # Draw the square
    for i in range(4):
        forward(length)
        left(90)


# The function to draw the circles (the dots of the dice)
def cercle(x, y, r):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


# The function to draw the dice
def dice(length, dots=1):
    
    # Set the dot's size value to an automatic one (if it was not set)
    # We cant do this in the function as it use a variable
    if dots == 1:
        dots = length/10
        
    # This funtcion is writed above and draw the square
    square(length)
    
    # Generating the vaule of the dice
    num = random.randint(1, 6)
    
    #To debug, you can then change the value of num
    #num = 6
      
    # Instead of using if num = 1; if num = 2;..
    # I use some math expressions to create dots which are in common for severals dice faces
    
    # Create the center dot if the random num is odd
    if (num % 2) == 0:
        pass
    else:
        cercle(0, -dots, dots)
    
    # Create the first two dots at two opposite corners if the nuber is not one (so the dots for 2, 3, 4, 5 and 6)
    if num != 1:
        
        # All of these caculs are used to let the user customize the size of the square and of the dotes of the dice, while keeping a margin between the dots and the square.
        # These caculs are not this interesting, it's most a lot of debuging and just work with the square function above
        #                # And Here, round*2.5 dosen't work. Don't ask me why.
        cercle((length/2) -(dots*2) +(dots/2), (length/2) -(dots*2.5) , dots)
        cercle(-(length/2) +(dots*2) -(dots/2), -(length/2) +(dots/2), dots)
    
    # If it's bigger that 3, we create the two mising dots at the two missing corners (for 4, 5 and 6)
    if num > 3:
        
        # Here it's the sames caculs than before but reverted and with somes tweaks
        cercle((length/2) -(dots*2) +(dots/2), -(length/2) +(dots/2), dots)
        cercle(-(length/2) +(dots*2) -(dots/2), (length/2) -(dots*2.5), dots)
    
    # As siw have two middle dots which are only use for this face, we create them separetly
    if num == 6:
        cercle((length/2) -(dots*2) +(dots/2), -dots, dots)
        cercle(-(length/2) +(dots*2) -(dots/2), -dots, dots)

#
# Then Finnaly we call the main function to generate the dice
# Create a dice with a square of 250px length and with dots with a size of 30
dice(250, 30)
