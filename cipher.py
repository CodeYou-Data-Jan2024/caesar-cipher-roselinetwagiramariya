def roseline_caesar(text, shift=5):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text
# this code cares whether the character is capitalized and lowercase but it does not encrypt numbers as well. Furthermore, it does not include a dictionary. 
plain_text = input("Enter the text to encrypt: ")
encrypted_text = roseline_caesar(plain_text)
print("Encrypted text:", encrypted_text)
