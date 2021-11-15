employees = open("employees.txt", "a")  # Opens (in this case) an existing file with append privileges

employees.write("\nMilo - PA")

employees.close()

employees1 = open("employees1.txt", "r+")  # Creates (in this case) a new file with read-write privileges
