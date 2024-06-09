
def count_equal_integers(numbers):
    # Initialize a dictionary to store the count of each integer
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Iterate through the dictionary and count the number of pairs with equal integers
    equal_count = 0
    for num, freq in count.items():
        if freq >= 2:
            equal_count += freq * (freq - 1) // 2
    
    return equal_count

def solve(numbers):
    n = len(numbers)
    # Initialize an array to store the answers for each k
    answers = [0] * n
    for k in range(n):
        # Find the number of equal integers in the remaining numbers
        equal_count = count_equal_integers(numbers[:k] + numbers[k+1:])
        answers[k] = equal_count
    
    return answers

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    answers = solve(numbers)
    for answer in answers:
        print(answer)

