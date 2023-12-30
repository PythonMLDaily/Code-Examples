import csv

new_csv_data = []
for year in range(2021, 2024):
    filename = f'salaries-{year}.csv'
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_csv_data.append([
                year,
                row['years_of_experience'] if 'years' not in row else row['years'],
                row['salary'],
            ])

with open('salaries-full.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'survey_year',
        'years_of_experience',
        'salary',
    ])
    writer.writerows(new_csv_data)
