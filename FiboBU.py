def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Initialize the first two Fibonacci numbers
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    # Calculate Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Example usage
n = 10
result = fibonacci(n)
print(f"Fibonacci({n}) = {result}")
