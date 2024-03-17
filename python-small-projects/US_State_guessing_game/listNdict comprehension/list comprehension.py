#SIMPLE

# new_list = [new_item for item in old_list]

# level up
# new_list = [new_item for item in old_list if test]
# example : missed_list = [str(state.strip()) for state in state_names if state.lower() not in answered_list]




student_dict = {
    "student" : ["Angela", "james" , "Lily"],
    "score" : [56, 76,98]
}

# looping through dictionaries:
# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#looping through dataframe
#
# for (key,value) in student_data_frame.items():
#     print(value)

# loop through rows of data frame thorough itters part 1
for (index,row) in student_data_frame.iterrows():
    print(row.students)

# loop through rows of data frame thorough itters part2
for (index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row)