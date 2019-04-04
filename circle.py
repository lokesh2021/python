from turtle import Turtle, Screen

# The snowman’s body should be made of 3 filled circles.

# The bottom circle should have a radius of 100 pixels.
# The middle circle should have a radius of 70 pixels.
# The top circle should have a radius of 40 pixels.

RADII = (100, 70, 40)

STAMP_SIZE = 20

# The snowman should be on a blue background
screen = Screen()

quinn = Turtle('circle')
quinn.setheading(90)
quinn.up()

# The outline of the snowman should be in black, and should be drawn filled with white.
quinn.color('black', 'white')

for not_first, radius in enumerate(RADII):

    if not_first:
        quinn.forward(radius)

    # The outline of each circle should be 3 pixels wide.
    quinn.shapesize((radius * 2) / STAMP_SIZE, outline=3)

    quinn.stamp()

    # Each circle should be centered above the one below it
    # There should be no gap between the circles.
    quinn.forward(radius)

# Give the snowman eyes

quinn.shapesize(15 / STAMP_SIZE)
quinn.color('black')
quinn.backward(3 * RADII[-1] / 4)

for x in (-RADII[-1] / 3, RADII[-1] / 3):
    quinn.setx(x)
    quinn.stamp()

# Give the snowman a mouth, and a nose (a hat is optional).

pass

# Make sure to include two stick-arms and at least two fingers on each hand.

pass

quinn.hideturtle()

screen.exitonclick()
