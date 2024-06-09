
def f1(N, A):
    # Initialize a dictionary to store the count of each integer
    count = {}
    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    
    # Initialize the answer array
    answer = [0] * N
    
    # Iterate through the dictionary and calculate the answer for each k
    for k in range(N):
        answer[k] = 0
        for a in count:
            if a != k+1 and count[a] > 0:
                answer[k] += count[a]
    
    return answer

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    answer = f1(N, A)
    for a in answer:
        print(a)

