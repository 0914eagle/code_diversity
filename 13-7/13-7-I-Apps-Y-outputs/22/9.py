
def stable_sort(my_list, *sort_attrs):
    # Convert the list to a list of tuples, with each tuple containing the value of each sort attribute
    sorted_list = [(getattr(x, attr) for x in my_list) for attr in sort_attrs]
    # Zip the sorted lists into a single list of tuples
    sorted_list = list(zip(*sorted_list))
    # Sort the list of tuples
    sorted_list.sort(key=lambda x: (x[0], x[1]))
    # Convert the list of tuples back to a list of dictionaries
    sorted_list = [dict(zip(sort_attrs, x)) for x in sorted_list]
    return sorted_list

