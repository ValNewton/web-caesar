
def alphabet_position(letter):
    '''returns index value of character in lowercase alphabet'''
    char = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value = alphabet.find(char)
    return value

def rotate_character(char, rot):
    '''this function rotates and alpha character and returns new character'''
    if not char.isalpha():                  #returns character unchanged if not a letter
        return char
    if rot > 25:                            #rotate only once through alphabet
        rot = rot % 26
    index =  alphabet_position(char)
    new_index = index + rot
    if new_index > 25:
        new_index = new_index - 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_char = alphabet[new_index]
    if char.isupper():                      #Capitalize new letter if original was capitalized,
        new_char = new_char.upper()
    return new_char


def encrypt(text,rot):
    '''encrypt text by rotating alpha characters by given amount(rot)'''
    new_text = ""
    for char in text:
        new_char = rotate_character(char,rot)
        new_text = new_text + new_char
    return new_text

#text = input("Type a message:")
#rot = int(input("Rotate by:")
#print(encrypt(text, rot))
