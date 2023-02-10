"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.
"""

def alphabet_position(text):
    #chr(a) = 97, chr(z) = 122
    result = []
    for letter in text:
        if letter.isalpha():
            result.append(str(26-(ord('z') - ord(letter.lower()))))
    
    return " ".join(result)

print(alphabet_position("The sunset sets at twelve o' clock."))