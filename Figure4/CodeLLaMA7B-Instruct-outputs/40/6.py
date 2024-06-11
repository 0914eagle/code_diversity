


def triples_sum_to_zero(l: list):
    

    # check if the list has three or more elements
    if len(l) < 3:
        return False

    # create a set to store the unique elements of the list
    unique_elements = set()

    # loop through the list and check if any three elements sum to zero
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    # if there are three distinct elements that sum to zero, return True
                    if len(unique_elements) == 2:
                        return True
                    # add the current elements to the set
                    unique_elements.add(l[i])
                    unique_elements.add(l[j])
                    unique_elements.add(l[k])

    # if no three distinct elements sum to zero, return False
    return False


