
def get_binary_representations(n):
    representations = 0
    for i in range(n):
        representations += get_binary_representations_helper(i, n)
    return representations

def get_binary_representations_helper(i, n):
    if i == 0:
        return 1
    if i == n:
        return 0
    representations = 0
    for j in range(i+1, n+1):
        representations += get_binary_representations_helper(j, n)
    return representations

if __name__ == '__main__':
    n = int(input())
    print(get_binary_representations(n))

