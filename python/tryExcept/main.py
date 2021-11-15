is_number = False

print("Hello! Please kindly give me a number and nothing but a number:")

while not is_number:
    try:
        number = float(input("> "))

        print("Thanks! You gave me " + str(number))

        is_number = True
    except ValueError:
        print("HEY! NUMBERS ONLY AROUND HERE!")
