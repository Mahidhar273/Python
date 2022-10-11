#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:
    contents = file.read()

Names = contents.split('\n')

with open(f"./Output/ReadyToSend/example.txt") as content:
    text = content.read()

for names in Names:
    with open(f"./Output/ReadyToSend/letter for {names}.txt", mode='w') as new:
        new_text = text.replace('Aang', names)
        new.write(new_text)



