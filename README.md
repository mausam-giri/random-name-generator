# prefix_combination_generator
Combination generator for filename, either prefix or suffix

This function takes 7 arguments:
- generate_combination(nums, fixed_string="", location="middle", isUpper=True, isLower=True, digits=True, specialChar=True)

"""
    Generates a random combination of numbers, uppercase letters, lowercase letters, digits, and special characters.
    
    Parameters:
    nums (int): The number of characters in the combination.
    fixed_string (str): A string that will be included in the combination at the specified location.
    location (str): The location of the fixed string in the combination. Can be "front", "middle", or "back".
    isUpper (bool): Include uppercase letters in the combination.
    isLower (bool): Include lowercase letters in the combination.
    digits (bool): Include digits in the combination.
    specialChar (bool): Include special characters in the combination.
    
    Returns:
    str: The generated combination.
"""


`
print(generate_combination(4, fixed_string="ABC", location="front"))
print(generate_combination(4, fixed_string="ABC", location="middle"))
print(generate_combination(4, fixed_string="ABC", location="back"))
`
