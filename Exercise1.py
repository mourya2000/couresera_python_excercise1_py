# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:22:58 2021

@author: Vivek Mourya
"""

#%%
def hello():
    ''' prints hello world'''
    print("hello, world")
    
#%%
def areaofcircle(radius):
    """ Computers the area of circle of the given radius """
    area = 3.14*radius**2
    print("The area of a circle of radius",radius,"is",area)
    
#%%

"""
Exercise:
write a function 'def areatriangle(b,h)' to compute the area
of a triangle: formula is area =.5*b*h.

You can test your function by execting the following codes:
"""

#%%
    # the following codes will test areatriangle()
    areatriangle(3,5)
    areatriangle(2,20)
    areatriangle(23,54)
    areatriangle(9,21)
#%%
'''
Solution:
'''

#%%
def areatriangle(b,h):
    # this function is run all the given areatriangle
    # b=base, h=hight
    area = 1/2*b*h
    print("The area of triangle base",b,"and height",h,"is",area)
    
    
#%%
name = "His name is Canan O'Brien"
cat = 'My cat is named "Butters"'
print(name)
print(cat)

#%%

""" 
If you need both a ' and " in you string, you can use the escape
character \ which tells Python that the following character is to be
taken as the literal character and is not a quote to delinit the string. See it
in action esacping the " below:
    
"""

#%%
both = "My cat's name is \"Butters\""
print(both)

#%%
def fehrenhit_to_celsius(temp):
    """ Converts fehrenhit temperature to Celsius.
    fourmula is 5/9 of temp minus 32 """
    # end='' keeps print from starting a new line.
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit temerature", temp," is equivalent to",newTemp, end='')
    
    
#%%

"""
Excercise 2:
    Write a function 'def celsius_to_fahrenheit(temp)' to convert Celsius
    to Fahrenheit temperature. The farmula is (9/5 times temp plus 32.
    print the output in the form:
The Celsius temperature 50 is equialent to 122 degree Fahrenheit.

"""

#%%
# the following will test the above function
celsius_to_fahrenheit(100)
celsius_to_fahrenheit(0)
celsius_to_fahrenheit(58)
celsius_to_fahrenheit(76)

#%%

def celsius_to_fahrenheit(temp):
    """ Convert to Celsius to Fahrenheit.
        Fourmula is 9/5 temp plus 32 """
    new_temp = (9/5)*temp + 32
    print(" The Celsius temperature", temp, "is equivalent to", new_temp, end=' ')
    print("degree fahrenheit.")
    
    
    
#%%
def name():
    """ Input first and last name. compbaine to one string and print"""
    
    fname = input("Enter your first name here :")
    lname = input("Enter your last name here :")
    fullname = fname + " " + lname
    print("Your name is :", fullname)
    
#%%

"""
Exercise:
    Extend the name function written in class to include the city and state.
That is, ask two more questions to get the city and the state you live in.
Print where you are from on a new line. Put the customary comma between
city and state. to save time, here is the starting function.
Your run should look like the following (even if this is not the customary
way in your country):
"""    
#%%
def name():
    """ Input first and last name, combaine to one string and print
        Also, input city and state and print """
        
    fname = input(" Enter your first name : ")
    lname = input(" Enter your last name : ")
    full_name = fname + " " + lname
    city = input(" Enter your city name : ")
    state = input(" Enter your state name : ")
    city_state = city + " " + state
    
    print("Your name is :",full_name)
    print("You live in : ",city_state)
    
#%%
    """ Three slightly difference version if-if, if-else, if-elif-else"""
    x = 5
    y = -7
    z = 0
    if x > 0:
        print("x is positive")
    if x < 0:
        print("x is nagative")
    
    if y > 0:
        print("y is positive")
    else:
        print("y is nagative")
    
    if z > 0:
        print("z is postive")
    elif z < 0:
        print("z is nagative")
    else:
        print("z must be zero")
        
        
#%%
    """ Python equality """
    x = 5
    y = 5
    z = 4

#%%
    print("x is equal to y",x == y)
    print("x is not equal to y",x != y)
    print("x is equal to z",x == z)
    print("x is not equal to z",x != z)
    
#%%
def area(type_,x):
    """ Computes the area of square or a circle.
        type_ must be the string "circle" or string "square"
        We use type_ here, because type is Python keyword."""
    if type_ == "circle":
        area = 3.14*x**2
        print(area)
    if type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one")
        
#%%
"""
Exercise:
Write a function absolutevalue(num) that computes the absolute value of
a number. You will need to use an 'if' statement. Remember if a number is 
less than zero then you must multiply by -1 to make it greater than zero.
Give output in the form:

The absolute value of -5  is  5
"""

#%%
absolutevalue(5)
absolutevalue(-5)
absolutevalue(4-4)
#%%
def absolutevalue(num):
    if num >= 0:
        abs_num = num 
    else:
        num < 0
        abs_num = -num
        
    print("The absolute value of",num,"is",abs_num)
    
    
#%%
def fahrenheit_to_celsius1():
    """ BAD. Does not check input before using it. 
    Input from keyboard, which is always a string and must often be
    converted to an int or float. 
    Converts Fahrenheit temp to Celsius.
    """
    
    temp = float(input("Enter the value of Fahrenheit : "))
    newtemp = 5*(temp-32)/9
    print("The fahrenheit temprature",temp,"is equvalent to",newtemp,"degree celsius")
    #print("The fahrenheit temprature",temp,"is equvalent is",end=' ')
    #print(newtemp,"degree celsius")
    
#%%
def fahrenheit_to_celsius2():
    """ IMPROVED. Does some checking of input before using it.
    Input from keyboard, which is always a string and must often be
    converted to an int or float. 
    Converts Fahrenheit temp to Celsius.
    Uses 'if' to make sure an entry was made.
    """
    
    temp_str = input("Enter the Fahrenheit temprature :")
    if temp_str:
        temp = int(temp_str)
        newtemp = 5*(temp-32)/9
        print("The fahrenheit temprature",temp,"is equvalent to", end=' ')
        print(newtemp,"degree celsius")
    
#%%
def fahrenheit_to_celsius3():
    """ MORE IMPROVED. Does even more checking of input before using it. 
    Input from keyboard, which is always a string and must often be
    converted to an int or float. 
    Converts Fahrenheit temp to Celsius.
    Uses if to check whether input is a number and then uses .isdigit() method 
    of strings to check whether input is made of of digits. 
    """
    temp_str = input("Enter fahrenheit temprature : ")
    if temp_str:
        if temp_str.isdigit():
            temp = int(temp_str)
            newtemp = 5*(temp-32)/9
            print("The fahrenheit temprature",temp,"is equvalent to", end=' ')
            print(newtemp,"degree celsius")
        else:
            print("You must enter a number. Bye")
            

#%%
def inches_to_feet1(inches):
    '''Convert inches to feet and inches '''
    feet = inches//12
    extra_inches = inches%12
    print(inches,"inches is to",feet,"feet and",extra_inches,"inches")
    
#%%
"""
Exercise: Rewrite inches_to_feet1(inches) calling it inches_to_feet2(inches)
using % to compute the inches. Recall that 19 % 5 will give 4 (the remainder).
Copy and paste the original into the solution area and modify to same typing 
time.
"""
#%%
def inches_to_feet2(inches):
    feet = inches//12
    extra_inches = inches%12
    print(inches,"inches is to",feet,"feet and",extra_inches,"inches")
    
#%%
"""
The 'while' loop. Loops are used to repeat actions and the scope of this
repetition is indicated by the indention after the 'while' statement.
"""
#%%
def cheer():
    """ Prints 2 4 6 8, who do we appreciate .... Note that everything in 
    the while loop is indented. The first line not indented is the first
    line following the while loop. """
    
    ct = 2
    while ct <= 8:
        print(ct,end=' ')    # end=' ' or end = " " keep to starting a new line
        ct = ct + 2
    print()         # now we'll start new line
    print("Who do we appreciate")
    print("COURSERA!")
    
    
#%%
def count_down():
    num = 10
    while num > 0:
        print(num,end=' ')
        num = num - 1
    print()
    print("BLASTOFF!")
    
#%%
"""
The 'for' loop. This loop uses an iterator to determine how many times to go
through the loop. The iterator we use below is 'range(start, stop, step)'.
"""
#%%
def cheer2():
    for num in range(2,9,2):
        print(num,end=' ')
    print()
    print("Who do we appreciate")
    print("COURSERA!")
    
    
    

#%%
def count_down2():
    for num_ in range(10,0,-1):
        print(num_,end=' ')
    print("BLASTOFF!")
    
    
