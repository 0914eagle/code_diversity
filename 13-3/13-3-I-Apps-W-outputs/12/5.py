
def f1(K):
    # Calculate the number of initial configurations that lead to the final
    num_configurations = 1
    for i in range(K):
        num_configurations = num_configurations * (2 * K - i) % (10**9 + 9)
    return num_configurations

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    K = int(input())
    print(f1(K))

