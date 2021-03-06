import sys ; sys.path += ['.', '../..']
import collections
from SharedCode import Function
import re

"""
>>> Single-byte XOR cipher

    The hex encoded Input has been XOR'd against a single character. Find the key, decrypt the message.

    Input: "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
"""

# ETAOIN SHRDLU - Most common frequency of letters in the english langauge in order of frequency
common_characters = ['e', 't', 'a', 'o', 'i', 'n', ' ', 's', 'h', 'r', 'd', 'l', 'u']


def task3():

    inputStr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    # Uses regex to group values into hex pairs
    decode = re.findall('..', inputStr)

    # Finds the most common hex pair
    most_common = collections.Counter(decode).most_common(1)[0][0]

    for char in common_characters:

        # The most common XORd with e will give the key
        hexChar = Function.Conversion.remove_byte_notation(Function.UTF8.hexadecimal(char))

        k = Function.XOR.hexXor(most_common, hexChar)

        key = k * round(len(inputStr) / 2)

        answer = Function.XOR.hexXor(inputStr, key)
        answer = Function.HexTo.utf8(answer)

        # Regex to check string contains alphanumeric values and punctuation
        if re.match('^[A-Za-z _.,!"\'$]*$', answer) is not None:
            # Answer found
            print(answer)
            return k

if __name__ == "__main__":
    k = task3()
    print(f"Answer found: {k} ")
