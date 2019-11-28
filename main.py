import re

print("Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():

    global run
    global previous

    equation = ""
    if previous == 0:
        equation = input("Enter:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("See you soon, master :)")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation) #removing potential symbols that can break our program using regex

        if previous == 0:
            previous = eval (equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()