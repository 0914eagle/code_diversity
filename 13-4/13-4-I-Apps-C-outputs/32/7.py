
def get_package_order(packages):
    # Initialize an empty order list
    order = []

    # Loop through the packages
    for package in packages:
        # Check if the package is already in the order list
        if package not in order:
            # Check if the package has any dependencies
            if package.dependencies:
                # Check if all the dependencies are in the order list
                if all(dep in order for dep in package.dependencies):
                    # If all dependencies are in the order list, add the package to the order list
                    order.append(package)
                else:
                    # If not all dependencies are in the order list, return "cannot be ordered"
                    return "cannot be ordered"
            else:
                # If the package has no dependencies, add it to the order list
                order.append(package)

    # Return the order list
    return order

