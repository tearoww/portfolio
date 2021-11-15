print("Hello! I'm a calculator. Give me a number:")

num1 = float(input("> "))

print("Thanks. Now I need an operator:")

operator = input("> ")

print("Cool. Lastly I need a second number:")

num2 = float(input("> "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Sorry, but the operator you gave me wasn't correct.")
