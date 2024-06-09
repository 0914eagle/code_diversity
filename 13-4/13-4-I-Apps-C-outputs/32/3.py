
def get_installation_order(packages):
    # Initialize a dictionary to store the dependencies of each package
    dependencies = {}

    # Iterate over the list of packages
    for package in packages:
        # Split the package into its name and dependencies
        name, deps = package.split(" ")

        # Add the package to the dictionary with its dependencies
        dependencies[name] = deps.split(", ")

    # Initialize a list to store the ordered packages
    ordered_packages = []

    # Iterate until all packages are installed
    while dependencies:
        # Find a package that has no dependencies
        for package, deps in dependencies.items():
            # If the package has no dependencies, add it to the ordered packages list
            if not deps:
                ordered_packages.append(package)
                break

        # Remove the package and its dependencies from the dictionary
        dependencies.pop(package)

        # Update the dependencies of the remaining packages
        for package, deps in dependencies.items():
            dependencies[package] = [dep for dep in deps if dep not in ordered_packages]

    return ordered_packages

