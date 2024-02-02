#!/usr/bin/python3
"""Module that defines function validUTF8"""


def validUTF8(data):
    # Function to check if a given integer is a valid continuation byte
    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        if (data[i] & 0b10000000) == 0:  # 1-byte character
            length = 1
        elif (data[i] & 0b11100000) == 0b11000000:  # 2-byte character
            length = 2
        elif (data[i] & 0b11110000) == 0b11100000:  # 3-byte character
            length = 3
        elif (data[i] & 0b11111000) == 0b11110000:  # 4-byte character
            length = 4
        else:
            return False  # Invalid leading byte

        # Check if the following bytes are valid continuations
        for j in range(1, length):
            if i + j >= len(data) or not is_continuation(data[i + j]):
                return False

        # Move to the next character
        i += length

    return True
