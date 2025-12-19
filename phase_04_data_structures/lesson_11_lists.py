"""
Lesson 11: Lists & List Operations
===================================
Lists are one of Python's most versatile and commonly used data structures.
They allow you to store multiple items in a single variable and perform
various operations on them.

Key Concepts:
- Creating lists
- Accessing list elements
- Modifying lists
- List methods
- Iterating over lists
- List comprehensions
"""

# ===== 1. CREATING LISTS =====
# Lists are created using square brackets []

# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with integers
numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

# List with strings
fruits = ["Apple", "Mango", "Banana", "Orange"]
print("Fruits:", fruits)

# List with mixed data types
mixed_list = [1, "Hello", 3.14, True, None]
print("Mixed list:", mixed_list)

# Using list() constructor
list_from_string = list("Python")
print("List from string:", list_from_string)

list_from_range = list(range(1, 6))
print("List from range:", list_from_range)

# Indian context example: School subjects
school_subjects = ["Mathematics", "Science", "Hindi", "English", "Social Studies"]
print("\nSchool subjects in India:", school_subjects)

# Indian context: Cricket team members
indian_cricketers = ["Rohit", "Kohli", "Bumrah", "Dhoni", "Pant"]
print("Indian cricketers:", indian_cricketers)


# ===== 2. ACCESSING LIST ELEMENTS =====
# Lists use zero-based indexing

students = ["Raj", "Priya", "Arun", "Sneha", "Vikram"]
print("\n--- Accessing Elements ---")
print("First student:", students[0])  # Positive indexing
print("Second student:", students[1])
print("Last student:", students[-1])  # Negative indexing
print("Second-last student:", students[-2])

# Slicing lists
print("\nSlicing:")
print("First three students:", students[0:3])
print("From index 2 to end:", students[2:])
print("From beginning to index 4:", students[:4])
print("Every second student:", students[::2])
print("Reversed list:", students[::-1])

# Indian context: City temperatures
city_temps = [35, 38, 32, 28, 30, 36, 34]
print("\nTemperatures in Delhi for a week:", city_temps)
print("Monday's temperature:", city_temps[0])
print("Last 3 days' temperatures:", city_temps[-3:])


# ===== 3. MODIFYING LISTS =====
print("\n--- Modifying Lists ---")

# Changing elements
colors = ["Red", "Green", "Blue"]
print("Original colors:", colors)
colors[1] = "Yellow"
print("After changing:", colors)

# Adding elements
colors.append("Purple")
print("After append:", colors)

colors.insert(0, "Orange")  # Insert at specific position
print("After insert at 0:", colors)

# Adding multiple elements
colors.extend(["Pink", "Brown"])
print("After extend:", colors)

# Removing elements
colors.remove("Brown")  # Remove by value
print("After removing Brown:", colors)

removed_item = colors.pop()  # Remove last item
print(f"Popped item: {removed_item}, List now: {colors}")

removed_at_index = colors.pop(0)  # Remove at specific index
print(f"Popped at 0: {removed_at_index}, List now: {colors}")

# Clear all elements
test_list = [1, 2, 3, 4]
test_list.clear()
print("\nAfter clear:", test_list)

# Indian context: Shopping cart
shop_cart = ["Dal", "Rice", "Oil"]
print("\nInitial cart:", shop_cart)
shop_cart.append("Turmeric")  # Add spice
print("After adding Turmeric:", shop_cart)
shop_cart.remove("Oil")
print("After removing Oil:", shop_cart)


# ===== 4. LIST METHODS =====
print("\n--- List Methods ---")

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original list:", nums)

# Count occurrences
print("Count of 1:", nums.count(1))
print("Count of 5:", nums.count(5))

# Find index of element
print("Index of 4:", nums.index(4))
print("Index of first 1:", nums.index(1))

# Sorting
sorted_nums = sorted(nums)
print("Sorted copy:", sorted_nums)

nums.sort()  # In-place sorting
print("After sort():", nums)

# Reverse
nums.reverse()
print("After reverse():", nums)

# Copy
copy_nums = nums.copy()
print("Copied list:", copy_nums)

# Length
print("Length:", len(nums))

# Sum and statistics
scores = [45, 78, 92, 88, 76]
print("\nScores:", scores)
print("Total:", sum(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))
print("Average:", sum(scores) / len(scores))

# Indian context: Student marks
student_marks = [78, 85, 92, 88, 76, 95]
print("\nStudent marks in India:", student_marks)
print("Highest mark:", max(student_marks))
print("Lowest mark:", min(student_marks))
print("Total marks:", sum(student_marks))
print("Percentage average:", (sum(student_marks) / (len(student_marks) * 100)) * 100)


# ===== 5. ITERATING OVER LISTS =====
print("\n--- Iterating Over Lists ---")

vegetables = ["Potato", "Tomato", "Onion", "Carrot", "Cabbage"]

# Using for loop
print("\nUsing for loop:")
for veg in vegetables:
    print(f"- {veg}")

# Using enumerate
print("\nUsing enumerate:")
for index, veg in enumerate(vegetables):
    print(f"{index + 1}. {veg}")

# Using range and len
print("\nUsing range and len:")
for i in range(len(vegetables)):
    print(f"Position {i}: {vegetables[i]}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print("\nSquares using list comprehension:", squares)

# Filtering with list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers 1-10:", even_numbers)

# Indian context: Multiplication table
print("\nIndian context - 7's multiplication table using list comprehension:")
table_of_7 = [7 * i for i in range(1, 11)]
print("7's table:", table_of_7)


# ===== 6. EXERCISES =====
print("\n" + "="*50)
print("EXERCISES")
print("="*50)

print("""
Exercise 1: Create a list of 5 Indian states and print each state.
States: Maharashtra, Tamil Nadu, Punjab, Kerala, Gujarat
""")

states = ["Maharashtra", "Tamil Nadu", "Punjab", "Kerala", "Gujarat"]
for state in states:
    print(f"- {state}")

print("\nExercise 2: Create a list of numbers from 1 to 10 and find sum and average.")
numbers = list(range(1, 11))
print(f"Numbers: {numbers}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

print("\nExercise 3: Create a list of fruits and replace the first fruit with 'Papaya'.")
fruits_list = ["Apple", "Banana", "Mango", "Grapes"]
print(f"Original: {fruits_list}")
fruits_list[0] = "Papaya"
print(f"Modified: {fruits_list}")

print("\nExercise 4: Create a list of numbers and remove all even numbers (advanced).")
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {original}")
odds_only = [x for x in original if x % 2 != 0]
print(f"Only odd numbers: {odds_only}")

print("\n" + "="*50)
print("End of Lesson 11")
print("="*50)
