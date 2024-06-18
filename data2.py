import csv


data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

file_name = 'example1.csv'


with open(file_name, 'w', newline='') as file:
   
    writer = csv.writer(file)
    
    
    writer.writerows(data)

print(f"CSV file '{file_name}' has been created successfully.")
