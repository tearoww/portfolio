def translate(phrase):
    result = ""

    for character in phrase:
        if character.upper() in "AEIOUYÅÄÖ":
            result = result + ""
        else:
            result = result + character

    return result


print("Hey! I'm a sort of a translator. Give me a phrase:")
print("\nThis is what I came up with:\n" + translate(input("> ")))
