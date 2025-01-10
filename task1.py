

def fibonacci(n):
    # Base cases for the first two Fibonacci numbers
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]
    
    # Generate Fibonacci numbers up to n terms
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    
    return fib_series

# Example usage:
n = 10  # The number of Fibonacci numbers to generate
print(fibonacci(n))
