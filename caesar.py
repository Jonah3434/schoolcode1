'''
Jonah Belttari
1/8/2020
Caesar Cipher
'''
word = input("Give a four letter word in caps ")
shift = int(input(("Enter the shift 1-25 ")))
letter1 = word[0]
letter2 = word[1]
letter3 = word[2]
letter4 = word[3]
letter1=ord(letter1) + shift
if letter1>=91:
    letter1 = letter1 -26
letter2 = ord(letter2) + shift
if letter2>=91:
    letter2 = letter2 -26
letter3 = ord(letter3) + shift
if letter3>=91:
    letter3 = letter3-26
letter4 = ord(letter4) + shift
if letter4>=91:
    letter4 = letter4 -26
print(chr(letter1) + chr(letter2) + chr(letter3) + chr(letter4))