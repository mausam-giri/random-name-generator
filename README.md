# Combination Generator for Filenames

Easily generate random combinations of characters to prepend, append, or insert in the middle of your filenames.

### Installation

To get started, simply install the package via pip:

```bash
pip install combogen
```

### Usage

The `generate_combination` function generates a random combination of characters based on your preferences and returns a string with a fixed part and the random combination.

#### Function Signature

```python
generate_combination(nums, fixed_string="", location="middle", isUpper=True, isLower=True, digits=True, specialChar=True)
```

#### Parameters

- **`nums`** (int):  
  The length of the random combination.

- **`fixed_string`** (str, optional):  
  Default is `""`.  
  The string in which the random combination will be inserted.

- **`location`** (str, optional):  
  Default is `"middle"`.  
  Specifies the location of the fixed string in the combination.  
  Possible values: `"start"`, `"middle"`, `"end"`.

- **`isUpper`** (bool, optional):  
  Default is `True`.  
  Whether to include uppercase characters in the combination.

- **`isLower`** (bool, optional):  
  Default is `True`.  
  Whether to include lowercase characters in the combination.

- **`digits`** (bool, optional):  
  Default is `True`.  
  Whether to include digits in the combination.

- **`specialChar`** (bool, optional):  
  Default is `False`.  
  Whether to include special characters in the combination.

#### Returns

- **str**: A string with the random combination inserted at the specified location.

---

### Examples

```python
from combogen import generate_combination

# Example 1: Combination at the start
print(generate_combination(4, fixed_string="ABC", location="start"))
# Output: ABCt857

# Example 2: Combination in the middle
print(generate_combination(4, fixed_string="ABC", location="middle"))
# Output: t8ABC57

# Example 3: Combination at the end
print(generate_combination(4, fixed_string="ABC", location="end"))
# Output: t857ABC
```

---

### Features

- Generate random combinations of uppercase letters, lowercase letters, digits, and special characters.
- Choose the location of your fixed string (start, middle, or end).
- Highly customizable with options for character inclusion (uppercase, lowercase, digits, special characters).
