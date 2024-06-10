
def get_result(x, y, z):
    # Calculate the number of upvotes and downvotes
    upvotes = x
    downvotes = y
    for i in range(z):
        upvotes += 1
        downvotes += 1
    
    # Check if the result is uncertain
    if upvotes > downvotes:
        return "+"
    elif upvotes < downvotes:
        return "-"
    else:
        return "0"

def main():
    x, y, z = map(int, input().split())
    print(get_result(x, y, z))

if __name__ == '__main__':
    main()

