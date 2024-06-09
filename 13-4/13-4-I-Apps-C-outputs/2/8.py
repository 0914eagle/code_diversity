
def is_beautiful_sequence(sequence):
    for i in range(len(sequence) - 1):
        if abs(sequence[i] - sequence[i+1]) != 1:
            return False
    return True

def construct_beautiful_sequence(a, b, c, d):
    sequence = []
    for i in range(a):
        sequence.append(0)
    for i in range(b):
        sequence.append(1)
    for i in range(c):
        sequence.append(2)
    for i in range(d):
        sequence.append(3)
    return sequence

def main():
    a, b, c, d = map(int, input().split())
    sequence = construct_beautiful_sequence(a, b, c, d)
    if is_beautiful_sequence(sequence):
        print("YES")
        print(" ".join(map(str, sequence)))
    else:
        print("NO")

if __name__ == "__main__":
    main()

