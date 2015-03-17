"""
an single player interpretation of the Dice Game Quixx
it programmed for learning purposes. So don't hit  me for a bad code ;)

author: Ch.Pohl
Date: 2015/03/16

"""
from random import randint

template_row = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
template_miss = ['1', '2', '3', '4']
dice = {"blue dice": 0, "red dice": 0, "yellow dice":  0, "green dice": 0, "1st white dice": 0,"2nd white dice": 0}

colors = {1:"   Red: ",2:"Yellow: ",3:" Green: ",4:"  Blue: "}
def draw_field():
    row = 1
    while row <=4:
        current =""
        for c in range(0,len(template_row)):
            if row<3:
                current=current+" "+template_row[c]
            else:
                current=template_row[c]+" "+current
        print " %s%s " %(colors[row],current)
        row+=1
def dice_roll():
    roll=1
    result =""

    for k in dice:
        dice[k]=randint(1,6)
        result=result+"["+str(roll)+"] "+k+": "+str(dice[k]) +" "
    print result

draw_field()

dice_roll()