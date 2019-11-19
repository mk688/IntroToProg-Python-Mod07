

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

# Example 1: Catching multiple error types
try:
    calculateBMI()
except (ValueError, TypeError) as error:
    print("Either Value or Type Error occurred:", error)
    print() # a line spacing

# Example 2: Catching a specific error
try:
    calculateBMI()
except ValueError as ve:
    print("There is a Value Error!:", ve)
    print()
except TypeError as te:
    print("There is a Type Error:", te)
    print() # a line spacing

# Example 3: Catching any errors using "Exception" and adding what to do if there is no error
# A finally clause is added, which is performed with or without an error.
try:
    calculateBMI()
except Exception as error:
    print("Error occurred:", error)
else:
    print("No error is found.")
finally:
    print("This is the end of a code.")
    print() # a line spacing

# Example 4: Raising an exception with an alias name
try:
    raise ValueError("Alias Name")
except ValueError as ne:
    print("There is an error: %s " % ne)
    print() # a line spacing

##################################################################################
# Demonstrate how pickling works
##################################################################################

# Define various types of test data to pickle
dataList = ['1', '2', '3']
dataDictionary = {"name":"Jane", "phonenumber":"123-456-7890"}
dataListTable = [{"task":"homework", "priority":"high"},{"task":"cook","priority":"low"}]

import pickle # import a package (typically on the top of a script)

fileName = "testpickle"
# Serialize Python object and write a file
fileObj = open(fileName,'wb') # write data in binary
pickle.dump(dataList,fileObj)
pickle.dump(dataDictionary,fileObj)
pickle.dump(dataListTable,fileObj)
fileObj.close()

# Read serialized data as Python object
fileObj = open(fileName,'rb') # read a binary data into Python object
print("Data pickled from a file")
print()
while True: # Read all data in the file
    try:
        loadData = pickle.load(fileObj)
        print(loadData)
    except EOFError: # break the while loop when it reaches the end of file
        print() # A line spacing for look
        print("End of file: No more data to write")
        break
fileObj.close()

