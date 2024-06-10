
import math

def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_min_cost(A, B):
    min_cost = 0
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i] == A[j]:
                min_cost += get_distance(A[j], A[(j+1)%len(A)])
                break
    return min_cost

def main():
    a = int(input())
    A = []
    for i in range(a):
        x, y = map(int, input().split())
        A.append((x, y))
    b = int(input())
    B = []
    for i in range(b):
        x, y = map(int, input().split())
        B.append((x, y))
    print(get_min_cost(A, B))

if __name__ == '__main__':
    main()

