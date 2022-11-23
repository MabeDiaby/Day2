# Strings
print("Hello"[0])
print("Hello"[4])
print("123" + "345") #123345

# Integer
print(123 + 345) #468
print(123_456_789) #123456789

# Float
print(3.14159) #3.14159

# Boolean
True
False

# Convert 
num_char = len(input("What is your name?"))
new_num_char - str(num_char)
print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a)) #String

a = float(123)
print(type(a)) #Float


# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first=two_digit_number[0]
sec=two_digit_number[1]
# res = int(first) + int(sec)
print(int(first) + int(sec))