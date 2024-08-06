# Function to generate Fibonacci series
def fibonacci_series(n):
    fibonacci_sequence = [0, 1]
    
    for i in range(2, n):
        next_element = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_element)
    
    return fibonacci_sequence

# Taking input from the user
n = int(input("Enter the number of elements you want in the Fibonacci series: "))

# Displaying the Fibonacci series
print(f"Fibonacci series with {n} elements:")
print(fibonacci_series(n))
