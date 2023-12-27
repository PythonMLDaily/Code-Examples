import csv


def write_to_file(filename, data_chunk, data_header=None):
    with open(filename, 'w') as new_file:
        writer = csv.writer(new_file)
        if data_header:
            writer.writerow(data_header)
        writer.writerows(data_chunk)


def split_csv(filename, row_count=50000):
    chunk = []
    row_number = 0
    file_number = 1
    header = ''
    original_filename, extension = filename.split('.')

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if header == '':
                header = row
                continue

            chunk.append(row)
            row_number += 1
            if row_number >= row_count:
                write_to_file(f'new-{original_filename}-{file_number}.{extension}', chunk, header)
                chunk = []
                file_number += 1
                row_number = 0

        if chunk:
            write_to_file(f'new-{original_filename}-{file_number}.{extension}', chunk, header)


split_csv('salaries.csv', 10000)