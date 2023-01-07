#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Jan 6, 2023
# This program gets user input and
# checks if each character is in the unicode
# dictionary, it then displays each character
# and the unicode


def display_in_hex(string, unicode_dict):
    # Create a list to store the hexadecimal Unicode values
    hex_values = []

    # Iterate through each character in the string
    for char in string:
        # Add the hexadecimal Unicode value to the list
        hex_values.append(f"0x{unicode_dict[char]:x}")

    # Return the list of hexadecimal Unicode values
    return hex_values


def main():

    # Create an empty dictionary to store the Unicode values
    unicode_dict = {}

    # Add the Unicode values for the basic Latin characters to the dictionary
    for i in range(ord("A"), ord("Z") + 1):
        unicode_dict[chr(i)] = i
    for i in range(ord("a"), ord("z") + 1):
        unicode_dict[chr(i)] = i

    # Add the Unicode values for special characters to the dictionary
    unicode_dict[" "] = 0x20
    unicode_dict["."] = 0x2E

    # Ask the user to enter a string
    string = input("Enter a string: ")

    # Ensure that the input is a valid
    if string not in unicode_dict.keys():
        print("Not in unicode dictionary.")
        return -1

    else:
        # Get the list of hexadecimal Unicode values for each character in the string
        hex_values = display_in_hex(string, unicode_dict)

        # Print the hexadecimal Unicode values for each character in the string
        for char, hex_value in zip(string, hex_values):
            print(f"{char}: {hex_value}")

    # Get the list of hexadecimal Unicode values for each character in the string
    hex_values = display_in_hex(string, unicode_dict)

    # Print the hexadecimal Unicode values for each character in the string
    for char, hex_value in zip(string, hex_values):
        print(f"{char}: {hex_value}")


if __name__ == "__main__":
    main()
