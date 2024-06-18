
def are_anagrams(string1, string2):
    
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    
    return sorted(string1) == sorted(string2)


def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if are_anagrams(string1, string2):
        print("The two strings are anagrams of each other.")
    else:
        print("The two strings are not anagrams of each other.")

main()
