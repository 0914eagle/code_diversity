
def f1(m, n):
    # Initialize a list to store the number of Zax and Xaz islands
    zax_islands = [0] * (m + 1)
    xaz_islands = [0] * (m + 1)
    
    # Iterate through the input and count the number of Zax and Xaz islands
    for i in range(m):
        resources = list(map(int, input().split()))
        if resources[0] == 0:
            zax_islands[i] += 1
        else:
            xaz_islands[i] += 1
    
    # Check if the number of Zax and Xaz islands is equal to the total number of islands
    if sum(zax_islands) == m and sum(xaz_islands) == m:
        return "YES"
    else:
        return "NO"

def f2(m, n):
    # Initialize a list to store the number of Zax and Xaz resources
    zax_resources = [0] * (n + 1)
    xaz_resources = [0] * (n + 1)
    
    # Iterate through the input and count the number of Zax and Xaz resources
    for i in range(m):
        resources = list(map(int, input().split()))
        for j in range(1, n + 1):
            if resources[j] == j:
                zax_resources[j] += 1
            elif resources[j] == n + 1 - j:
                xaz_resources[j] += 1
    
    # Check if the number of Zax and Xaz resources is equal to the total number of resources
    if sum(zax_resources) == n and sum(xaz_resources) == n:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(f1(m, n))
    print(f2(m, n))

