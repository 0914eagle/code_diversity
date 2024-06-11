FIX = 

def vowels_count(s):
    
    vowels = "aeiou"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
        elif i == "y" and s[-1] == "y":
            count += 1
    return count

