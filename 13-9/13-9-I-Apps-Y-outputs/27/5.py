
def solve(friends):
    n = len(friends)
    given_gifts = [0] * n
    received_gifts = [0] * n
    for i in range(n):
        if friends[i] != 0:
            given_gifts[i] = 1
            received_gifts[friends[i] - 1] = 1
    
    for i in range(n):
        if friends[i] == 0:
            for j in range(n):
                if given_gifts[j] == 0 and received_gifts[j] == 0:
                    friends[i] = j + 1
                    given_gifts[i] = 1
                    received_gifts[j] = 1
                    break
    
    return friends

