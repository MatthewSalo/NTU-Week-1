# Task 2
number_1 = int(input("What's your first number? "))
number_2 = int(input("What's your second number? "))

if number_1 % number_2 == 0:
    print(number_2, "is a multiple of", number_1)
else:
    print(number_2, "is not a multiple of", number_1)