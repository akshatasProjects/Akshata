# Previous password generator use to give the password in order meaning "Letters+Numbers+Symbols" so to avoid that here is the 
# Password generator with Shuffle()

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','£','$','%','^','&','*','(',')','-']

print("WELCOME TO PASSWORD GENERATOR")

# GET INPUT FROM THE USER FOR NUMBER OF LETTERS, NUMBERS AND SYMBOLS THEY WANT TO INCLUDE
user_letter = int(input("How many letters you would like to include in your password?: "))
user_num = int(input("How many numbers you want to include in your password?: "))
user_symbols = int(input("How many symbols you want to include? :"))

gen_password_list = []

for ltr in range(1, user_letter+1):
    gen_password_list.append(random.choice(letters))

for num in range(1, user_num+1):
    gen_password_list.append(random.choice(numbers))

for symbol in range(1, user_symbols):
    gen_password_list.append(random.choice(symbols))

random.shuffle(gen_password_list)
print(gen_password_list)

# CONVERTING THE LIST TO STRING

password =" "
for eachChar in gen_password_list:
    password += eachChar


print(f"Your Password is : {password}")

# Mutable Sequences Only: It works on mutable types like lists. It cannot be used directly on immutable objects such as strings or tuples, 
# which would raise a TypeError.

