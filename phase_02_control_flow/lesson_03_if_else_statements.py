"""\nPHASE 2: CONTROL FLOW - Lesson 3\nIf/Else Statements - Making Decisions in Python\n
Objective:
- Understand conditional statements
- Learn if, elif, else syntax
- Make decisions in programs
- Write programs with multiple paths

Indian Context Example:
We'll use real-world Indian scenarios like exam grades, school admission,
festival eligibility to make learning relatable!
"""

# ============================================================
# PART 1: BASIC IF STATEMENT
# ============================================================

print("=" * 50)
print("PART 1: BASIC IF STATEMENT")
print("=" * 50)

# Example 1: Simple if statement
age = 18
if age >= 18:
    print(f"Your age is {age}. You are an adult!")
    print("You can vote in Indian elections!")

# Example 2: Another if statement
marks = 85
if marks >= 80:
    print(f"Your marks: {marks}")
    print("Excellent performance! You deserve a celebration!")

# Example 3: if statement that might not execute
temperature = 15
if temperature > 35:
    print(f"Temperature is {temperature}°C. It's too hot!")
    print("Stay hydrated and avoid going outside.")

print("\nProgram continued...\n")


# ============================================================
# PART 2: IF-ELSE STATEMENT
# ============================================================

print("=" * 50)
print("PART 2: IF-ELSE STATEMENT")
print("=" * 50)

# Example 1: Weather check
month = 7
if month >= 6 and month <= 9:
    print(f"Month {month} is Monsoon season in India!")
    print("Prepare for heavy rains and floods.")
else:
    print(f"Month {month} is not monsoon season.")
    print("Weather should be comparatively dry.")

# Example 2: Exam result
student_marks = 45
if student_marks >= 40:
    print(f"Marks: {student_marks}")
    print("PASS! You have passed the exam!")
else:
    print(f"Marks: {student_marks}")
    print("FAIL! Please try again in the supplementary exam.")

# Example 3: Festival eligibility
age_for_voting = 25
if age_for_voting >= 18:
    print(f"Age: {age_for_voting}")
    print("You can attend adult celebrations at Diwali!")
else:
    print(f"Age: {age_for_voting}")
    print("You might need parental supervision.")

print("\n")


# ============================================================
# PART 3: IF-ELIF-ELSE STATEMENT
# ============================================================

print("=" * 50)
print("PART 3: IF-ELIF-ELSE STATEMENT")
print("=" * 50)

# Example 1: Grade classification
marks_obtained = 78
if marks_obtained >= 90:
    grade = "A+ (Outstanding)"
elif marks_obtained >= 80:
    grade = "A (Excellent)"
elif marks_obtained >= 70:
    grade = "B (Good)"
elif marks_obtained >= 60:
    grade = "C (Average)"
elif marks_obtained >= 40:
    grade = "D (Below Average)"
else:
    grade = "F (Fail)"

print(f"Marks: {marks_obtained}")
print(f"Grade: {grade}")

print("\n")

# Example 2: School admission based on marks
entrance_marks = 85
if entrance_marks >= 90:
    school = "Top Tier School (Delhi Public School)"
elif entrance_marks >= 75:
    school = "Good School (DAV Public School)"
elif entrance_marks >= 60:
    school = "Average School (Government School)"
else:
    school = "Technical School (Vocational Training)"

print(f"Entrance Marks: {entrance_marks}")
print(f"Admission: {school}")

print("\n")

# Example 3: Shopping discount based on purchase amount (Indian Rupees)
purchase_amount = 5500  # INR
if purchase_amount >= 10000:
    discount_percent = 30
    discount_name = "Premium Member"
elif purchase_amount >= 5000:
    discount_percent = 20
    discount_name = "Gold Member"
elif purchase_amount >= 2000:
    discount_percent = 10
    discount_name = "Silver Member"
else:
    discount_percent = 0
    discount_name = "Regular Customer"

discount_amount = (purchase_amount * discount_percent) / 100
final_amount = purchase_amount - discount_amount

print(f"Purchase Amount: Rs. {purchase_amount}")
print(f"Member Status: {discount_name}")
print(f"Discount: {discount_percent}% (Rs. {discount_amount})")
print(f"Final Amount: Rs. {final_amount}")

print("\n")


# ============================================================
# PART 4: NESTED IF STATEMENTS
# ============================================================

print("=" * 50)
print("PART 4: NESTED IF STATEMENTS")
print("=" * 50)

# Example 1: Voter eligibility in India
age_years = 22
citizenship = "Indian"
if citizenship == "Indian":
    print(f"Citizenship: {citizenship}")
    if age_years >= 18:
        print(f"Age: {age_years}")
        print("You are eligible to vote in Indian elections!")
    else:
        print(f"Age: {age_years}")
        print("You must be 18 years old to vote.")
else:
    print(f"Citizenship: {citizenship}")
    print("You must be an Indian citizen to vote.")

print("\n")

# Example 2: Admission to IIT (Indian Institute of Technology)
jee_score = 250
pcm_aggregate = 95
if jee_score >= 200:
    print(f"JEE Score: {jee_score}")
    if pcm_aggregate >= 85:
        print(f"Class 12 PCM Aggregate: {pcm_aggregate}%")
        print("Congratulations! You can apply to IIT!")
    else:
        print(f"Class 12 PCM Aggregate: {pcm_aggregate}%")
        print("Your JEE score is good, but class 12 marks are needed.")
else:
    print(f"JEE Score: {jee_score}")
    print("You need a higher JEE score to apply to IIT.")

print("\n")


# ============================================================
# PART 5: MULTIPLE CONDITIONS (AND, OR)
# ============================================================

print("=" * 50)
print("PART 5: MULTIPLE CONDITIONS (AND, OR)")
print("=" * 50)

# Example 1: Using AND (both conditions must be true)
student_age = 16
student_class = 10
if student_age >= 15 and student_class >= 8:
    print(f"Age: {student_age}, Class: {student_class}")
    print("Eligible for National Talent Search Examination (NTSE)!")
else:
    print(f"Age: {student_age}, Class: {student_class}")
    print("Not eligible for NTSE yet.")

print("\n")

# Example 2: Using OR (at least one condition must be true)
isweekend = True
is_holiday = False
if isweekend or is_holiday:
    print(f"Weekend: {isweekend}, Holiday: {is_holiday}")
    print("No school today! Time to play!")
else:
    print(f"Weekend: {isweekend}, Holiday: {is_holiday}")
    print("School day! Get ready for studies.")

print("\n")

# Example 3: Science stream eligibility
physics_marks = 85
chem_marks = 78
bio_marks = 45
if (physics_marks >= 70 and chem_marks >= 70) or (physics_marks >= 80):
    print(f"Physics: {physics_marks}, Chemistry: {chem_marks}")
    print("You can pursue Science stream!")
else:
    print(f"Physics: {physics_marks}, Chemistry: {chem_marks}")
    print("Consider other streams like Commerce or Arts.")

print("\n")


# ============================================================
# PART 6: PRACTICAL EXAMPLES
# ============================================================

print("=" * 50)
print("PART 6: PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: School Fee Calculation
print("\nSchool Fee Calculation (Indian Context):\n")
student_class_num = 5
annual_fee_per_class = {
    1: 5000,
    2: 5500,
    3: 6000,
    4: 7000,
    5: 8000,
    6: 10000,
    10: 15000,
    12: 20000
}

if student_class_num in annual_fee_per_class:
    fee = annual_fee_per_class[student_class_num]
    print(f"Class: {student_class_num}")
    print(f"Annual Fee: Rs. {fee}")
    
    if student_class_num <= 3:
        print("Category: Primary")
    elif student_class_num <= 5:
        print("Category: Upper Primary")
    else:
        print("Category: Secondary")
else:
    print("Class not found in system.")

print("\n")

# Example 2: Cricket match decision
print("Cricket Match Decision (Indian Example):\n")
team_a_score = 280
team_b_score = 275
wickets_lost = 5

if team_a_score > team_b_score:
    print(f"Team A: {team_a_score} runs")
    print(f"Team B: {team_b_score} runs")
    print("Result: Team A wins!")
    runs_difference = team_a_score - team_b_score
    print(f"Team A won by {runs_difference} runs!")
elif team_a_score < team_b_score:
    print(f"Team A: {team_a_score} runs")
    print(f"Team B: {team_b_score} runs")
    print("Result: Team B wins!")
    runs_difference = team_b_score - team_a_score
    print(f"Team B won by {runs_difference} runs!")
else:
    if wickets_lost >= 10:
        print(f"Tied match! All out with {wickets_lost} wickets lost.")
    else:
        print("Match is tied!")

print("\n")


# ============================================================
# EXERCISES
# ============================================================

print("=" * 50)
print("EXERCISES FOR YOU TO TRY")
print("=" * 50)

print("""
EXERCISE 1: JEE Score Evaluation
Write a program that:
- Takes a student's JEE score (out of 300)
- If score >= 250: "You can get into top IIT"
- If score >= 200: "You can get into good IIT"
- If score >= 150: "You can get into NIT"
- If score < 150: "Try again next year"

EXERCISE 2: Monsoon Season Helper
Write a program that:
- Takes a month number (1-12)
- Tells if it's monsoon season in India (June-September)
- Suggests appropriate activities

EXERCISE 3: Festival Calendar
Write a program that:
- Takes a month number
- Tells which major Indian festival is in that month
- If no festival, says it's a regular month

EXERCISE 4: School Attendance
Write a program that:
- Takes the number of days present out of 200
- If >= 85%: "Attendance is good"
- If >= 75%: "Attendance is average, be careful"
- If < 75%: "You may not be allowed to appear in exams"
""")

print("\n")
print("Happy Coding! Keep practicing! 🚀")
print("Remember: Every decision in your program shapes its behavior!")
