# ===============================
# VARIABLES & DATA TYPES
# ===============================

print("\n--- VARIABLES & DATA TYPES ---")

name = "Mishika"
age = 21
marks = 92.5

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# ===============================
# LIST
# ===============================

print("\n--- LIST ---")

students = ["Rahul", "Aman", "Mishika"]

print("Student List:", students)

for s in students:
    print("Student:", s)


# ===============================
# TUPLE
# ===============================

print("\n--- TUPLE ---")

subjects = ("Math", "Physics", "CS")

print("Subjects:", subjects)
print("First subject:", subjects[0])


# ===============================
# SET
# ===============================

print("\n--- SET ---")

numbers = {1,2,3,3,2}

print("Unique numbers:", numbers)


# ===============================
# DICTIONARY
# ===============================

print("\n--- DICTIONARY ---")

student = {
    "name": "Mishika",
    "marks": 92,
    "city": "Indore"
}

print("Student Dictionary:", student)
print("Student name:", student["name"])


# ===============================
# STRING MANIPULATION
# ===============================

print("\n--- STRING MANIPULATION ---")

text = "Python Programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))


# ===============================
# CONDITIONAL STATEMENT
# ===============================

print("\n--- CONDITIONAL STATEMENT ---")

marks = 85

if marks >= 80:
    print("Grade A")
else:
    print("Grade B")


# ===============================
# LOOPS
# ===============================

print("\n--- FOR LOOP ---")

for i in range(3):
    print("Number:", i)


print("\n--- WHILE LOOP ---")

i = 1
while i <= 3:
    print("Count:", i)
    i += 1


# ===============================
# FUNCTION
# ===============================

print("\n--- FUNCTION ---")

def greet(name):
    print("Hello", name)

greet("Mishika")


# ===============================
# FILE HANDLING
# ===============================

print("\n--- FILE HANDLING ---")

with open("sample.txt","w") as file:
    file.write("Hello Mishika")

print("File created and text written.")


# ===============================
# EXCEPTION HANDLING
# ===============================

print("\n--- EXCEPTION HANDLING ---")

try:
    x = 10/0
except:
    print("Error: Cannot divide by zero")


# ===============================
# OBJECT ORIENTED PROGRAMMING
# ===============================

print("\n--- OBJECT ORIENTED PROGRAMMING ---")

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Mishika",92)
s1.display()


# ===============================
# NUMPY
# ===============================

print("\n--- NUMPY ARRAY ---")

import numpy as np

arr = np.array([80,75,92,65])

print("Array:", arr)
print("Mean:", np.mean(arr))


# ===============================
# MATRIX
# ===============================

print("\n--- MATRIX ---")

matrix = np.array([
[80,75],
[92,65]
])

print(matrix)


# ===============================
# PANDAS DATAFRAME
# ===============================

print("\n--- PANDAS DATAFRAME ---")

import pandas as pd

data = {
"Name": ["Rahul","Aman","Mishika","Riya"],
"Marks": [80,75,92,65]
}

df = pd.DataFrame(data)

print(df)


# ===============================
# DATA FILTERING
# ===============================

print("\n--- DATA FILTERING ---")

high_marks = df[df["Marks"] > 80]

print(high_marks)


# ===============================
# DATA VISUALIZATION
# ===============================

print("\n--- DATA VISUALIZATION (MATPLOTLIB) ---")

import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.show()


# ===============================
# STATISTICS
# ===============================

print("\n--- STATISTICS ---")

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))


# ===============================
# PROBABILITY
# ===============================

print("\n--- PROBABILITY ---")

total_students = len(arr)
high = len(arr[arr > 80])

probability = high/total_students

print("Probability of marks > 80:", probability)


# ===============================
# GRADIENT DESCENT CONCEPT
# ===============================

print("\n--- GRADIENT DESCENT ---")

learning_rate = 0.1
weight = 5
gradient = 2

weight = weight - learning_rate * gradient

print("Updated weight:", weight)