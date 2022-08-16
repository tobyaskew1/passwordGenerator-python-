import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetCaps = []
chars = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "\"", "\'", "<", ">", ",", ".", "?", "/"]
password = ''
string = ""
num = 0

for i in alphabet :
    alphabetCaps.append(i.upper())

selection = numbers + alphabetCaps + alphabet + chars

passwordLength = int(input("Please enter the length of your password: "))

while num < passwordLength:
    string = random.choice(selection)
    password = str(string) + password
    num += 1

print(password)