number = int(input("Enter a single digit "))
if number >= 4:
    luhn_double = (number*2) - 9
    print("The luhn double for", number, "is", luhn_double)
elif number <= 9:
    luhn_double = number*2
    print("The luhn double for", number, "is", luhn_double)
else:
    print("Invalid number")

