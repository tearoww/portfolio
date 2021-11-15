print(2 ** 3)


def power(base_number, power_number):
    result = 1

    for index in range(power_number):
        result = result * base_number

    return result


print(power(2, 4))
print(power(2, 5))
