## Assignment 07
Author: Minsun Kim

Date: Nov 19, 2019

Class: IT FDN 100 A

### Introduction
This document describes how Python handles errors, what pickling means, how pickling is done in Python using some examples run in PyCharm and Python Shell.  It also provides some useful websites for reference and more examples in handling exceptions and pickling.

### How to Handle Exception in Python
Exceptions are the syntactically correct errors that occur during the execution of a Python code and the program will terminate with the built-in messages to indicate why it terminates without completing a job.  These messages are not necessarily user-friendly and there is a way to handle exceptions in the code to let the user know what kind of error has occurred. It also lets you continue the program if it is desired.  They are helpful especially when the programmer expects certain types of errors that could be made by the user.  
Let me demonstrate how this works in a very simple scenario, where the program asks the user to enter their weight, height, and name to compute the body mass index (BMI) for the user. I first create a header and a function to calculate BMI as shown in Figure 1.
```
# ------------------------------------------------- #
# Title: Assignment 07
# Description: create a script that demonstrates
# how Structured error handling and Pickling work.
# <MKim>,<11.19.2019>,Created Script
# ------------------------------------------------- #

##################################################################################
# Demonstration of Structured Error Handling
##################################################################################

# We use an example of calculating body mass index (BMI)
# from the weight and height entered by the user

# Define a function to calculate BMI
# We can expect that the user might enter a wrong data type,
# which will crash the program since the float type is required to compute BMI

def calculateBMI():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    name = input("Enter your name: ")
    BodyMassIndex = weight / (height ** 2)
    print("Computed BMI of %s is %f" % (name, BodyMassIndex))
    print() # a line spacing
    return
    
```

Figure 1. Script to perform a function to calculate a body mass index, which will be used in Assignment 07.

The programmer expects that the user may enter a string by mistake instead of a number for their weight or height, which will make the program crash since you cannot apply mathematical operators to a string type to compute BMI. In order to prevent the program from crashing when such event occurs, you can add an exception using try-except clause to the code.  Note that you can add multiple error types in a single except clause as shown in Figure 2a. Running the script in PyCharm and Python Shell are shown in Figure 2b and Figure 2c respectively.

```
# Example 1: Catching multiple error types
try:
    calculateBMI()
except (ValueError, TypeError) as error:
    print("Either Value or Type Error occurred:", error)
    print() # a line spacing
```
Figure 2a. Script to handle multiple exceptions at the same time.



