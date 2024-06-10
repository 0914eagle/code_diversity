
def get_shifted_char(char, direction):
    if direction == 'L':
        return chr(ord(char) - 1)
    else:
        return chr(ord(char) + 1)

def solve(sequence):
    direction = sequence[0]
    sequence = sequence[1:]
    result = ''
    for i in range(len(sequence)):
        result += get_shifted_char(sequence[i], direction)
    return result

def main():
    input_sequence = input()
    print(solve(input_sequence))

if __name__ == '__main__':
    main()

