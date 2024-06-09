
def f1(N, A):
    # Initialize a dictionary to store the count of equal integers
    count = {}

    # Iterate over the input array and increment the count of equal integers
    for i in range(N):
        if i != k:
            if A[i] in count:
                count[A[i]] += 1
            else:
                count[A[i]] = 1

    # Return the sum of the counts of equal integers
    return sum(count.values())

def f2(...):
    ...

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    for k in range(N):
        print(f1(N, A))

