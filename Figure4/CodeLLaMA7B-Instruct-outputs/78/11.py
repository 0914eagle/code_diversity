

def hex_key(num):
    

    count = 0
    for char in num:
        if char in "2357BDF":
            count += 1
    return count

