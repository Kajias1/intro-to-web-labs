import csv

table_file_name = 'people.csv'

data = [
    ["Name",    "Age",  "City"          ],
    ["Alice",   "30",   "New York"      ],
    ["Bob",     "25",   "Los Angeles"   ],
    ["Charlie", "35",   "Chicago"       ]
]

with open(table_file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Data has been written to {table_file_name}")

print("Reading data from the CSV file:")
with open(table_file_name, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)