def rose_leo(text, shift=5):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    shifted_alphabet = {}
    for i in range(len(alphabet)):
        shifted_alphabet[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]

    encrypted_text = ""
    for char in text:
        if char.lower() in alphabet:  
            if char.islower():
                encrypted_text += shifted_alphabet[char]
            else:
                encrypted_text += shifted_alphabet[char.lower()].upper()
        else:
            encrypted_text += char
    return encrypted_text
# this code also includes numbers so that they are also encrypted. And see like 19 LOL 
plain_text = input("Let me help you hide your secrets: ")
encrypted_text = rose_leo(plain_text)
print("Encrypted text:", encrypted_text)
