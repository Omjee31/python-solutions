def fibo(n):
    """
    This function returns the nth Fibonacci number using recursion.
    """

    # Base case:
    # If n is 0 or 1, return n itself
    if n <= 1:
        return n

    # Recursive case:
    # Sum of the previous two Fibonacci numbers
    return fibo(n - 1) + fibo(n - 2)


# Taking input from the user
num = int(input("Enter Number: "))

# Calling the function and storing the result
result = fibo(num)

# Printing the Fibonacci number
print("Fibonacci number:", result)
)
                
