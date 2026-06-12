# Holberton School Interview - UTF-8 Validation

## Description
This project is part of the Holberton School technical interview preparation.
It focuses on bitwise operations and string/data encoding concepts, specifically
validating whether a given set of bytes represents a valid UTF-8 encoding.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code follows the `PEP 8` style (version 1.7.x), checked with `pycodestyle`
- All files are executable

## Tasks

### 0. UTF-8 Validation
**File:** `utf8_validation/0-validate_utf8.py`

Method `validUTF8(data)` that determines if a given data set represents
a valid UTF-8 encoding.

- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data is represented as a list of integers, where each integer
  represents 1 byte of data (only the 8 least significant bits are used)

**Approach:**
The function iterates through the list of integers. For each byte, it
checks the leading bits to determine how many bytes the current character
spans (1 to 4), based on the standard UTF-8 byte patterns:

| Leading bits | Total bytes |
|--------------|-------------|
| `0xxxxxxx`   | 1           |
| `110xxxxx`   | 2           |
| `1110xxxx`   | 3           |
| `11110xxx`   | 4           |

It then verifies that the correct number of continuation bytes follow,
each starting with `10xxxxxx`. If at any point the pattern is invalid
or the data runs out unexpectedly, the function returns `False`.
If the entire data set is parsed successfully, it returns `True`.

**Example usage:**
```python
#!/usr/bin/python3
validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))
# True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))
# True

data = [229, 65, 127, 256]
print(validUTF8(data))
# False
```

## Author
SagaLou