import random
import string

def generate_combination(nums: int, fixed_string: str="", location: str="start", isUpper: bool=True, isLower: bool=True, digits: bool=True, specialChar: bool=False) -> str:
    """
    Generates random combination of characters based upon arguments and return fixed_string with combination
    
    Parameters:
    ----------
        nums: int
            Length of random combination

        fixed_string (Optional): str
            default: ""
            String in which random combination will be included

        location (Optional): str
            default: "start"
            values: "start", "middle", "end"
            Location of fixed string in the combination

        isUpper (Optional): bool
            default: True
            Uppercase characters included in the combination

        isLower (Optional): bool
            default: True
            Lowercase characters included in the combination

        digits (Optional): bool
            default: True
            Digits included in the combination

        specialChar (Optional): bool
            default: False
            Special Characters included in the combination

    Returns:
    -------
        str: fixed_string with random combination as per location
    """
    combination = ""
    characters = ""
    if isUpper:
        characters += string.ascii_uppercase
    if isLower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if specialChar:
        characters += string.punctuation

    if location == "start":
        combination += fixed_string
    for i in range(nums):
        combination += random.choice(characters)
    if location == "middle":
        combination = combination[:int(nums/2)] + fixed_string + combination[int(nums/2):]
    if location == "end":
        combination += fixed_string
    return combination
