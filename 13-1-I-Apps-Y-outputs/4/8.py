
import re

def solve(n, packages):
    pink_packages = []
    for package in packages:
        if re.search("pink|rose", package, re.IGNORECASE):
            pink_packages.append(package)
    return len(pink_packages)

