import csv

def calculate_average(filename, column_name):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        values = [float(row[column_name]) for row in reader if row[column_name]]
    return sum(values) / len(values) if values else 0

filename = "data.csv"
column_name = "column_name"
average = calculate_average(filename, column_name)
print(f"Average: {average}")
