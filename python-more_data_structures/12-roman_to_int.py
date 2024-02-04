#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (roman_string and isinstance(roman_string, str)):
        return 0
    diction = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
               "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    length = len(roman_string)
    number = 0
    i = 0
    while i < length:
        if i < length - 1 and roman_string[i: i + 2] in diction.keys():
            number = number + diction[roman_string[i: i + 2]]
            i = i + 1
        elif roman_string[i] in diction.keys():
            number = number + diction[roman_string[i]]
        i = i + 1
    return number
