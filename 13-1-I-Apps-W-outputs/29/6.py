
def handle_change_requests(requests):
    # Initialize a dictionary to store the mapping of old handles to new handles
    handle_map = {}

    # Iterate over the requests and update the handle map
    for request in requests:
        old_handle, new_handle = request.split()
        if old_handle not in handle_map:
            handle_map[old_handle] = new_handle
        else:
            handle_map[old_handle] = handle_map[old_handle]

    # Find the unique users who changed their handles
    unique_users = set(handle_map.keys())

    # Print the number of unique users
    print(len(unique_users))

    # Print the mapping of old handles to new handles for each unique user
    for user in unique_users:
        print(f"{user} {handle_map[user]}")

