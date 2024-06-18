# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Initialize sum to store the total sum of digits
    total_sum = 0
    
    # Convert the number to its absolute value to handle negative numbers
    number = abs(number)
    
    # Iterate through each digit in the number
    while number > 0:
        # Extract the last digit of the number
        digit = number % 10
        # Add the digit to the total sum
        total_sum += digit
        # Remove the last digit from the number
        number //= 10
    
    return total_sum

# Main function
def main():
    # Taking input from the user
    number = int(input("Enter a number: "))
    
    # Calculating the sum of digits
    result = sum_of_digits(number)
    
    # Printing the result
    print("The sum of the digits of the given number is:", result)

# Calling the main function
main()

