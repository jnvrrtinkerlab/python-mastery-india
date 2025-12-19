"""
Lesson 13: Dictionaries & Key-Value Mappings
=============================================
Dictionaries are unordered collections of key-value pairs. They provide
an efficient way to store and retrieve data using meaningful keys instead
of numeric indices.

Key Concepts:
- Creating dictionaries
- Accessing and modifying dictionary values
- Dictionary methods
- Nested dictionaries
- Dictionary comprehensions
- Real-world applications
"""

# ===== 1. CREATING DICTIONARIES =====
# Dictionaries use curly braces {} with key:value pairs

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)
print("Type:", type(empty_dict))

# Dictionary with string keys
person = {
    "name": "Raj",
    "age": 25,
    "city": "Mumbai",
    "profession": "Engineer"
}
print("\nPerson dictionary:", person)

# Dictionary with mixed key types
mixed_dict = {
    "string_key": "value",
    42: "numeric key",
    3.14: "float key",
    (1, 2): "tuple key"  # Tuples can be keys
}
print("Mixed keys dict:", mixed_dict)

# Using dict() constructor
constructor_dict = dict(name="Priya", age=23, city="Delhi")
print("\nUsing dict():", constructor_dict)

# Indian context: School student record
student_record = {
    "roll_no": 101,
    "name": "Arun",
    "class": "12th",
    "stream": "Science",
    "school": "Delhi Public School",
    "gpa": 3.8
}
print("\nStudent record:", student_record)

# Indian context: Cricket player stats
player_stats = {
    "name": "Virat Kohli",
    "matches": 250,
    "runs": 12000,
    "average": 48.0,
    "centuries": 45,
    "country": "India"
}
print("Player stats:", player_stats)


# ===== 2. ACCESSING & MODIFYING DICTIONARIES =====
print("\n--- Accessing & Modifying ---")

book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2020,
    "pages": 350,
    "price": 299.99
}

print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f"Price: {book['price']}")

# Using get() method (safer)
print(f"\nUsing get():")
print(f"Year: {book.get('year')}")
print(f"ISBN (doesn't exist): {book.get('isbn')}")
print(f"ISBN with default: {book.get('isbn', 'Not available')}")

# Modifying values
book['price'] = 349.99  # Update
print(f"\nUpdated price: {book['price']}")

# Adding new key-value pairs
book['isbn'] = "978-0123456789"
print(f"Added ISBN: {book['isbn']}")

# Updating multiple values
book.update({"edition": 2, "language": "English"})
print(f"After update: {book}")

# Removing key-value pairs
del book['pages']
print(f"\nAfter deleting pages: {book}")

removed_value = book.pop('price')
print(f"Popped price: {removed_value}")
print(f"Dictionary now: {book}")

# Indian context: Product inventory
product = {
    "name": "Masala Chai",
    "category": "Beverage",
    "price": 50,
    "quantity": 100,
    "supplier": "Local Vendor"
}
print("\nProduct before: ", product)
product['price'] = 55  # Price update
product['quantity'] = 85  # Sold some
print("Product after update:", product)


# ===== 3. DICTIONARY METHODS =====
print("\n--- Dictionary Methods ---")

scores = {
    "Raj": 95,
    "Priya": 92,
    "Arun": 88,
    "Sneha": 96,
    "Vikram": 85
}

print(f"Scores: {scores}")

# keys(), values(), items()
print(f"\nKeys: {list(scores.keys())}")
print(f"Values: {list(scores.values())}")
print(f"Items: {list(scores.items())}")

# Iterating
print("\nIterating over keys:")
for name in scores.keys():
    print(f"  {name}")

print("\nIterating over items:")
for name, score in scores.items():
    print(f"  {name}: {score}")

# length
print(f"\nNumber of students: {len(scores)}")

# Checking membership
print(f"'Raj' in scores: {'Raj' in scores}")
print(f"90 in scores.values(): {90 in scores.values()}")

# clear()
test_dict = {"a": 1, "b": 2}
test_dict.clear()
print(f"\nAfter clear: {test_dict}")

# copy()
original = {"x": 10, "y": 20}
copy_dict = original.copy()
copy_dict['x'] = 50
print(f"\nOriginal: {original}")
print(f"Copy after modification: {copy_dict}")

# setdefault()
movie = {"title": "3 Idiots", "director": "Rajkumar Hirani"}
movie.setdefault("year", 2009)
movie.setdefault("rating", 8.4)
print(f"\nMovie after setdefault: {movie}")


# ===== 4. NESTED DICTIONARIES =====
print("\n--- Nested Dictionaries ---")

# Dictionary containing other dictionaries
school = {
    "name": "Delhi Public School",
    "location": {
        "city": "Delhi",
        "state": "Delhi",
        "country": "India"
    },
    "students": {
        "class_10": 120,
        "class_11": 100,
        "class_12": 95
    },
    "established": 1989
}

print(f"School name: {school['name']}")
print(f"City: {school['location']['city']}")
print(f"Class 12 students: {school['students']['class_12']}")

# Modifying nested values
school['location']['state'] = "DL"
school['students']['class_10'] = 125
print(f"\nAfter modification:")
print(f"State: {school['location']['state']}")
print(f"Class 10 students: {school['students']['class_10']}")

# Indian context: Company structure
company = {
    "name": "TechCorp India",
    "departments": {
        "engineering": {
            "employees": 50,
            "manager": "Rajesh"
        },
        "sales": {
            "employees": 30,
            "manager": "Priya"
        },
        "hr": {
            "employees": 10,
            "manager": "Sneha"
        }
    },
    "revenue": "10 Crore"
}

print(f"\nCompany: {company['name']}")
print(f"Engineering employees: {company['departments']['engineering']['employees']}")
print(f"Sales manager: {company['departments']['sales']['manager']}")


# ===== 5. DICTIONARY COMPREHENSIONS =====
print("\n--- Dictionary Comprehensions ---")

# Creating dictionaries from lists
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(f"Squares: {squares}")

# Creating dictionaries with conditions
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Swapping keys and values
original_dict = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original_dict.items()}
print(f"\nOriginal: {original_dict}")
print(f"Swapped: {swapped}")

# Indian context: Creating marks from list
students_list = ["Raj", "Priya", "Arun"]
marks_dict = {student: (i+1)*80 for i, student in enumerate(students_list)}
print(f"\nStudents marks: {marks_dict}")


# ===== 6. PRACTICAL EXAMPLES =====
print("\n--- Practical Examples ---")

# Counting occurrences
fruits = ["apple", "banana", "apple", "mango", "banana", "apple"]
fruit_count = {}
for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
print(f"Fruit count: {fruit_count}")

# Using dict to store function results
temperature_converter = {
    "celsius_to_fahrenheit": lambda c: (c * 9/5) + 32,
    "fahrenheit_to_celsius": lambda f: (f - 32) * 5/9
}
temp_c = 25
temp_f = temperature_converter["celsius_to_fahrenheit"](temp_c)
print(f"\n{temp_c}°C = {temp_f:.2f}°F")


# ===== 7. EXERCISES =====
print("\n" + "="*50)
print("EXERCISES")
print("="*50)

print("""
Exercise 1: Create a dictionary for a book and access its values.
""")
my_book = {
    "title": "Learn Python",
    "author": "Guido van Rossum",
    "pages": 400,
    "price": 599
}
print(f"Book: {my_book['title']} by {my_book['author']}")
print(f"Pages: {my_book['pages']}, Price: Rs. {my_book['price']}")

print("\nExercise 2: Create a nested dictionary for student details.")
student = {
    "personal": {
        "name": "Arun",
        "age": 17,
        "city": "Bangalore"
    },
    "academic": {
        "class": "12",
        "stream": "Science",
        "gpa": 3.9
    }
}
print(f"Student: {student['personal']['name']}")
print(f"Class: {student['academic']['class']}, GPA: {student['academic']['gpa']}")

print("\nExercise 3: Count vowels in a word using dictionary.")
word = "Python"
vowel_dict = {}
for letter in word:
    vowel_dict[letter] = vowel_dict.get(letter, 0) + 1
print(f"Letter count in '{word}': {vowel_dict}")

print("\nExercise 4: Create a dictionary of Indian states and capitals.")
states_capitals = {
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Punjab": "Chandigarh",
    "Kerala": "Thiruvananthapuram",
    "Delhi": "New Delhi"
}
for state, capital in states_capitals.items():
    print(f"{state}: {capital}")

print("\n" + "="*50)
print("End of Lesson 13")
print("="*50)
