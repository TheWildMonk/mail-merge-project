# TODO: Create a letter using starting_letter.txt
#  for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

receiver = []
with open(f"./Input/Names/invited_names.txt", mode="r") as names:
    all_names = names.readlines()
    for each_name in all_names:
        receiver.append(each_name.strip("\n"))

for each_name in receiver:
    with open(f"./Output/ReadyToSend/letter_to_{each_name}.txt", mode="w") as single_letter:
        with open("./Input/Letters/starting_letter.txt") as starting_letter:
            letter_content = starting_letter.read()
        new_letter = single_letter.write(letter_content.replace("[name]", each_name))
