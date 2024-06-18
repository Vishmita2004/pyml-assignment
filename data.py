import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# Specify the name of the CSV file
file_name = 'example.csv'

# Open the CSV file in write mode
with open(file_name, 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write data to the CSV file
    writer.writerows(data)

print(f"CSV file '{file_name}' has been created successfully.")
