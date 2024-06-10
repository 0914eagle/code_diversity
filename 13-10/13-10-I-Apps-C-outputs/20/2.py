
def find_numbers(A, B):
    count = 0
    for i in range(A, B+1):
        count += 1
    return count

def find_numbers_in_interval(A, B):
    count = 0
    for i in range(A, B+1):
        count += 1
    return count

if __name__ == '__main__':
    Q = int(input())
    for i in range(Q):
        A, B = map(int, input().split())
        print(find_numbers_in_interval(A, B))

