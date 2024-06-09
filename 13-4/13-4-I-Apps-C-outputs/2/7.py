
def is_beautiful_sequence(seq):
    return all(abs(seq[i] - seq[i+1]) == 1 for i in range(len(seq)-1))

def construct_beautiful_sequence(a, b, c, d):
    seq = []
    for i in range(a):
        seq.append(0)
    for i in range(b):
        seq.append(1)
    for i in range(c):
        seq.append(2)
    for i in range(d):
        seq.append(3)
    return seq

def main():
    a, b, c, d = map(int, input().split())
    seq = construct_beautiful_sequence(a, b, c, d)
    if is_beautiful_sequence(seq):
        print("YES")
        print(" ".join(str(x) for x in seq))
    else:
        print("NO")

if __name__ == "__main__":
    main()

