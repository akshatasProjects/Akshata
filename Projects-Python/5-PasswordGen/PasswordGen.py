import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','£','$','%','^','&','*','(',')','-']

print("WELCOME TO PASSWORD GENERATOR")

# GET INPUT FROM THE USER FOR NUMBER OF LETTERS, NUMBERS AND SYMBOLS THEY WANT TO INCLUDE
user_letter = int(input("How many letters you would like to include in your password?: "))
user_num = int(input("How many numbers you want to include in your password?: "))
user_symbols = int(input("How many symbols you want to include? :"))

print(user_letter)
print(user_num)
print(user_symbols)

gen_password =" "

for char in range(1, user_letter+1):
    # gen_password += random.choice(letters)
    gen_password = random.choice(letters)
    print(gen_password)
   
for eachNum in range(1, user_num+1):
    gen_password += random.choice(numbers)
    print(gen_password)

for sym in range(1, user_symbols+1):
    gen_password += random.choice(symbols)
    print(gen_password)

print(f"Here is the Password Generated: {shuffled_pass}")

# TYPE ERROR : it will generate a type error when you try to concatenate gen_password to numbers if those are not in string format
# concatenation can be done only with string to string