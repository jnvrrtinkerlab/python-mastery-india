"""
Lesson 14: Sets & Unordered Collections
========================================
Sets are unordered collections of unique elements. They are useful for
removing duplicates, performing set operations (union, intersection, etc.),
and testing membership.

Key Concepts:
- Creating sets
- Set operations (add, remove, pop)
- Mathematical set operations
- Set comprehensions
- Frozensets (immutable sets)
- Real-world applications
"""

# ===== 1. CREATING SETS =====
# Sets use curly braces {} with unique elements

# Empty set (note: {} is a dictionary, use set())
empty_set = set()
print("Empty set:", empty_set)
print("Type:", type(empty_set))

# Set with elements
fruits = {"Apple", "Mango", "Banana", "Orange"}
print("\nFruits set:", fruits)
print("Type:", type(fruits))

# Set removes duplicates automatically
numbers_with_dupes = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print("\nNumbers (duplicates removed):", numbers_with_dupes)

# Mixed types in sets
mixed_set = {1, "Hello", 3.14, True}
print("Mixed set:", mixed_set)

# Creating sets from other sequences
from_list = set([1, 2, 3, 4, 5])
print("\nFrom list:", from_list)

from_string = set("Python")
print("From string:", from_string)

from_range = set(range(1, 6))
print("From range:", from_range)

# Indian context: Cricket players
indian_players = {"Rohit", "Kohli", "Bumrah", "Dhoni", "Pant"}
print("\nIndian cricket players:", indian_players)

# Indian context: States
india_states = {"Maharashtra", "Tamil Nadu", "Delhi", "Punjab", "Kerala"}
print("Indian states:", india_states)


# ===== 2. SET OPERATIONS =====
print("\n--- Set Operations ---")

# Adding elements
colors = {"Red", "Green", "Blue"}
print(f"Original: {colors}")
colors.add("Yellow")
print(f"After add: {colors}")

# add() doesn't add if element exists
colors.add("Red")  # No change
print(f"After adding Red again: {colors}")

# Adding multiple elements
colors.update(["Orange", "Purple", "Pink"])
print(f"After update: {colors}")

# Removing elements
colors.remove("Purple")  # Raises error if not found
print(f"After remove: {colors}")

# Discard (doesn't raise error)
colors.discard("Pink")  # Safe removal
colors.discard("Brown")  # No error even if not found
print(f"After discard: {colors}")

# Pop (removes and returns arbitrary element)
removed = colors.pop()
print(f"Popped: {removed}, Set now: {colors}")

# Clear all elements
test_set = {1, 2, 3}
test_set.clear()
print(f"After clear: {test_set}")

# Indian context: Shopping items
shop_items = {"Rice", "Dal", "Oil", "Salt", "Spices"}
print("\nShop items:", shop_items)
shop_items.add("Turmeric")  # Add new spice
print("After adding Turmeric:", shop_items)
shop_items.remove("Salt")
print("After removing Salt:", shop_items)


# ===== 3. MATHEMATICAL SET OPERATIONS =====
print("\n--- Mathematical Set Operations ---")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all elements from both sets)
union_set = set_a | set_b  # or set_a.union(set_b)
print(f"\nUnion (A | B): {union_set}")

# Intersection (common elements)
intersection_set = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection_set}")

# Difference (elements in A but not in B)
difference_set = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {difference_set}")

# Symmetric difference (elements in either but not both)
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric Difference (A ^ B): {sym_diff}")

# Subset and superset
subset = {1, 2}
print(f"\n{subset} is subset of {set_a}: {subset.issubset(set_a)}")
print(f"{set_a} is superset of {subset}: {set_a.issuperset(subset)}")

# Disjoint (no common elements)
set_x = {1, 2}
set_y = {3, 4}
print(f"\n{set_x} and {set_y} are disjoint: {set_x.isdisjoint(set_y)}")
print(f"{set_a} and {set_b} are disjoint: {set_a.isdisjoint(set_b)}")

# Indian context: Cricket teams
team_india = {"Rohit", "Kohli", "Bumrah", "Dhoni", "Pant"}
team_pakistan = {"Babar", "Bumrah", "Afridi", "Hassan", "Shehzad"}

common_players = team_india & team_pakistan
print(f"\nCommon players: {common_players}")

all_players = team_india | team_pakistan
print(f"All players: {all_players}")

india_only = team_india - team_pakistan
print(f"Only in India team: {india_only}")


# ===== 4. SET METHODS & PROPERTIES =====
print("\n--- Set Methods & Properties ---")

nums = {1, 2, 3, 4, 5, 1, 2}  # Automatically removes duplicates
print(f"Set: {nums}")

# Length
print(f"Length: {len(nums)}")

# Membership
print(f"3 in nums: {3 in nums}")
print(f"10 in nums: {10 in nums}")

# Copy
original = {"a", "b", "c"}
copy_set = original.copy()
copy_set.add("d")
print(f"\nOriginal: {original}")
print(f"Copy: {copy_set}")

# Min and Max
scores_set = {45, 78, 92, 88, 76}
print(f"\nScores: {scores_set}")
print(f"Min: {min(scores_set)}")
print(f"Max: {max(scores_set)}")
print(f"Sum: {sum(scores_set)}")


# ===== 5. SET COMPREHENSIONS =====
print("\n--- Set Comprehensions ---")

# Creating sets from lists
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
squares = {x**2 for x in numbers}
print(f"Squares: {squares}")

# Set comprehension with condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even number squares: {even_squares}")

# From string
letters = {letter for letter in "Mississippi"}
print(f"Unique letters in Mississippi: {letters}")

# Indian context: Unique states
states_list = ["Maharashtra", "Delhi", "Maharashtra", "Tamil Nadu", "Delhi", "Punjab"]
unique_states = {state for state in states_list}
print(f"\nUnique states: {unique_states}")


# ===== 6. FROZENSETS =====
print("\n--- Frozensets (Immutable Sets) ---")

# Frozensets are immutable (can be used as dictionary keys)
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozen}")
print(f"Type: {type(frozen)}")

# Can be used as dictionary keys
set_counts = {}
set_counts[frozenset({1, 2})] = "set one-two"
set_counts[frozenset({3, 4})] = "set three-four"

for key, value in set_counts.items():
    print(f"{key}: {value}")

# Operations work on frozensets too
frozen_a = frozenset({1, 2, 3})
frozen_b = frozenset({2, 3, 4})
print(f"\nUnion: {frozen_a | frozen_b}")
print(f"Intersection: {frozen_a & frozen_b}")


# ===== 7. PRACTICAL EXAMPLES =====
print("\n--- Practical Examples ---")

# Remove duplicates from list
data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
unique_data = list(set(data))
print(f"Original: {data}")
print(f"Unique: {unique_data}")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print(f"\nList 1: {list1}")
print(f"List 2: {list2}")
print(f"Common: {list(common)}")

# Anagram check
word1 = "listen"
word2 = "silent"
print(f"\n'{word1}' and '{word2}' are anagrams: {set(word1) == set(word2)}")


# ===== 8. EXERCISES =====
print("\n" + "="*50)
print("EXERCISES")
print("="*50)

print("""
Exercise 1: Create a set of fruits and add/remove elements.
""")
fruits_set = {"Apple", "Mango", "Banana"}
print(f"Original: {fruits_set}")
fruits_set.add("Orange")
fruits_set.add("Guava")
print(f"After adding: {fruits_set}")
fruits_set.remove("Banana")
print(f"After removing Banana: {fruits_set}")

print("\nExercise 2: Find union and intersection of two sets.")
set_x = {1, 2, 3, 4, 5}
set_y = {3, 4, 5, 6, 7}
print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Union: {set_x | set_y}")
print(f"Intersection: {set_x & set_y}")

print("\nExercise 3: Remove duplicates from a list using sets.")
original_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Original list: {original_list}")
no_duplicates = list(set(original_list))
print(f"Without duplicates: {no_duplicates}")

print("\nExercise 4: Create a set from a string and count unique letters.")
text = "Programming"
unique_letters = set(text.lower())
print(f"Text: {text}")
print(f"Unique letters: {unique_letters}")
print(f"Count of unique letters: {len(unique_letters)}")

print("\n" + "="*50)
print("End of Lesson 14")
print("="*50)
