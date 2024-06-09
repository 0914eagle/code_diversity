
def fibfib(n: int) -> int:
    
    if n < 3:
        return 0
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

