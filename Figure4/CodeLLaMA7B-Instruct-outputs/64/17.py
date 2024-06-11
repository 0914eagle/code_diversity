

FIX = 

def vowels_count(s):
    
    count = 0
    for char in s:
        if char in "aeiouy" and char != "y" or char == "y" and s[-1] == "y":
            count += 1
    return count

