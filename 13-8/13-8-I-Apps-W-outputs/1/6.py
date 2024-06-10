
def get_resulting_sequence(a, b):
    resulting_sequence = []
    for i in range(len(a)):
        if a[i] == 0:
            resulting_sequence.append(b.pop(0))
        else:
            resulting_sequence.append(a[i])
    return resulting_sequence

def is_increasing_sequence(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    return True

def is_possible_to_recover_hitagi(a, b):
    resulting_sequence = get_resulting_sequence(a, b)
    return not is_increasing_sequence(resulting_sequence)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("Yes") if is_possible_to_recover_hitagi(a, b) else print("No")

