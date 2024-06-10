
def read_input():
    N = int(input())
    attendees = list(map(int, input().split()))
    return N, attendees

def solve(N, attendees):
    pairs = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if abs(i-j) == sum(attendees[i:j+1]):
                pairs += 1
    return pairs

def main():
    N, attendees = read_input()
    print(solve(N, attendees))

if __name__ == '__main__':
    main()

