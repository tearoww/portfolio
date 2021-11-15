def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    # or, you know, just return max(num1, num2, num3)


def compare_strings(text1):
    if str.__contains__("dog", text1):
        return True
    else:
        return False


print(max_num(100, 200, 5))
print(compare_strings("dog"))
