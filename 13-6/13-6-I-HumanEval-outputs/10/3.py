
def fibfib(n: int) -> int:
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

