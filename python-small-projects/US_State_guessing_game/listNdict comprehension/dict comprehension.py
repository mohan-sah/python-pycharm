# SIMPLE
# new_dict = { new_key : new_value for item in list }

# LEVEL UP
# new_dict = {new_key: new_value for (key,value) in old_dict.items()}

# LEVEL UP
# new_dict = {new_key: new_value for (key,value) in old_dict.items() IF TEST}
names = ['Alex', "mohan", 'ravi', 'shubham', 'goyal', 'gagan', 'rahul']
print(f"names : {names}")

# goal
# students_score = {
#     "Alex": 89,
#     "mohan": 90,
#     'ravi': 34,
#     'shubham': 89,
# }
from random import randint

student_score = {individual: randint(60, 99) for individual in names}
print(student_score)
# goal achieved.

# level up goal
passed_student = {student: score for (student, score) in student_score.items() if score > 70}
print(passed_student)

# goal cleared

# LEVEL UP
# for pandas data frame
# new_dict = {new_key: new_value for (index, row) in df.iterrows()}
