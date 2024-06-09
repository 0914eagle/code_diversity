
def string_xor(a: str, b: str) -> str:
    
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length.")
    
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    
    return result

# Test the function
print(string_xor('010', '110'))  # Output: '100'
