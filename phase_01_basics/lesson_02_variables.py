#!/usr/bin/env python3
"""
Lesson 02: Variables - Storing Information

Objective: Learn how to create and use variables to store data.
"""

# Variables are containers that store values
print("=" * 60)
print("LESSON 02: VARIABLES - STORING INFORMATION")
print("=" * 60)
print()

# Creating Variables (Indian Context)
student_name = "Lahari"  # String variable
student_age = 15         # Integer variable
height = 5.6             # Float variable
is_present = True        # Boolean variable

print("Student Details:")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Height: {height} feet")
print(f"Present: {is_present}")
print()

# Variables can be reassigned
student_name = "Karthik"
student_age = 16
print(f"Updated: {student_name} is now {student_age} years old")
print()

# Multiple variable assignment
marks_math, marks_english, marks_science = 95, 88, 92
print(f"Marks - Math: {marks_math}, English: {marks_english}, Science: {marks_science}")
print()

# Calculating average
average_marks = (marks_math + marks_english + marks_science) / 3
print(f"Average Marks: {average_marks:.2f}")
print()

print("🔥 YOU'VE MASTERED VARIABLES!")
print()

print("=" * 60)
print("CHALLENGES:")
print("=" * 60)
print("1. Create variables for your school name and city")
print("2. Create a variable for your favorite subject")
print("3. Create a variable for your birthday year")
print("4. Calculate how many years you've been in school")
print()
