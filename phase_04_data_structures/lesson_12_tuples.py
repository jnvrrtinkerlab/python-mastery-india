"""
Lesson 12: Tuples & Immutable Sequences
========================================
Tuples are immutable sequences in Python. Once created, they cannot be changed.
They are useful for protecting data from accidental modification and can be
used as dictionary keys (unlike lists).

Key Concepts:
- Creating tuples
- Accessing tuple elements
- Tuple unpacking
- Tuple methods
- Immutability and its benefits
- Tuples vs Lists
"""

# ===== 1. CREATING TUPLES =====
# Tuples are created using parentheses () or just commas

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)
print("Type:", type(empty_tuple))

# Single element tuple (note the comma)
single_tuple = (42,)
print("\nSingle element tuple:", single_tuple)
print("Type:", type(single_tuple))

# Multiple elements
number_tuple = (10, 20, 30, 40, 50)
print("\nNumber tuple:", number_tuple)

# Mixed types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Without parentheses (implicit tuple)
implicit_tuple = 5, "World", 2.71
print("\nImplicit tuple:", implicit_tuple)

# Tuple from other sequences
from_list = tuple([1, 2, 3, 4, 5])
print("From list:", from_list)

from_string = tuple("Python")
print("From string:", from_string)

from_range = tuple(range(1, 6))
print("From range:", from_range)

# Indian context: Coordinates
city_coordinates = ("New Delhi", 28.7041, 77.1025)
print("\nDelhi coordinates (name, latitude, longitude):", city_coordinates)

# Indian context: Cricket match details
match_info = ("India", "Pakistan", "Asia Cup", 2023)
print("Match info:", match_info)


# ===== 2. ACCESSING TUPLE ELEMENTS =====
print("\n--- Accessing Elements ---")

fruits = ("Apple", "Mango", "Banana", "Orange", "Guava")
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Second-last fruit:", fruits[-2])

# Slicing
print("\nSlicing:")
print("First three:", fruits[0:3])
print("From index 2 onwards:", fruits[2:])
print("Reversed:", fruits[::-1])
print("Every second:", fruits[::2])

# Indian context: Month names
months = ("January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December")
print("\nMonths in a year:")
print(f"First month: {months[0]}")
print(f"Last month: {months[-1]}")
print(f"Months in Q1: {months[0:3]}")


# ===== 3. TUPLE UNPACKING =====
print("\n--- Tuple Unpacking ---")

# Basic unpacking
coordinates = (40.7128, -74.0060)  # New York coordinates
latitude, longitude = coordinates
print(f"Latitude: {latitude}, Longitude: {longitude}")

# Multiple unpacking
rgb = (255, 128, 0)
red, green, blue = rgb
print(f"\nColor - Red: {red}, Green: {green}, Blue: {blue}")

# Unpacking with multiple variables
person = ("Raj", 25, "Engineer", "Mumbai")
name, age, profession, city = person
print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
print(f"City: {city}")

# Using underscore for ignored values
data = (1, 2, 3, 4, 5)
first, _, third, *rest = data
print(f"\nFirst: {first}, Third: {third}, Rest: {rest}")

# Indian context: Student details
student = ("Priya", "Grade 12", "Science", 95.5, "Delhi")
student_name, grade, stream, score, location = student
print(f"\nStudent: {student_name}")
print(f"Grade: {grade}")
print(f"Stream: {stream}")
print(f"Score: {score}%")
print(f"Location: {location}")


# ===== 4. TUPLE OPERATIONS =====
print("\n--- Tuple Operations ---")

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# Repetition
repeat_tuple = ("Hi",) * 3
print(f"Repetition: ('Hi',) * 3 = {repeat_tuple}")

# Membership
colors = ("Red", "Green", "Blue", "Yellow")
print(f"\n'Red' in colors: {'Red' in colors}")
print(f"'Pink' in colors: {'Pink' in colors}")

# Length
print(f"Length of colors: {len(colors)}")

# Count
numbers = (1, 2, 2, 3, 2, 4, 5, 2)
print(f"\nNumbers: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Count of 4: {numbers.count(4)}")

# Index
print(f"Index of 3: {numbers.index(3)}")
print(f"Index of first 2: {numbers.index(2)}")

# Min, Max, Sum
scores = (78, 92, 85, 88, 95)
print(f"\nScores: {scores}")
print(f"Min: {min(scores)}")
print(f"Max: {max(scores)}")
print(f"Sum: {sum(scores)}")

# Indian context: Cricket scores
cricketer_scores = (45, 78, 92, 38, 156, 67, 89)
print(f"\nCricketer scores: {cricketer_scores}")
print(f"Highest score: {max(cricketer_scores)}")
print(f"Average: {sum(cricketer_scores) / len(cricketer_scores):.2f}")


# ===== 5. IMMUTABILITY AND BENEFITS =====
print("\n--- Immutability ---")

# Tuples cannot be modified
original = (1, 2, 3)
print(f"Original tuple: {original}")

# This would cause an error (commented out):
# original[0] = 10  # TypeError: 'tuple' object does not support item assignment

# To modify, create a new tuple
modified = original + (4, 5)
print(f"Modified (new tuple): {modified}")
print(f"Original unchanged: {original}")

# Tuples can be used as dictionary keys (lists cannot)
print("\nUsing tuples as dictionary keys:")
location_temps = {}
location_temps[("Delhi", 2023)] = 45.5
location_temps[("Mumbai", 2023)] = 42.1
location_temps[("Bangalore", 2023)] = 38.2

for location, temp in location_temps.items():
    print(f"{location[0]} ({location[1]}): {temp}°C")


# ===== 6. TUPLES VS LISTS =====
print("\n--- Tuples vs Lists ---")

# Performance
import time

# Create list
test_list = list(range(1000000))
start = time.time()
for _ in range(100):
    x = test_list[500000]
list_time = time.time() - start

# Create tuple
test_tuple = tuple(range(1000000))
start = time.time()
for _ in range(100):
    x = test_tuple[500000]
tuple_time = time.time() - start

print(f"List access (100 iterations): {list_time:.6f} seconds")
print(f"Tuple access (100 iterations): {tuple_time:.6f} seconds")

# Tuples are immutable and hashable
print("\nHashability:")
tuple_set = {(1, 2), (3, 4), (1, 2)}  # Set removes duplicates
print(f"Set of tuples: {tuple_set}")
# list_set = {[1, 2], [3, 4]}  # This would error


# ===== 7. EXERCISES =====
print("\n" + "="*50)
print("EXERCISES")
print("="*50)

print("""
Exercise 1: Create a tuple of 5 Indian states and print them.
Then find the length and access the 3rd element.
""")

states_tuple = ("Maharashtra", "Tamil Nadu", "Punjab", "Kerala", "Gujarat")
print(f"States: {states_tuple}")
print(f"Length: {len(states_tuple)}")
print(f"3rd state: {states_tuple[2]}")

print("\nExercise 2: Unpack a tuple of person details.")
person_details = ("Arun", 28, "Software Engineer")
name, age, job = person_details
print(f"Name: {name}, Age: {age}, Job: {job}")

print("\nExercise 3: Create a tuple from a string and count vowels.")
word = "Python"
word_tuple = tuple(word)
print(f"Word: {word}")
print(f"As tuple: {word_tuple}")
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_count = sum(1 for letter in word_tuple if letter.lower() in vowels)
print(f"Vowels found: {vowel_count}")

print("\nExercise 4: Use tuples as dictionary keys for city data.")
city_data = {}
city_data[("Delhi", "2023", "Temperature")] = 45
city_data[("Mumbai", "2023", "Humidity")] = 75
for key, value in city_data.items():
    print(f"{key}: {value}")

print("\n" + "="*50)
print("End of Lesson 12")
print("="*50)
