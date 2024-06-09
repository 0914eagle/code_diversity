
def is_achievable(costs, increases, X):
    # Check if the total cost is within reach
    if sum(costs) <= X:
        return True
    
    # Sort the books by cost in descending order
    sorted_books = sorted(enumerate(costs), key=lambda x: x[1], reverse=True)
    
    # Initialize the understanding levels and total cost
    levels = [0] * len(costs)
    total_cost = 0
    
    # Loop through the books and buy the ones that will increase the understanding levels the most
    for i, (book_idx, book_cost) in enumerate(sorted_books):
        # Check if buying this book will bring the understanding levels above X
        if sum(levels) + sum(increases[book_idx]) >= X:
            return True
        
        # Buy the book and update the understanding levels and total cost
        levels = [level + increase for level, increase in zip(levels, increases[book_idx])]
        total_cost += book_cost
    
    # If we reach this point, it means we couldn't buy any more books to bring the understanding levels above X
    return False

def find_min_cost(costs, increases, X):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Loop through all possible combinations of books to buy
    for book_combination in itertools.combinations(range(len(costs)), X):
        # Check if the combination is achievable
        if is_achievable(costs, increases, X):
            # If it is, calculate the total cost and update the minimum cost if necessary
            total_cost = sum(costs[book_idx] for book_idx in book_combination)
            if total_cost < min_cost:
                min_cost = total_cost
    
    # Return the minimum cost
    return min_cost

if __name__ == '__main__':
    costs = [10, 20, 30, 40, 50]
    increases = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    X = 30
    print(find_min_cost(costs, increases, X))

