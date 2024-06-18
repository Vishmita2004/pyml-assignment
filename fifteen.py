import csv

def read_csv_file(file_name):
    try:
        
        with open(file_name, 'r', newline='') as file:
            
            reader = csv.reader(file)
            
            
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")


def main():
    
    file_name = 'example.csv'  

    read_csv_file(file_name)


main()
