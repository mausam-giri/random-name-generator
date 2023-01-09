
# combogen

  

## Combination generator for filename, either prefix or suffix

  

This function takes 7 arguments:

`generate_combination(nums, fixed_string="", location="middle", isUpper=True, isLower=True, digits=True, specialChar=True)`



  

>  Generates random combination of characters based upon arguments and return fixed_string with combination

Parameters:
---------- 
- nums: int

    Length of random combination

- fixed_string (Optional): str

    default: ""
    
    String in which random combination will be included
    
- location (Optional): str

    default: "start"

    values: "start", "middle", "end"

    Location of fixed string in the combination

- isUpper (Optional): bool

    default: True
    
    Uppercase characters included in the combination

- isLower (Optional): bool

    default: True

    Lowercase characters included in the combination

- digits (Optional): bool

    default: True

    Digits included in the combination

- specialChar (Optional): bool

   default: False

   Special Characters included in the combination


Returns:
---------- 
- str: fixed_string with random combination as per location 

```
    print(generate_combination(4, fixed_string="ABC", location="start"))
        Output: ABCt857
    
    print(generate_combination(4, fixed_string="ABC", location="middle"))
        Output: t8ABC57
    
    print(generate_combination(4, fixed_string="ABC", location="end"))
        Output: t857ABC
```
