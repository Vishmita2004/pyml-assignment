
def generate_fibonacci(n):
    fibonacci_sequence = []
    
    
    a, b = 0, 1
    
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence


def main():
    
    n = int(input("Enter the number of Fibonacci numbers to generate: "))

    
    fibonacci_sequence = generate_fibonacci(n)

    
    print("The first", n, "numbers in the Fibonacci sequence are:", fibonacci_sequence)


main()
