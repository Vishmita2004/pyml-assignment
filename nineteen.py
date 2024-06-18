import string


def remove_punctuation(input_string):
    
    punctuation_set = set(string.punctuation)
    
    
    cleaned_string = ''.join(char for char in input_string if char not in punctuation_set)
    
    return cleaned_string


def main():
    
    input_string = input("Enter a string with punctuation: ")

    
    cleaned_string = remove_punctuation(input_string)

    
    print("String after removing punctuation:", cleaned_string)


main()
