
def read_and_print_lines():
    lines = []

    
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)


    print("\nThe lines you entered are:")
    for line in lines:
        print(line)


read_and_print_lines()
