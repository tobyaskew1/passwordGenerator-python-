import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabetCaps = []
chars = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", ":", ";", "\"", "\'", "<", ">", ",", ".", "?", "/"]
password = []
num = 0

for i in alphabet :
    alphabetCaps.append(i.upper())

passwordLength = int(input("Please enter the length of your password: "))

while num < passwordLength:
    password.append(random.choice(numbers))
    num += 1
    while num < passwordLength:
        password.append(random.choice(chars))
        num += 1
        while num < passwordLength:
            password.append(random.choice(alphabetCaps))
            num += 1
            while num < passwordLength:
                password.append(random.choice(alphabet))
                num += 1

random.shuffle(password)
print(password)