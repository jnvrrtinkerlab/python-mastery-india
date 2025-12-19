"""
PHASE 2: CONTROL FLOW - Lesson 4
While Loops - Repeating Code Until a Condition is False

Objective:
- Understand while loop syntax and how it works
- Learn when to use while loops vs for loops
- Master loop control with break and continue
- Recognize and prevent infinite loops
- Apply while loops to real-world problems

Indian Context:
We'll use real Indian scenarios like bank PIN attempts, shopping,
school exams, and cricket scoring to make learning relatable!
"""

import time

print("\n" + "="*60)
print("PHASE 2: CONTROL FLOW - LESSON 4")
print("While Loops - Learn by Doing!")
print("="*60)

# ============================================================
# PART 1: BASIC WHILE LOOP SYNTAX
# ============================================================

print("\n" + "-"*60)
print("PART 1: BASIC WHILE LOOP SYNTAX")
print("-"*60)

print("\nExample 1: Simple counting loop")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count = count + 1

print("\nExample 2: Countdown")
num = 5
while num > 0:
    print(f"Time remaining: {num} seconds")
    num -= 1
print("Time's up!")

print("\nExample 3: Greeting until condition is met")
greeting = "Hello"
while len(greeting) < 20:
    greeting = greeting + " World"
    print(f"Greeting: {greeting}")


# ============================================================
# PART 2: REAL-WORLD INDIAN EXAMPLES
# ============================================================

print("\n" + "-"*60)
print("PART 2: REAL-WORLD INDIAN EXAMPLES")
print("-"*60)

# Example 1: Bank PIN Attempts (Maximum 3 attempts)
print("\nExample 1: Bank PIN Verification")
print("Scenario: Customer has 3 attempts to enter correct PIN")

correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input(f"\nEnter PIN (Attempt {attempts + 1}/3): ")
    attempts += 1
    
    if pin == correct_pin:
        print("✓ PIN Correct! Access Granted!")
        break
    elif attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"✗ Wrong PIN! {remaining} attempts remaining.")
    else:
        print("✗ Account Locked! Too many wrong attempts.")


# Example 2: School Exam Score Accumulation
print("\n" + "-"*30)
print("\nExample 2: Total Exam Scores (Indian Schools)")
print("Scenario: Calculate total from multiple subjects")

total_marks = 0
subjects = ["Hindi", "English", "Mathematics", "Science", "Social Studies"]
subject_index = 0

while subject_index < len(subjects):
    marks = int(input(f"Enter marks for {subjects[subject_index]} (out of 100): "))
    total_marks += marks
    subject_index += 1

average = total_marks / len(subjects)
print(f"\nTotal Marks: {total_marks}")
print(f"Average: {average:.2f}")
print(f"Percentage: {(average)}%")


# Example 3: Shopping Cart Loop (Indian Store)
print("\n" + "-"*30)
print("\nExample 3: Shopping Cart Accumulation")
print("Scenario: Add items to cart until customer is done")

cart_total = 0
item_count = 0

while True:
    item_name = input(f"\nEnter item name (or 'done' to finish): ")
    
    if item_name.lower() == 'done':
        break
    
    price = float(input(f"Enter price of {item_name} (Rs.): "))
    cart_total += price
    item_count += 1
    print(f"Added {item_name} - Rs. {price}")
    print(f"Cart Total: Rs. {cart_total}")

print(f"\n=== Final Bill ===")
print(f"Items: {item_count}")
print(f"Total: Rs. {cart_total}")

if cart_total > 1000:
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print(f"Discount (10%): Rs. {discount}")
    print(f"Final Total: Rs. {final_total}")


# ============================================================
# PART 3: BREAK AND CONTINUE STATEMENTS
# ============================================================

print("\n" + "-"*60)
print("PART 3: BREAK AND CONTINUE STATEMENTS")
print("-"*60)

# Example 1: Break - Exit loop early
print("\nExample 1: Using BREAK to exit loop")
print("Scenario: Find first number divisible by 7 between 1-50")

num = 1
while num <= 50:
    if num % 7 == 0:
        print(f"Found! {num} is divisible by 7")
        break
    num += 1
print(f"Loop ended at number {num}")


# Example 2: Continue - Skip current iteration
print("\nExample 2: Using CONTINUE to skip")
print("Scenario: Print odd numbers from 1-10")

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:  # Even number
        continue  # Skip to next iteration
    print(f"Odd number: {num}")


# Example 3: Practical - Cricket Batting Example
print("\nExample 3: Cricket - Get Out Detection")
print("Scenario: Batsman plays shots, stops if gets out")

runs = 0
balls_faced = 0
max_wickets_risk = 5

while balls_faced < 10:
    balls_faced += 1
    
    # Simulate a risky shot every 5 balls
    if balls_faced % max_wickets_risk == 0:
        print(f"Ball {balls_faced}: RISKY SHOT! Got OUT!")
        print(f"Final Score: {runs} runs from {balls_faced} balls")
        break
    
    # Alternate between scoring and dot balls
    if balls_faced % 2 == 0:
        runs += 4
        print(f"Ball {balls_faced}: Boundary! (+4 runs)")
    else:
        print(f"Ball {balls_faced}: Dot ball (no run)")

print(f"\nTotal Runs: {runs} runs from {balls_faced} balls")


# ============================================================
# PART 4: WHILE LOOPS WITH LISTS AND DICTIONARIES
# ============================================================

print("\n" + "-"*60)
print("PART 4: WHILE LOOPS WITH LISTS AND DICTIONARIES")
print("-"*60)

# Example 1: Process list with while loop
print("\nExample 1: Remove items from list")
school_tasks = ["Attend classes", "Do homework", "Play sports", "Eat lunch", "Sleep"]

while school_tasks:
    task = school_tasks.pop(0)  # Remove first task
    print(f"Completing: {task}")
print("All tasks done!")


# Example 2: Validate user input with while loop
print("\nExample 2: Validate Age Input")
print("Scenario: Keep asking until valid age is entered")

while True:
    try:
        age = int(input("\nEnter your age: "))
        if age < 0:
            print("Age cannot be negative!")
            continue
        elif age < 5:
            print("You must be at least 5 years old for school.")
        elif age > 100:
            print("Are you sure? That's quite old!")
            break
        else:
            print(f"Age {age} is valid!")
            break
    except ValueError:
        print("Please enter a valid number!")


# ============================================================
# PART 5: PREVENTING INFINITE LOOPS
# ============================================================

print("\n" + "-"*60)
print("PART 5: PREVENTING INFINITE LOOPS")
print("-"*60)

print("""
\nWARNING: Infinite Loop Examples (commented out)
Never run these!

# BAD - Infinite Loop (never increments counter)
# while True:
#     print("This will never stop!")

# BAD - Condition always true
# x = 5
# while x > 0:
#     print(x)
#     # forgot to change x!

\nBEST PRACTICES:
1. Always update the loop variable
2. Use clear loop conditions
3. Include break statements for early exit
4. Test loops with print statements
5. Use timeout mechanisms if needed
""")


# ============================================================
# EXERCISES
# ============================================================

print("\n" + "-"*60)
print("EXERCISES FOR YOU TO TRY")
print("-"*60)

print("""
EXERCISE 1: School Attendance
Write a program that:
- Asks student if they attended each day of the week
- Counts total days attended
- Calculates attendance percentage
- Shows if attendance is good (>=75%)

EXERCISE 2: Exam Preparation
Write a program that:
- Asks student "Ready for exam?" repeatedly
- If 'yes': Shows "Good luck!"
- If 'no': Shows "Keep studying!" and asks again
- Tracks how many study rounds they did

EXERCISE 3: Shopping Till Amount
Write a program that:
- Keeps asking for item prices
- Stops when total reaches Rs. 1000
- Shows how many items they bought
- Calculates average item price

EXERCISE 4: Number Guessing Game
Write a program that:
- Player guesses a number between 1-100
- Give hints (too high/too low)
- Count attempts
- Show if they won
""")

print("\n" + "="*60)
print("Happy Learning! While loops are powerful! 🚀")
print("="*60)
