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

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure2b.png "tooltip text")

Figure 2b. Running a script shown in Figure 2a in PyCharm.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure2c.png "tooltip text")

Figure 2c. Running a script shown in Figure 2a in Python Shell.

You can handle a specific error in each except clause.  The benefit of doing this way is that you can specify a task to do for each exception. The example script in this case is shown in Figure 3a. Running the script in PyCharm and Python Shell are shown in Figure 3b and Figure 3c respectively.

```
# Example 2: Catching a specific error
try:
    calculateBMI()
except ValueError as ve:
    print("There is a Value Error!:", ve)
    print()
except TypeError as te:
    print("There is a Type Error:", te)
    print() # a line spacing
```
Figure 3a. Script to handle a specific exception in each except clause.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure3b.png "tooltip text")

Figure 3b. Running a script shown in Figure 3a in PyCharm.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure3c.png "tooltip text")

Figure 3c. Running a script shown in Figure 3a in Python Shell.

An else clause followed by an except clause is used to perform a task when there are no exceptions specified prior to an else clause. A finally clause is put at the end of try-except clause. A finally clause is always executed no matter whether or not there is an exception while executing the code. A pseudo code to include try, except, else, and finally clauses is shown below.
 
![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure4.png "tooltip text")

Figure 4. Pseudo code for try-except-else-finally clause

If you want to handle any exceptions rather than a specific one, you can use “Exception” class as shown in Figure 5a.  Note that the except clause is performed only when the try clause results in exceptions. If the user enters a number as expected, then the except clause is skipped. The script to include all try-except-else-finally clause is shown in Figure 5a. Running the script in PyCharm and Python Shell without any exceptions are shown in Figure 2b and Figure 2c respectively.

```
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
```
Figure 5a. Script with try-except-else-finally clause

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure5b.png "tooltip text")

Figure 5b. Running a script shown in Figure 5a in PyCharm.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure5c.png "tooltip text") 

Figure 5c. Running a script shown in Figure 5a in Python Shell.

You can also “raise” an exception when a certain condition meets, which means that the program forces the exception to occur.  You can alias the name of the exception.  A simple script to raise an exception without any condition is shown in Figure 6a. 

```
# Example 4: Raising an exception with an alias name
try:
    raise ValueError("Alias Name")
except ValueError as ne:
    print("There is an error: %s " % ne)
    print() # a line spacing
```
Figure 6a. Script to raise an exception with the user-defined name.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure6b.png "tooltip text")

Figure 6b. Running a script shown in Figure 6a in PyCharm.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure6c.png "tooltip text")

Figure 6c. Running a script shown in Figure 6a in Python Shell.

A further example of handling exceptions is shown in the script written to demonstrate how pickle works in Figure 7.

### How to Pickle in Python

Pickle in Python means converting a Python object, e.g., list and dictionary, into a character stream before saving it into a file and converting the stream back to an object when it is loaded into Python environment from a file. In order to utilize this feature, you first have to import pickle package as shown in Figure 7. There are two main functions in pickle. The first one is dump, which serializes the data to store in a file.  The second one is load, which deserialize the data from a file with pickled data and loads it as a Python object. You use the second argument of “wb” or “rb” during writing or reading a file. The additional alphabet “b” next to w (write) or r (read) indicates a binary format.

Let me demonstrate how pickling works using a script (See Figure 7). I first created multiple variables in different data types (1) list, (2) dictionary, and (3) list table which contains two rows. I wrote these Python variables to a file using pickle and the content of this resulting file is shown in Figure 9. As you can see, the data is serialized so it cannot be read.   Then I read a file back into the Python environment and output what is read in Python environment. As shown in Figure 8, they match with my variables defined in my original script shown in Figure 7.

```
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
```
Figure 7. Script to show pickle works.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure8.png "tooltip text")

Figure 8. Content of a file written using pickle.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure9.png "tooltip text")

Figure 9. Running a script shown in Figure 7 in PyCharm.

![alt text](https://github.com/mk688/IntroToProg-Python-Mod07/blob/master/docs/Figure10.png "tooltip text")

Figure 10. Running a script shown in Figure 7 in Python Shell.

### Helpful websites

- A couple of useful websites I found to learn how Python handles exceptions are listed below.

https://www.pythonforbeginners.com/error-handling/exception-handling-in-python

I like the brevity of the explanation on this website. It is excellent for a quick reference (or refresher) to various exceptions to handle in Python.

https://docs.python.org/2/library/exceptions.html

This site is helpful to see what kinds of exceptions are available in Python and I can also find the hierarchy of the built-in exceptions.

- A couple of useful websites I found to learn how pickling works in Python are listed below.  

https://www.datacamp.com/community/tutorials/pickle-python-tutorial

This website has not only the explanation of what pickle is and how it is done but also explains what cannot be pickled. It is helpful to trouble shoot the problems I had while trying out pickling data.

https://pythontips.com/2013/08/02/what-is-pickle-in-python/

This website is written clearly for the beginners in Python and uses simple examples that are easy to understand.

### Summary
I was able to write my own demonstration of how structured handling errors work and how pickling works in Python. I also wrote a script to show handling several exceptions, serialize Python objects into a binary file and read serialized data back into Python object.

