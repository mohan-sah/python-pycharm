# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as content_names:
    names = content_names.readlines()
    print(names)
    people = []
    for name in names:
        name.strip("\\n")
        people.append(name)

    print(people)

with open("Input/Letters/starting_letter.txt") as letter_content:
    letter = letter_content.read()




# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
