
def f1(n, k, a):
    # Initialize variables
    line = a
    winner = 0
    count = 0
    
    # Play games until someone wins k games in a row
    while winner == 0:
        # Play game between first two players
        if line[0] > line[1]:
            line = line[1:] + line[:1]
            count += 1
        else:
            line = line[1:] + line[:1]
        
        # Check if someone has won k games in a row
        if count == k:
            winner = line[0]
    
    return winner

def f2(...):
    # Implement function f2 if needed
    pass

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))
    print(f1(n, k, a))

