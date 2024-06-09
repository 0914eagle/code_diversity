
def can_grasshopper_eat_insect(n, k, line):
    start, end = line.index("G"), line.index("T")
    if abs(start - end) > k:
        return "NO"
    
    for i in range(start, end, k):
        if line[i] == "#":
            return "NO"
    
    return "YES"

