
def get_max_apps(n, c, download_sizes, storage_sizes):
    # Initialize a list to store the selected apps
    selected_apps = []
    # Initialize a variable to store the total disk space used
    total_disk_space = 0
    # Iterate through the apps
    for i in range(n):
        # Check if the current app can be installed
        if total_disk_space + max(download_sizes[i], storage_sizes[i]) <= c:
            # If it can be installed, add it to the selected apps list
            selected_apps.append(i + 1)
            # Update the total disk space used
            total_disk_space += max(download_sizes[i], storage_sizes[i])
    # Return the selected apps list
    return selected_apps

def get_installation_order(n, selected_apps):
    # Initialize a list to store the installation order
    installation_order = []
    # Iterate through the selected apps
    for app in selected_apps:
        # Add the app to the installation order list
        installation_order.append(app)
    # Return the installation order list
    return installation_order

if __name__ == '__main__':
    # Read the input
    n, c = map(int, input().split())
    download_sizes = []
    storage_sizes = []
    for i in range(n):
        d, s = map(int, input().split())
        download_sizes.append(d)
        storage_sizes.append(s)
    # Call the get_max_apps function
    selected_apps = get_max_apps(n, c, download_sizes, storage_sizes)
    # Call the get_installation_order function
    installation_order = get_installation_order(n, selected_apps)
    # Print the maximum number of apps that can be installed
    print(len(selected_apps))
    # Print the installation order
    print(*installation_order)

