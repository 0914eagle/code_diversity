

def reverse_delete(s,c):
    
    # Your code here
    result = ""
    for char in s:
        if char not in c:
            result += char
    if result == result[::-1]:
        return (result, True)
    else:
        return (result, False)

