######################################################################
# Script Name: Assignment2.py
# Title: VAriable declaration, data types and data structures in Python
# Description: This file teaches varibale declaration, data types, 
# basic arithmetic, and date structures in Python.
# Author: Edgar Gonzalez
# Date:  September 11, 2022 
######################################################################

# Sample declaration and initialization of variables:
myBirthYear = 2000          # int: integer. Only whole numbers
myWeightLbs = 160.0         # flt: float. Fractional values as decimal
myFirstName = 'Edgar'       # str: string. Any sequence of characters
myGender = 'M'              # str: also a string!
isATeacher = False          # bool: Boolean. Can only hold True or False.

# TODO 1: Complete the following print statements:
print( 2000 )         # TODO 1.1: Print the value of myBirthYEar.
print( 160.0 )        # TODO 1.2: Print the value of myWeight.
print('Edgar')        # TODO 1.3: Print the value of myFirstName.
print('M')            # TODO 1.4: Print the value of myGender.
print(False )         # TODO 1.5: Print the value of isATeacher.

# TODO 2: Complete the following assignment statements:
myBirthYear = 2000            # TODO 2.1: assign with your birth year.
myWeightLbs = 160.0           # TODO 2.2: assign with your weight (or made up).
myFirstName = 'Edgar'         # TODO 2.3: assign with your first name.
myGender = 'M'                # TODO 2.4: assign with your gender.
isATeacher =  False           # TODO: 2.5: assign with the correct value, per the name.

# TODO 3: Assign the following with new values:
myAge = 22
print(myAge)                               # TODO 3.1: current year minus the value of myBirthYear.
myWeight = '72.57kgs'
print(myWeight)                         # TODO 3.2: convert myWeightLbs to Kilogram equivalent: Kg = lbs / 2.2046
Fullname = 'Edgar Gonzalez'
print(Fullname)              # TODO 3.3: add your last name after the value myFirstName, include a space. example: 'John Doe'
isGreaterThan = 7 > 3 
print(isGreaterThan)                   # TODO 3.4: compare any two numbers using the greater than operator.

# TODO 4: Use a print statement to combine 3 of the variables from TODO 3 in a single sentence of your choosing:
# TODO  : HINT: you can use any concatenation method to combine the values.
print(Fullname, myAge, myWeight)

# TODO 5: Do the following
# TODO 5.1:  declare a List that includes a string of your first name,
# TODO 5.1: integer of your age, string of your state of residence, estimate fraction of how many year you have
# TODO 5.1: lived in that state.
demoList = ['Edgar' , 22 , 'Texas' , 18.5 ]
# TODO 5.2: Now, using the list you just created, use 2 print statements to create the following output.
# TODO 5.2: (don't include quotes, replace [values] with your data from your list, don't include [ ] brackets.)
# TODO 5.2: "Hello, my name is [nathan] and I am [32] years old."
# TODO 5.2: "I have lived in [Oregon] for about [7.5] years."
print('Hello, my name is Edgar and I am 22 years old.')
print('I have lived in Texas for about 18.5 years.')

# TODO 6: Do the following
# TODO 6.1: Using examples from the reading, declare a Dictionary, as you did in TODO 5.1, using the
# TODO 6.1: key names: name, age, state, years
demoDictionary = { 
    'name': 'Edgar',
    'age': 22,
    'state': 'Texas',
    'years': 18.5}
# TODO 6.2: Now, using the dictionary you just created, use 2 print statements to create the following output.
# TODO 6.2: (don't include quotes, replace [values] with your data from your list, don't include [ ] brackets.)
# TODO 6.2: "Hello, my name is [nathan] and I am [32] years old."
# TODO 6.2: "I have lived in [Oregon] for about [7.5] years."
print('Hello my name is ' + demoDictionary['name'] + ' and I am ' + str(demoDictionary['age']) + ' years old.')
print('I have lived in ' + demoDictionary['state'] + ' for about ' + str(demoDictionary['years']) + ' years.')
