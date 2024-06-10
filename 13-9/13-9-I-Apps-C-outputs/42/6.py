
def get_sequence(oranges, apples):
    if oranges < 1 or apples < 1:
        return "Impossible"
    
    sequence = []
    while oranges > 0 and apples > 0:
        if oranges > apples:
            sequence.append("A")
            oranges -= 1
        else:
            sequence.append("B")
            apples -= 1
    
    return "".join(sequence)

def main():
    oranges, apples = map(int, input().split())
    print(get_sequence(oranges, apples))

if __name__ == '__main__':
    main()

