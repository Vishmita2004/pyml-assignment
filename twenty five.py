
def copy_file(source_file, destination_file):
    try:
        
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            
            destination.write(source.read())
        print(f"Contents of '{source_file}' have been successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: One of the files '{source_file}' or '{destination_file}' was not found.")


def main():
    
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    
   
    copy_file(source_file, destination_file)


main()
