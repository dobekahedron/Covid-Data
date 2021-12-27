#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:46:21 2021
@author: bekahsmith

'''This program provides a visual of the spread of covid-19 beginning on January 3, 2020.
Each time the total number of new cases sextupled (6 times), the branches are doubled and change color.

"""
#----------------Setting things up-----------------------------
import turtle
import random
import csv

turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
panel.setup(width=1280, height=920)
panel.bgcolor('black')

#----------------Variables-------------------------------------

'''The following 3 lines are from: https://www.delftstack.com/howto/python/python-csv-to-dictionary/ '''
with open('covidglobalWHO.csv', mode='r') as inp:
    reader = csv.reader(inp) 
    coviddata = {rows[0]:rows[1] for rows in reader} # sets the key-value pairs in the new dictionary

cases = list(coviddata.values()) # this takes the dictionary called coviddata, and makes a list of all the values (number of new cases)

total = 1 # start with a case count of 1
doubled = total # the variable doubled will be updated to reflect the total case count. at the beginning of the pandemic, it matches the total number of new cases.
colorz1 = 30
colorz2 = 225

covid = turtle.Turtle(visible=False)
covid.width(4)
covid.color(colorz2,0,colorz1) # set a beginning color

branches = [covid]
covid.up()
covid.goto(-400,0)
covid.down()

#----------------Draw the data-----------------------------

for i in range(len(cases)): # cycles through each value in the list of cases
    for j in range(len(branches)):
        #found how to check if a number is odd or even, then make turtle turn left or right based on that outcome.
        #credit: https://www.javatpoint.com/python-check-number-is-odd-or-even
        '''Fun to experiment with different modulos, so it turns every...3 or 4 iterations?'''
        if (i % 2) == 0 and i <= 30:  # divides i by 2 and checks if there is a remainder, to determine if i is even
            branches[j].left(random.randint(40,60)) #turns the branches left on even rounds. Testing how to form branches with different angles based on time.
        elif (i % 2) > 0 and i <= 30: 
            branches[j].right(random.randint(40,60)) 
            
        elif (i % 2) == 0 and i > 30 and i <= 200: # beginning at 30 days into the pandemic, until 200 days, make smaller turns
            branches[j].left(random.randint(30,60))
        elif (i % 2) > 0 and i > 30 and i <= 200:
            branches[j].right(random.randint(30,60))    
            
        elif (i % 2) == 0 and i > 200: # even smaller turns. omg, so many branches, so much covid
            branches[j].left(random.randint(50,90))
        elif (i % 2) > 0 and i > 200:
            branches[j].right(random.randint(50,90))
        
        '''Fun to experiment with many different lengths to move forward in next line'''
        branches[j].forward(4) # take all of the branches forward for each line (day) of covid-19 data
        panel.update() # update the panel after each branch is drawn. Also tried updating after next if statement, but the animation looks better this way.

    doubled = doubled + (int(cases[i]))  # Here I am keeping a running total of cases.
    
    if doubled > total * 6: # Make changes to pattern each time the running total of cases has sextupled
        total = doubled # stores the new value of doubled cases
        if colorz1 <= 235: # adds a color gradient for g value (without going over 255)
            colorz1 += 5
        else:
            pass
        if colorz2 >= 10: # adds a color gradient for b value (without going under 0)
            colorz2 -= 10
        else:
            pass
        for j in range(len(branches)): # when cases double, each existing turtle is doubled
            location = branches[j].pos() # this saves the position of each turtle so the new turtle will be added in the same location
            newbranch = turtle.Turtle(visible=False) #creates the new turtle
            newbranch.width(4)
            newbranch.color(colorz2,0,colorz1) # uses new color values to add gradient each time cases have doubled
            newbranch.up()
            newbranch.goto(location) # go to the stored location
            newbranch.down()
            branches.append(newbranch) # add the new turtle to the list.
        
    else: # if cases weren't doubled on this day, don't do anything else.
        pass

#----------------End-----------------------------

turtle.done()