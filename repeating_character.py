def find_first_repeating_character(s):
    char_count = {}

    for char in s:
        if char in char_count:
            print(f"First repeating character: {char}, Memory address: {hex(id(char))}")
            return char
        char_count[char] = 1
    
    return None

# Test cases
print(find_first_repeating_character("hello"))  # Output: 'l', Memory address
print(find_first_repeating_character("python"))  # Output: None
print(find_first_repeating_character("swiss"))   # Output: 's', Memory address
