
def get_result(x, y, z):
    # Calculate the total number of upvotes and downvotes
    total_upvotes = x + z
    total_downvotes = y + z
    
    # Check if the result is uncertain
    if total_upvotes == total_downvotes:
        return "0"
    elif total_upvotes > total_downvotes:
        return "+"
    else:
        return "-"
    
def main():
    x, y, z = map(int, input().split())
    print(get_result(x, y, z))
    
if __name__ == '__main__':
    main()

