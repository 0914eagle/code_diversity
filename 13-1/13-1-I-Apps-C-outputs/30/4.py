
def f1(m, n):
    # Initialize a list to store the number of islands each being can occupy
    zax_islands = [0] * (m + 1)
    xaz_islands = [0] * (m + 1)
    
    # Iterate through the input and update the number of islands each being can occupy
    for i in range(m):
        resources = list(map(int, input().split()))
        for resource in resources:
            if resource != 0:
                if resource % 2 == 0:
                    zax_islands[i + 1] += 1
                else:
                    xaz_islands[i + 1] += 1
    
    # Check if the Zax and Xaz can coexist on El-gă-rizm
    for i in range(1, m + 1):
        if zax_islands[i] + xaz_islands[i] != n:
            return "NO"
    
    return "YES"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(f1(m, n))

