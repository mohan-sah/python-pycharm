# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas as pd

nato_phonetic_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

# loop through rows of data frame
dict_nato = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
    # print(row.letter)
    # print(row.code)
print(dict_nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input().upper()
word_list = [item for item in user_input]
print(word_list)

phonetic_code = [dict_nato[item] for item in word_list ]
print(phonetic_code)

