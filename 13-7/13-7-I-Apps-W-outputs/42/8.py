
def read_input():
    N = int(input())
    attendees = list(map(int, input().split()))
    return N, attendees

def count_pairs(N, attendees):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(i-j) == attendees[i] + attendees[j]:
                count += 1
    return count

def main():
    N, attendees = read_input()
    print(count_pairs(N, attendees))

if __name__ == '__main__':
    main()

