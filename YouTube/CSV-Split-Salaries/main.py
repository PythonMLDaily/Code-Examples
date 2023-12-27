import csv

chunk = []
row_count = 0
file_number = 1
header = ''

with open('salaries.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if header == '':
            header = row
            continue

        chunk.append(row)
        row_count += 1
        if row_count >= 50000:
            with open(f'salaries-{file_number}.csv', 'w') as new_file:
                writer = csv.writer(new_file)
                writer.writerow(header)
                writer.writerows(chunk)
            chunk = []
            file_number += 1
            row_count = 0

    if chunk:
        with open(f'salaries-{file_number}.csv', 'w') as new_file:
            writer = csv.writer(new_file)
            writer.writerow(header)
            writer.writerows(chunk)

