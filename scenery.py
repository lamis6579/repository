
'''
    This program is responsible for making a 4-layered pink cake placed on a 4 legged table, based on a few user inputs 
    such as the length of the table and the size of the cake layer. 

    Heer's repository: https://github.com/HeerKGit/h-first-repository
    Nastassaya's respository: https://github.com/Nastassya1719/NRepository1
    Lamis's repository: https://github.com/lamis6579/turtle.py


'''

import turtle

# function responsible for calculating the radius of the semi-circle we require as the frosting for our cake. 
def radius(layer_size):
    radius = ((layer_size - 90) // 10)
    return radius


# procedure for adjusting the position of the turtle so the icing can be drawn properly. 
def adjust_pos_icing(layer_size):

    turtle.penup()
    turtle.pencolor('black')
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)

# procedure for drawing the candle on the top most layer of the cake. 
def candle(layer_size):
    r = radius(layer_size)
    turtle.penup()
    turtle.pencolor('crimson')
    turtle.right(90)
    turtle.forward((r * 4.5) + 1.5) # it moves 4.5 radius' forward and adds 1.5 to palce the candle right in the center. 
    turtle.right(90)
    turtle.begin_fill()
    turtle.pendown()
    turtle.fillcolor('crimson')
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(25)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(2.5)
    turtle.right(90)
    turtle.begin_fill()
    turtle.fillcolor('dark orange')
    turtle.pencolor('dark orange')
    turtle.circle(6.5,110)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0,0) # moves turtle to where it began from ('home')


# procedure to create the frosting on the top most layer of the cake. 
def cake_frosting(layer_size):

    r = radius(layer_size)

    turtle.begin_fill()
    turtle.fillcolor('saddle brown')
    turtle.circle(r,180) # 180 degrees allows us to create a semi-circle
    turtle.right(180)
    turtle.end_fill()


# this function is used to create layers of the cake.
def cake_layers(layer_size, height, color_layer): 
    
    turtle.right(90)
    turtle.fillcolor(color_layer) # passing different colors for different layers. 
    turtle.pencolor(color_layer)
    turtle.begin_fill() # this will start the coloring process.
    turtle.pendown() # put the pen down to start drawing.
    turtle.forward(layer_size) # starts drawing the cake
    turtle.left(90) 
    turtle.forward(height) # the height of the layer
    turtle.left(90)
    turtle.forward(layer_size)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill() # this will finish filling the color of the layer. 
    turtle.left(180)
    turtle.forward(height)
    turtle.right(90)

    '''
    the command below ensures that all the layers of the cake are centered.
    We chose to move forward 15 because we are subtracting 30 from the layer size as we go. 
    So this ensures that theres a space of 15 px left between each side of the layer 
    below to draw the new layer in the center above.
    '''

    turtle.forward(15)  
    turtle.left(90)


def table(table_length, table_color, layer_size):

    '''
    this is just a procedure to create the table that the cake will go over. This table will have 4 legs.
    '''

    # initialised variables for the length of the big and small leg. 
    big_leg = (table_length * 0.5)  
    small_leg = (table_length * 0.25)

    turtle.pencolor(table_color)
    turtle.penup()
    turtle.goto(-120, -100) # after playing around with the coordinates, I decided where I want to begin drawing my table from. 
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(table_color)
    turtle.forward(table_length)
    turtle.left(90)
    turtle.forward(15) # 15 px is the height of the first rectangle. 
    turtle.left(90)
    turtle.forward(table_length)
    turtle.left(90)
    turtle.forward(15)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.fillcolor(table_color)
    turtle.forward(big_leg)
    turtle.left(90)
    turtle.forward(15) # 15px is is the width of the legs.
    turtle.left(90)
    turtle.forward(big_leg)
    turtle.right(90)
    turtle.forward(20) # space of 20px left between two legs.
    turtle.right(90)
    turtle.forward(small_leg)
    turtle.left(90)
    turtle.forward(15) 
    turtle.left(90)
    turtle.forward(small_leg)
    turtle.right(90)
    turtle.forward((table_length - 100)) # calculation to ensure that all 4 legs are on the same distance from each other and are centered for each table. 
    turtle.right(90)
    turtle.forward(small_leg)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(small_leg)
    turtle.right(90)
    turtle.forward(20) # space of 20px between both legs. 
    turtle.right(90)
    turtle.forward(big_leg)
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(big_leg)
    turtle.left(90)
    turtle.end_fill()
    turtle.forward(table_length)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward((table_length - layer_size) // 2) # this ensures that the cake is centered on the table. 
    turtle.left(90)


# main function which takes in user inputs and calls functions accordingly/in order. 
def main():

    turtle.speed(5) 
    turtle.screensize(1280, 800) 
    turtle.setup(1280, 800)
    turtle.bgcolor('light blue')
    turtle.hideturtle() # hiding the turtle so the drawing can be done smoothly.

    table_color = input('Please enter the color of the table: ')
    table_length = int(input('Please enter length of table. It should be between 150 - 400: '))
    layer_size = int(input('Please enter the cake size. You can choose any value between 150 - 400. Note that the cake size should be equal to or smaller than the table size: '))
    table(table_length, table_color, layer_size)

    print ('Your cake is loading... Happy Birthday!')

     
    cake_layers(layer_size, 30, 'pale violet red' )

    # we keep subtracting 30 from the layer size after the first layer is made so that we can create a realistic cake look.
    cake_layers(layer_size - 30, 30,'light pink' )
    cake_layers(layer_size - 60, 30, 'misty rose')
    cake_layers(layer_size - 90, 30, 'seashell')

    adjust_pos_icing(layer_size) 

    # calling the cake_frosting procedure 5 times as we have created the semi-circles in such a way that exactly 5 would cover the whole top layer. 
    cake_frosting(layer_size)
    cake_frosting(layer_size)
    cake_frosting(layer_size)
    cake_frosting(layer_size)
    cake_frosting(layer_size)

    candle(layer_size)

main()

input('Press any key and enter to exit: ')
quit()


