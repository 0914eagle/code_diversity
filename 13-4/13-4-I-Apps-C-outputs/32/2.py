
import sys

def get_dependencies(package, dependencies):
    if package not in dependencies:
        return []
    return dependencies[package]

def get_install_order(packages):
    dependencies = {}
    for package in packages:
        dependencies[package] = get_dependencies(package, dependencies)
    
    install_order = []
    while dependencies:
        installed_packages = []
        for package, deps in dependencies.items():
            if not deps:
                installed_packages.append(package)
        if not installed_packages:
            return "cannot be ordered"
        install_order.extend(installed_packages)
        for package in installed_packages:
            del dependencies[package]
            for dep in get_dependencies(package, dependencies):
                dependencies[dep].remove(package)
    
    return " ".join(install_order)

if __name__ == "__main__":
    num_cases = int(input())
    for _ in range(num_cases):
        num_packages = int(input())
        packages = []
        for _ in range(num_packages):
            package, dependencies = input().split()
            packages.append(package)
            dependencies = dependencies.split()
            for dep in dependencies:
                if dep not in packages:
                    packages.append(dep)
        print(get_install_order(packages))
        print()

