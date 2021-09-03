employees = open("employees.txt", "r")  # TODO Change to a HTML course file

if employees.readable():
    print(employees.read())

    # for employee in employees.readlines():
    #     print(employee)

employees.close()
