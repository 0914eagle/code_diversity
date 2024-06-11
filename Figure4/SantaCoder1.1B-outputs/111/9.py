def histogram(test):
    
    # Your code here
    # return {}
    if not test:
        return {}
    else:
        return collections.Counter(test)

# Test cases:
print(histogram('a b c'))
print(histogram('a b b a'))
print(