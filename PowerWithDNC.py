def power(a, b):
    # Base cases
    if b == 0:
        return 1
    if b == 1:
        return a
    
    # If b is even
    if b % 2 == 0:
        half = power(a, b // 2)  # Divide the problem
        return half * half  # Combine the results
    
    # If b is odd
    else:
        return a * power(a, b - 1)  # Reduce the problem

# Example usage
a = 2
b = 10
result = power(a, b)
print(f"{a}^{b} = {result}")
