
def count_character_frequency(input_string):
    
    frequency_dict = {}

    
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict


def main():
    
    input_string = input("Enter a string: ")

    
    frequency_dict = count_character_frequency(input_string)

    
    print("Character frequencies:")
    for char, frequency in frequency_dict.items():
        print(f"'{char}': {frequency}")


main()
