import random
import string

password = ""
selection = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

print("Welcome to Toby's password generator!")
passwordLength = int(input("Please enter the length of your password: "))

password = random.sample(selection, passwordLength)

print("Your new password is : "+"".join(password))
print("Don't share this password with anyone, but share the generator!")