
print("What is the capital of the United Kingdom?")

answer_1 = input("Choose one of the following: London, Paris, Washington, or Madrid \n")
if answer_1.lower() == "london":
    print("Correct!")
    results = 1
else:
    print("Incorrect answer, better luck next time. ")
    results = 0

print("------------------------------\n")

print("What is the most widely used currency in the European continent?")

answer_2 = input("Choose one of the following: Pound, Euro, Dollar, or Rand \n")
if answer_2.lower() == "euro":
    print("Correct!")
    results += 1
else:
    print("Incorrect answer, better luck next time. ")

print("------------------------------\n")

print("Which country won the football world champion in 1966?")
answer_3 = input("Choose one of the following: England, Germany, Spain, or Portugal \n")
if answer_3.lower() == "portugal":
    print("Correct!")
    results += 1
else:
    print("Incorrect answer, better luck next time.")

print("------------------------------\n")

if results == 3:
    print("------------------------------\n"
          "Wow! you got all the questions right. Good job!")
if results == 2:
    print("------------------------------\n"
          "Hmmm, only two answers right. Not bad")
if results == 1:
    print("------------------------------\n"
          "Only one answer was correct, gotta bump those numbers up.")
if results == 0:
    print("------------------------------\n"
          "You got nothing right")