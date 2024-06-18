
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        
        celsius = float(input("Enter temperature in Celsius: "))
        
        
        fahrenheit = celsius_to_fahrenheit(celsius)
        
        
        print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
    elif choice == 2:
       
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        
        celsius = fahrenheit_to_celsius(fahrenheit)
        
       
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")
    else:
        print("Invalid choice! Please enter 1 or 2.")


main()
