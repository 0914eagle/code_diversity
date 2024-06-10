
def get_input():
    n = int(input())
    balls = list(map(int, input().split()))
    k = int(input())
    no_next_to = list(map(int, input().split()))
    l = int(input())
    seq = list(map(int, input().split()))
    return n, balls, k, no_next_to, l, seq

def get_all_valid_arrangements(n, balls, k, no_next_to, l, seq):
    valid_arrangements = []
    for i in range(n):
        for j in range(n):
            if i != j and (i not in no_next_to or j not in no_next_to):
                valid_arrangements.append([i, j])
    return valid_arrangements

def get_num_arrangements(valid_arrangements, balls, l, seq):
    num_arrangements = 0
    for arrangement in valid_arrangements:
        sequence = []
        for i in range(l):
            sequence.append(arrangement[i % 2])
        for i in range(len(balls)):
            if balls[i] != 0:
                sequence.append(i + 1)
                balls[i] -= 1
        if sequence == seq:
            num_arrangements += 1
    return num_arrangements

def main():
    n, balls, k, no_next_to, l, seq = get_input()
    valid_arrangements = get_all_valid_arrangements(n, balls, k, no_next_to, l, seq)
    num_arrangements = get_num_arrangements(valid_arrangements, balls, l, seq)
    print(num_arrangements % 1000000007)

if __name__ == '__main__':
    main()

