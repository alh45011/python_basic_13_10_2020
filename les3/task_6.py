def capitalize(string):
    code = ord(string[0]) - 32
    return chr(code) + string[1:]


print(capitalize("string"))

def capitalize_string(string):
    values = string.split()
    output = ""

    for value in values:
        output += capitalize(value) + " "

    return output[0:-1]


print(capitalize_string("some stupid string"))
