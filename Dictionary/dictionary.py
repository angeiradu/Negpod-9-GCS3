#!/usr/bin/python3
def roman_to_int(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for i in range(len(roman_numeral)-1, -1, -1):
        current_value = roman_values[roman_numeral[i]]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        prev_value = current_value
    
    return result

#Ask the user to enter a Roman numeral and convert it to an integer
roman_numeral = input("Enter a Roman numeral: ")
integer = roman_to_int(roman_numeral)

print(roman_numeral, "is", integer)

