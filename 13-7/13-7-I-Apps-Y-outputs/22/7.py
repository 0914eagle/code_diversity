
def stable_sort(my_list, *sort_keys):
    # Convert the list to a list of tuples, where each tuple contains the sort keys and the original value
    my_list = [(getattr(x, key) for key in sort_keys) + (x,) for x in my_list]
    # Sort the list stably using the sort keys
    my_list.sort(key=lambda x: x[:len(sort_keys)])
    # Return the sorted list of original values
    return [x[-1] for x in my_list]

