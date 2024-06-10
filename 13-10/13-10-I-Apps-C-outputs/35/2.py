
def get_initial_fruits(x, y):
    return x, y

def get_sequence_of_cards(x, y):
    if x == 0 and y == 0:
        return "Impossible"
    
    sequence = []
    while x > 0 or y > 0:
        if x > 0:
            sequence.append("A")
            x -= 1
        if y > 0:
            sequence.append("B")
            y -= 1
    
    return "".join(sequence)

def main():
    x, y = map(int, input().split())
    print(get_sequence_of_cards(x, y))

if __name__ == '__main__':
    main()

