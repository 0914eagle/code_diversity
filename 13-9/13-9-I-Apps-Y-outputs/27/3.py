
def solve(friends):
    n = len(friends)
    given = [0] * n
    received = [0] * n
    for i in range(n):
        if friends[i] != 0:
            given[i] = 1
            received[friends[i] - 1] += 1
    
    for i in range(n):
        if given[i] == 0:
            for j in range(n):
                if received[j] == 0:
                    given[i] = 1
                    received[j] += 1
                    break
    
    for i in range(n):
        if given[i] == 0:
            return []
    
    result = []
    for i in range(n):
        result.append(friends[i] if friends[i] != 0 else received[i] + 1)
    return result

