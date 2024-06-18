
def convert_to_title_case(input_string):
    return input_string.title()


def main():
    
    input_string = input("Enter a string: ")

    
    title_case_string = convert_to_title_case(input_string)

    print("Title case string:", title_case_string)


main()
