
def f1(s1, s2, t):
    # find the position of the first difference between s1 and s2
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            break
    
    # if there is no difference, return -1
    if i == len(s1):
        return -1
    
    # find the position of the second difference between s1 and s2
    for j in range(i+1, len(s1)):
        if s1[j] != s2[j]:
            break
    
    # if there is no second difference, return -1
    if j == len(s1):
        return -1
    
    # find the position of the third difference between s1 and s2
    for k in range(j+1, len(s1)):
        if s1[k] != s2[k]:
            break
    
    # if there is no third difference, return -1
    if k == len(s1):
        return -1
    
    # if we reach this point, we have found three different positions
    # return the string s1 with the characters at positions i, j, and k changed
    return s1[:i] + s2[i] + s1[j+1:k] + s2[j] + s1[k+1:]

def f2(s1, s2, t):
    # find the position of the first difference between s1 and s2
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            break
    
    # if there is no difference, return -1
    if i == len(s1):
        return -1
    
    # find the position of the second difference between s1 and s2
    for j in range(i+1, len(s1)):
        if s1[j] != s2[j]:
            break
    
    # if there is no second difference, return -1
    if j == len(s1):
        return -1
    
    # find the position of the third difference between s1 and s2
    for k in range(j+1, len(s1)):
        if s1[k] != s2[k]:
            break
    
    # if there is no third difference, return -1
    if k == len(s1):
        return -1
    
    # if we reach this point, we have found three different positions
    # return the string s2 with the characters at positions i, j, and k changed
    return s2[:i] + s1[i] + s2[j+1:k] + s1[j] + s2[k+1:]

if __name__ == '__main__':
    n, t = map(int, input().split())
    s1 = input()
    s2 = input()
    
    result = f1(s1, s2, t)
    if result == -1:
        result = f2(s1, s2, t)
    
    print(result)

