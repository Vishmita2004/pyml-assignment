
def calculate_age(birth_year):
    current_year = 2024  
    age = current_year - birth_year
    return age

def main():
    
    birth_year = int(input("Enter your birth year: "))
    
    age = calculate_age(birth_year)

    print("Your age is:", age)

main()
