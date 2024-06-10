
def get_magnitude(estimate):
    return len(str(estimate))

def main():
    N = int(input())
    for _ in range(N):
        estimate = int(input())
        print(get_magnitude(estimate))

if __name__ == '__main__':
    main()

