
def check_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    ends_with_suffix = string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix


def main():
    
    string = input("Enter a string: ")
    prefix = input("Enter a prefix: ")
    suffix = input("Enter a suffix: ")

    
    starts_with_prefix, ends_with_suffix = check_prefix_suffix(string, prefix, suffix)

   
    if starts_with_prefix:
        print(f"The string '{string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{string}' does not start with the prefix '{prefix}'.")

    if ends_with_suffix:
        print(f"The string '{string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{string}' does not end with the suffix '{suffix}'.")


main()
