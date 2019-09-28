input_value = int(input("Enter a number: "))

def to_binary(number):
    return "{0:b}".format(number)

def to_octal(number):
    return "{0:o}".format(number)

def to_hex(number):
    return "{0:X}".format(number)

print(to_binary(input_value))
print(to_octal(input_value))
print(to_hex(input_value))

