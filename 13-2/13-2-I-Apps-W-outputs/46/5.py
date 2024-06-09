
def f1(t, pieces):
    # convert the pieces to a list of integers
    pieces = [int(piece) for piece in pieces]
    
    # count the number of instances of t in the pieces
    count = 0
    for piece in pieces:
        if piece == t:
            count += 1
    
    return count

def f2(t, pieces):
    # convert the pieces to a list of integers
    pieces = [int(piece) for piece in pieces]
    
    # count the number of instances of t in the pieces
    count = 0
    for piece in pieces:
        if piece == t:
            count += 1
    
    return count

if __name__ == '__main__':
    t = int(input())
    pieces = input().split()
    print(f1(t, pieces))
    print(f2(t, pieces))

