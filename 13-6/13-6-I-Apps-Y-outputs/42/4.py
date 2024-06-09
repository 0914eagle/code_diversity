
def get_sticks_input():
    N = int(input())
    L = list(map(int, input().split()))
    return N, L

def is_triangle(a, b, c):
    return (a**2 + b**2) >= c**2

def count_triangles(L):
    count = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            for k in range(j+1, len(L)):
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k] and is_triangle(L[i], L[j], L[k]):
                    count += 1
    return count

def main():
    N, L = get_sticks_input()
    print(count_triangles(L))

if __name__ == '__main__':
    main()

