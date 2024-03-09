# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as content_names:
    old_names = content_names.readlines()
    names = []
    for name in old_names:
        names.append(name.strip())
    print(names)


with open("Input/Letters/starting_letter.txt") as letter_content:
    letter = letter_content.read()
    print(letter)

for name in names:
    new_letter = letter.replace("[name]", f"{name}")
    with open(f"Output/ReadyToSend/letter_for_{name}.txt" , mode="w") as wishes:
        wishes.write(new_letter)




# with open("my_file.txt", mode="a") as file:
#     file.write("\nho ho ho")




# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
