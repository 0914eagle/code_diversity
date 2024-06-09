
def get_number_of_boxes(n, m, a, X):
    # Write your code here
    return ...

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    X = list(map(int, input().split()))
    for i in range(m):
        print(get_number_of_boxes(n, m, a, X[i]))

if __name__ == '__main__':
    main()

