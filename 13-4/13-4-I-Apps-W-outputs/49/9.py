
def get_sequence_element(n):
    sequence = [1]
    current_element = 1
    current_position = 1
    while current_position < n:
        current_element += 1
        for i in range(current_element):
            sequence.append(i+1)
        current_position += current_element
    return sequence[n-1]

def main():
    n = int(input())
    print(get_sequence_element(n))

if __name__ == '__main__':
    main()

