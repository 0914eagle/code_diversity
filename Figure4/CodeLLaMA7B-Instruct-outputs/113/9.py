

def odd_count(lst):
    
    result = []
    for i, string in enumerate(lst):
        count = 0
        for char in string:
            if int(char) % 2 == 1:
                count += 1
        result.append(f"the number of odd elements {count}n the str{i}ng {i} of the {i}nput.")
    return result


