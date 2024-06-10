
def change_base(x: int, base: int) -> str:
    
    # Convert input number to string in given base
    x_str = str(x)
    x_str = x_str.zfill(len(x_str) + (6 - len(x_str)) // 3)
    x_str = x_str.replace('0', '').replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E').replace('6', 'F').replace('7', 'G').replace('8', 'H').replace('9', 'I')
    # Reverse the string
    x_str = x_str[::-1]
    # Return the reversed string
    return x_str

