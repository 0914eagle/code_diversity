
def get_input():
    N = int(input())
    L = list(map(int, input().split()))
    return N, L

def count_triangles(L):
    count = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            for k in range(j+1, len(L)):
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    count += 1
    return count

def main():
    N, L = get_input()
    print(count_triangles(L))

if __name__ == '__main__':
    main()

