#!/usr/bin/env python
# coding: utf-8

# # CECS 229 Sample Assignment: Python Review
# 
# #### Due Date:
# 
# N/A
# 
# #### Objectives:
# 
# 1. Review Python functions and classes.
# 2. Know how to convert an .ipynb file to .py
# 3. Understand how to submit work to and read feedback given by, CodePost.
# 
# ### Directions 
# 
# Complete the programming problems below.  When you are finished, convert your notebook to a .py file named `sample.py` and submit it to the appropriate CodePost auto-grader folder.  Please note that this assignment is for practice only and does not affect your grade.
# 
# Review on functions and classes are provided at the end of this notebook for your reference.

# -----------------------------------
# #### Problem 1:
# 
# Create a function `hello(subject)` that returns the string “Hello, (insert subject here)!” using the input subject.
# 
# INPUT: `subject` - a string representing the subject to include in the greeting
# 
# OUTPUT: the greeting as a string

# In[12]:


def hello(subject):
    return f"Hello, {subject}!"


# ----------------------------------------------------------------------------
# #### Problem 2
# 
# Create a class named `Bug` with the following attributes and interface implementation:
# 
# * **Attributes:**
#     - `name` – a string representing the name of this `Bug` object.
#     - `position` – a list with two elements, representing the location of the Bug object on the xy-plane.  The first element represents the x-coordinate, while the second element represents the y-coordinate.
# * **Interface:**
#     - `__init__(self, name, position = [0, 0])`: constructor that initializes a Bug object with given name and position.  If the position is not given, then the Bug’s position is initialized at the origin.
#     - `move_up(self, units)`: moves the position of this Bug object up by given number of units (int).
#     - `move_down(self, units)`: moves the position of this Bug object down by given number of units (int).
#     - `move_left(self, units)`: moves the position of this Bug object left by given number of units (int).
#     - `move_right(self, units)`: moves the position of this Bug object right by given number of units (int).
#     - `__str__(self)`: returns a string representation of this Bug object containing the name and position.  The string should be formatted as follows:
#                 Name: <insert name here>
#                 Position: (<insert x>, <insert y>)
# 

# In[ ]: 

class Bug:

    def __init__(self, name, position = [0,0]):
        self.name = name
        self.position = position
    
    def move_up(self, units):
        x = self.position()[0]
        y = self.position()[1]
        self.position = [x, y+units]

    def move_down(self, units):
        x = self.position()[0]
        y = self.position()[1]
        self.position = [x, y-units]

    def move_left(self, units):
        x = self.position()[0]
        y = self.position()[1]
        self.position = [x-units, y]

    def move_right(self, units):
        x = self.position()[0]
        y = self.position()[1]
        self.position = [x+units, y]
    
    def __str__(self):
        print("Name: " + self.name + "\nPosition: " + str(self.position))




# -----------------------------------
# ## Review on Functions
# 
# In programming, a ***function*** is a named block of reusable code.  Functions increase the readability of a program by eliminating the need for duplicate lines of code.  Instead, a single function call replaces the duplicate lines.  Functions may or may not take arguments to execute its purpose.  Functions always return either a null value or an intended value.  Below are basic syntax outlines for writing functions in Python:
# 
# **SYNTAX: Function without arguments nor intended return**
# 
# `def func_name():
#     # body goes here
#     return # "return with no value will default to "None"
# `
# 
# Note: If no intended return is specified, then the Python null value, `None` is returned.
# 
# 
# **SYNTAX: Function with arguments and intended return**
# 
# `def func_name(arg1, arg2, ...):
#     # body goes here
#     return value   
#     `
#     
# **Examples:**

# In[12]:


from random import randint

def print_greeting():
    """This function prints a random greeting""" # doc string
    greetings = ["Hello!", "Hi!", "Hola!", "Hi there!", "What's cracking?!", "Sup.", ":)"]
    print(greetings[randint(0, len(greetings)-1)]) # randint --> random module
    return


# In[8]:


# for i in range(10):
#     print(f"Greeting #{i+1}: ", end = "")
#     print_greeting()


# In[11]:


# print(print_greeting()) # prints a random greeting but also returns "None"


# In[20]:


def square(n):
    """
    This function returns the square of the given value.
    A value error is raised if the given argument is not numeric
    INPUT: n - numeric value
    OUTPUT: the square of n
    """
    if type(n) != float and type(n) != int:
        raise ValueError("Argument must be of type 'float' or 'int'") # this is calling the constructer of the ValueError class.
        # by raising an error, all execution og the program calling this function will be terminated (only if statement is True)
    return n * n


# In[15]:


# square(3)


# In[21]:


# square(3/2)


# In[22]:


# square(1.5)


# In[23]:


# square('hi') # test ValueError for square() here


# In[29]:


'''
The following function contains an error.  Python uses assignment statements to bind variable names to values.
If the values are manipulated, a new object is created in memory storing the result of the manipulataion and 
the variable name is rebound to this new object. i.e., the original value is not replaced.

Can you identify where the error is happening?

ANSWER: does not properly change the array. Multiplying the elements, but new value is stored to a new location of memory. Values never associated back to array
'''

def double_arr(arr):
    """
    this function doubles the values in the given array
    INPUT: arr - a list of numeric values.
    OUTPUT: None
    """
    for ele in arr:
        ele *= 2    # In Python, a variable is assigned to a computed value, after the computation has been made in a different memory cell 
        # (i.e., not the oiginal location of the element in the array)
    return


# In[30]:


# values = [1, 2, 3, 4, 5]
# double_arr(values)
# print(values)


# In[33]:


'''This is a corrected version of the function defined above'''

def double_arr(arr):
    """
    this function doubles the values in the given array
    INPUT: arr - a list of numeric values.
    OUTPUT: None
    """
    # can fix by using a different type of loop
    for i in range(len(arr)):
        arr[i] *= 2    # array at someplace multipled by 2
    return 


# In[32]:


# values = [1, 2, 3, 4, 5]
# double_arr(values)
# print(values)


# ----
# 
# ## Review on Classes
# 
# In programming, a ***class*** is a blueprint for an object.  A class defines what attributes and behaviors an object will support.  Classes are used when a program needs several objects that behave the same but might hold different data.  
# 
# For example, a software program that keeps track of student enrollment needs to model a single `Student` object with attributes name, ID, and courses with corresponding grades.  It also needs to define behaviors for
# 
# 1. adding a course to the student record,
# 2. recording letter grades for the courses the student is enrolled in,
# 3. calculating the student's GPA,
# 4. printing the student's record.
# 
# Once this blueprint is defined, it can keep a log of several `Student` instances, i.e. objects, and manipulate them to perform the desired tasks.
# 
# The behaviors of an object are defined using a special function called a **method**.  The main difference between a function and a method is that a method can only be called on an object of the class that defines it.  For example, if `student1` is a `Student` object and `get_gpa()` is a method that the class defines, then the syntax for calling `get_gpa()` on `student1` is `student1.get_gpa()`. In Python, all methods defined by a class must include a special argument called `self`.  `self` is a keyword that is used to reference that the current object.
# 
# 
# **SYNTAX | Class Method**
# 
# `class ClassName:
#     ... 
#     def method1(self, other parameters):
#         #body goes here
#         return
# `
# 
# The **attributes** of an object are the data associated to the object.  A class defines what data an object of the class will have in a special method called a constructor.  In Python, the syntax for defining a constructor and default data is as follows:
# 
# **SYNTAX | Class Attributes**
# 
# `def ClassName:
#     def __init__(self, arg1, arg2, ...): # constuctor
#         self.attribute1 = arg1
#         self.attribute2 = arg2
#         ...
#         return
# `
# 
# We can define how built-in functions and operations act on objects of our defined classes by implementing special methods.  One example of such a method is `__str__`.  The `__str__` method returns the string representation of an object, that is, it defines what string to return should the built-in function `str()` be called on an instance of the class.  Other special methods that can be implemented are:
# 
# * `__len__` - defines what integer to return if the function `len()` is called on an instance of the class.
# * `__bool__` - defines what Boolean value to return if the `bool()` function is called on an instance of the class.
# * `__lt__` - defines what the operator `<` should return if it is used to compare two instances of the class. 
# * `__gt__` - defines what the operator `>` should return if it is used to compare two instances of the class.  
# * `__eq__` - defines what the operator `==` should return if it is used to compare two instances of the class. 
# * `__le__` - defines what the operator `<=` should return if it is used to compare two instances of the class. 
# 
# When we implement special methods of this type in our classes, we say we are *overloading* the relevant functions/operators.  You can find more information on overloading built-in operators and functions [here](https://realpython.com/operator-function-overloading/).
# 
# To summarize, a class defines the attributes (data) and the behaviors (actions on data) allowed for a certain type of object.  It can also overload built-in operators and functions so that they work on instances of the class.

# In[3]:


class Student:
    
    valid_grades = {'A' : 4.0, 'B' : 3.0, 'C' : 2.0, 'D' : 1.0, 'F': 0.0, 'W' : 'na', 'IP' : 'na', 'P' : 'na', 'NP' : 'na'}
    
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
        self.courses = {} # empty dictionary (key-value)
        
    def enroll(self, course, term):
        self.courses[course] = [term, 'IP'] # creates new key-value pair. 
        # Key: the course (string)
        # Value: term and grade (list)
        return 
    
    def record_grade(self, course, grade):
        if grade not in Student.valid_grades:
            raise ValueError("Invalid letter grade given.")
        if course not in self.courses:
            raise ValueError("Course not in student's record.")  
        self.courses[course][1] = grade
        return
    
    def get_gpa(self):
        grd_pts = 0
        num_courses = 0
        for course, details in self.courses.items():
            
            letter_grade = details[1]
            pts = Student.valid_grades[letter_grade]
            if type(pts) == float:
                grd_pts += pts
                num_courses += 1
        return grd_pts/num_courses
    
    def print_record(self):
        print("-"*40 + f"\nName: {self.name}\nID: {self.uid}\n")
        for course, details in self.courses.items():
            print("\tCourse: %-20sTerm: %-20sGrade: %s" % (course, details[0], details[1]))
        print("\nGPA: %.2f" % self.get_gpa())
        return
    
    def __str__(self):
        return f"Name: {self.name}\nUID: {self.uid}"
        # example of overloading. See information about attritubes of specific object
        # returns Student Name and University ID

#     # practice
#     def __len__(self): 
#         """overrload the len() built-in function so that it returns the number of courses that the student is enrolled in"""
#         return len(self.courses)


# In[11]:


# jane = Student("Jane Doe", "000-000-001")

# jane.enroll("CECS 274 SEC 01", "Spring 2022")
# jane.enroll("CECS 174 SEC 02", "Fall 2022")
# jane.enroll("MATH 247 SEC 01", "Fall 2022")
# jane.enroll("CECS 229 SEC 02", "Spring 2023")

# jane.record_grade("CECS 274 SEC 01", "A")
# jane.record_grade("CECS 174 SEC 02", "A")
# jane.record_grade("MATH 247 SEC 01", "B")


# joe = Student("Joe Doe", "000-00-002")
# joe.enroll("CECS 174 SEC 01", "Spring 2022")
# joe.enroll("CECS 274 SEC 02", "Fall 2022")
# joe.enroll("MATH 247 SEC 01", "Fall 2022")

# joe.record_grade("CECS 174 SEC 01", "A")
# joe.record_grade("CECS 274 SEC 02", "B")
# joe.record_grade("MATH 247 SEC 01", "C")


# jane.print_record()
# joe.print_record()

# print('-'*40)
# print(jane)
# print('-'*40)
# print(joe)


# In[ ]:




