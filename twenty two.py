
def find_min_max(numbers):
    if not numbers:  
        return None, None
    else:
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum


def main():
  
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    
    
    numbers = [int(num) for num in numbers]

    
    min_value, max_value = find_min_max(numbers)

   
    if min_value is not None and max_value is not None:
        print("Minimum value:", min_value)
        print("Maximum value:", max_value)
    else:
        print("The list is empty.")


main()
