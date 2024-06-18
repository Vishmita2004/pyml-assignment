
def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum


def main():
    
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    
    
    numbers = [int(num) for num in numbers]
    
    
    total_sum = calculate_sum(numbers)


    print("Sum of the numbers:", total_sum)


main()
