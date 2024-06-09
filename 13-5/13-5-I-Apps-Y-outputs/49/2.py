
def f1(n, a):
    # Initialize a dictionary to map each number to its final value
    final_values = {i: i for i in range(1, 1000000001)}
    final_values[1] = 2
    final_values[2] = 1
    final_values[3] = 4
    final_values[4] = 3
    final_values[5] = 6
    final_values[6] = 5
    final_values[10] = 9
    final_values[9] = 10

    # Apply the algorithm to the array
    result = []
    for i in range(n):
        result.append(final_values[a[i]])

    return result

def f2(n, a):
    # Initialize a dictionary to map each number to its final value
    final_values = {i: i for i in range(1, 1000000001)}
    final_values[1] = 2
    final_values[2] = 1
    final_values[3] = 4
    final_values[4] = 3
    final_values[5] = 6
    final_values[6] = 5
    final_values[10] = 9
    final_values[9] = 10

    # Apply the algorithm to the array
    result = []
    for i in range(n):
        result.append(final_values[a[i]])

    return result

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    result = f1(n, a)
    print(*result, sep=' ')

