
def f1(h, m, s, t_1, t_2):
    # Convert the input times to integers
    t_1 = int(h * 3600 + m * 60 + s)
    t_2 = int(t_2 * 3600)
    
    # Check if the target time is reachable
    if t_1 == t_2:
        return "YES"
    
    # Check if the target time is on the same side of the clock face as the starting time
    if t_1 < t_2 and t_1 + 12000 < t_2:
        return "NO"
    if t_1 > t_2 and t_1 - 12000 > t_2:
        return "NO"
    
    # Check if the target time is on the opposite side of the clock face as the starting time
    if t_1 < t_2 and t_1 + 12000 > t_2:
        return "YES"
    if t_1 > t_2 and t_1 - 12000 < t_2:
        return "YES"
    
    # Check if the target time is on the same side of the clock face as the starting time, but not on the same hour
    if t_1 < t_2 and t_1 + 3600 < t_2:
        return "NO"
    if t_1 > t_2 and t_1 - 3600 > t_2:
        return "NO"
    
    # Check if the target time is on the opposite side of the clock face as the starting time, but not on the same hour
    if t_1 < t_2 and t_1 + 3600 > t_2:
        return "YES"
    if t_1 > t_2 and t_1 - 3600 < t_2:
        return "YES"
    
    # If none of the above conditions are met, the target time is not reachable
    return "NO"

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    h = int(input())
    m = int(input())
    s = int(input())
    t_1 = int(input())
    t_2 = int(input())
    
    print(f1(h, m, s, t_1, t_2))

