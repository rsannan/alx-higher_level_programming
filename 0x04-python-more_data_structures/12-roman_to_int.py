#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    sum_letter = 0
    if isinstance(roman_string, str) and roman_string is not None:
        for letter in range(len(roman_string)):
            if roman_string[letter] not in roman_dict:
                sum_letter = sum_letter + 0
                continue

            c_letter = roman_dict.get(roman_string[letter])

            if letter == 0:
                sum_letter = c_letter

            else:
                p_letter = roman_dict.get(roman_string[letter-1])
                if c_letter > p_letter:
                    sum_letter = c_letter - p_letter
                else:
                    sum_letter = sum_letter + c_letter


        return sum_letter
    return 0
