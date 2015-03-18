"""
an single player interpretation of the Dice Game Quixx
it programmed for learning purposes. So don't hit  me for a bad code ;)

author: Ch.Pohl
Date: 2015/03/16

"""
from random import randint

template_row = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
template_miss = ['1', '2', '3', '4']


colors = {1:"   Red: ", 2: "Yellow: ", 3: " Green: ", 4: "  Blue: "}


class Playingfield():

    playing_row = {1: [], 2: [], 3: [], 4: []}


    def draw_field_initial(self):
        row = 1
        while row <= 4:
            current = ""
            for c in range(0, len(template_row)):
                if row <3 :
                    current=current + " " + template_row[c]
                    self.playing_row[row].append(template_row[c])
                else:
                    current=template_row[c] + " " + current
                    self.playing_row[row].append(template_row[c])
            print " %s%s " %(colors[row],current)
            row += 1
        #playing_row[3].reverse()
        #playing_row[4].reverse()
        # print playing_row


    def draw_field_playing(self):
        row = 1

        for k in self.playing_row:
            line = ""
            for c in self.playing_row[k]:
                if row<3:
                    line = line+" " +str(c)
                else:
                    line = str(c)+" "+line
            print "%s%s" % (colors[k], line)
            row += 1

class Diehandling():

    dice = {"blue dice": 0, "red dice": 0, "yellow dice":  0, "green dice": 0, "1st white dice": 0,"2nd white dice": 0}


    def dice_roll(self):
        roll = 1
        result = ""

        for k in self.dice:
            self.dice[k]=randint(1,6)
            result=result + "[" + str(roll) + "] " + k + ": " + str(self.dice[k]) + " "
        print result


game = Playingfield()
rolls = Diehandling()

game.draw_field_initial()
game.draw_field_playing()
rolls.dice_roll()