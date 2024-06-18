
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = factorial(num)
        print(f"The factorial of {num} is: {fact}")

main()
