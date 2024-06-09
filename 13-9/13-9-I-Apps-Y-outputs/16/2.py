
def solve(H, n, d):
    # Calculate the total hit points after each round
    total_hp = [H]
    for i in range(n):
        total_hp.append(total_hp[i] + d[i])
    
    # Find the first minute when the monster's hit points are less than or equal to 0
    for i in range(n):
        if total_hp[i] <= 0:
            return i + 1
    
    # If the battle continues infinitely, return -1
    return -1

