import random
import string

def generatePassword(minLength, numbers = True, specialChars = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialChars:
        characters += special

    pwd = ""
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(pwd) < minLength:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            hasNumber = True
        elif new_char in special:
            hasSpecial = True    

        meetsCriteria = True
        if numbers:
            meetsCriteria = hasNumber
        if specialChars:
            meetsCriteria = meetsCriteria and hasSpecial

    return pwd

minLength = int(input("Enter the minimum length: "))
hasNumber = input("Do you want to have numbers (y/n)?").lower() == "y"
hasSpecial = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generatePassword(minLength, hasNumber, hasSpecial)  
print("The generate password is: ", pwd)              