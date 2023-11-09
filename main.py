


'''
import colorgram
colors= colorgram.extract("palette.png",30)
print(colors)

rgb_colors=[]

for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

'''
import random
import turtle as tm

tm.colormode(255)
timmy= tm.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.shape("turtle")
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0) # derece

color_list=[(232, 229, 205), (207, 223, 236), (128, 167, 199), (199, 165, 108), (199, 140, 173), (221, 211, 108), (211, 233, 223), (158, 60, 126), (229, 209, 221), (52, 106, 158), (186, 154, 39), (202, 80, 133), (122, 191, 161), (148, 102, 49), (41, 173, 127), (151, 18, 97), (226, 166, 189), (14, 145, 107), (159, 213, 184), (175, 187, 219), (96, 118, 180), (34, 164, 198), (144, 209, 226), (240, 223, 9), (165, 25, 17), (88, 16, 80), (35, 35, 177), (216, 71, 63)]

number_of_dots=100
for dot_count in range(1,number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen=tm.Screen()
screen.exitonclick()
