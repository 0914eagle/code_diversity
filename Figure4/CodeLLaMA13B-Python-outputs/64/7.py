FIX = 

def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    if s[-1] == "y":
        count -= 1
    return count

