# Write a code that creates password using entirely user inputs
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator")
user_letters = int(input("How many letters do you want in your password?"))
user_symbols = int(input("How many symbols do you want in your password?"))
user_numbers = int(input("How many numbers do you want in your password?"))

# Order not randomized
#password = random.randint(0, user_numbers) + random.randint(0, user_symbols) + random.randint(0, user_letters)
#print(''.join(random.sample(letters, user_letters)) + ''.join(random.sample(symbols, user_symbols)) + ''.join(random.sample(numbers, user_numbers)))

'''password = ""
for char in range(0, user_letters):
    password += random.choice(letters)

for char in range(0, user_symbols):
    password += random.choice(symbols)

for char in range(0, user_numbers):
    password += random.choice(numbers)

print(password)'''

# Order randomized
password_list = []
for char in range(0, user_letters):
    password_list.append(random.choice(letters))

for char in range(0, user_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, user_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")