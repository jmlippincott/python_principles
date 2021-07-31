# Write a function named format_number that takes a non-negative number as its only parameter.
#
# Your function should convert the number to a string and add commas as a thousands separator.
#
# For example, calling format_number(1000000) should return "1,000,000".

def format_number(number):
    number = str(number)
    commas  = ((len(number) - 1) // 3)
    if len(number) > 3:
        for i in range(commas):
            number = number[:((-3 * (i + 1)) - i)] + "," + number[((-3 * (i + 1)) - i):]
        return number
    else:
        return number