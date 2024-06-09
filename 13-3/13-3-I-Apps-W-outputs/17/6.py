
def f1(N, A):
    # Initialize a dictionary to store the count of each integer
    count = {}
    for i in range(N):
        if i != k:
            if A[i] in count:
                count[A[i]] += 1
            else:
                count[A[i]] = 1
    
    # Initialize the answer to 0
    answer = 0
    
    # Iterate through the dictionary and check if any integer has a count of 2 or more
    for key, value in count.items():
        if value >= 2:
            answer += 1
    
    # Return the answer
    return answer

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    for k in range(N):
        print(f1(N, A))

