
def handle_changes(requests):
    # Initialize a dictionary to store the mapping of old handles to new handles
    handle_map = {}

    # Iterate over the requests and update the handle map
    for request in requests:
        old_handle, new_handle = request.split()
        if old_handle not in handle_map:
            handle_map[old_handle] = new_handle
        else:
            handle_map[old_handle] = handle_map[old_handle]

    # Find the number of unique users who changed their handles
    n = len(set(handle_map.values()))

    # Print the mapping of old handles to new handles
    for old_handle, new_handle in handle_map.items():
        print(old_handle, new_handle)

    return n

