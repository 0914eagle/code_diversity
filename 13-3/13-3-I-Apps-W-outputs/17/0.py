
def f1(N, A):
    # Initialize a dictionary to store the count of each integer
    count = {}
    for i in range(N):
        if i + 1 != k:
            if A[i] in count:
                count[A[i]] += 1
            else:
                count[A[i]] = 1
    
    # Initialize the answer to 0
    answer = 0
    
    # Iterate through the dictionary and check if any integer has a count greater than 1
    for key, value in count.items():
        if value > 1:
            answer += value * (value - 1) // 2
    
    return answer

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    for k in range(1, N + 1):
        print(f1(N, A, k))

