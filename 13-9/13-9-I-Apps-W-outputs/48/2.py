
def get_result(x, y, z):
    # Calculate the number of upvotes and downvotes
    upvotes = x
    downvotes = y
    for i in range(z):
        upvotes += 1
        downvotes += 1
    
    # Check if the number of upvotes is greater than the number of downvotes
    if upvotes > downvotes:
        return "+"
    
    # Check if the number of downvotes is greater than the number of upvotes
    elif downvotes > upvotes:
        return "-"
    
    # If the number of upvotes and downvotes are equal, return 0
    else:
        return "0"

def main():
    x, y, z = map(int, input().split())
    print(get_result(x, y, z))

if __name__ == '__main__':
    main()

