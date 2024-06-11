def unique_digits(x):
    
    # YOUR CODE HERE
    return [i for i in x if not any(int(j)%2==0 for j in str(i))]


# + deletable=false editable=false nbgrader={"cell_type": "code", "