import csv


def read_dataset(China):
    with open(China, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def count_rows(China):
    with open(China, 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
    return row_count


def filter_var1_greater_than_zero(China):
    with open(China, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['Var1']) > 0:
                print(row)


def calculate_average_var5(China):
    with open(China, 'r') as file:
        reader = csv.DictReader(file)
        total_var5 = 0
        row_count = 0
        for row in reader:
            total_var5 += int(row['Var5'])
            row_count += 1
        average_var5 = total_var5 / row_count
    return average_var5


dataset_file = 'China.csv'
read_dataset(dataset_file)
row_count = count_rows(dataset_file)
print(f'Total number of rows: {row_count}')
filter_var1_greater_than_zero(dataset_file)
average_var5 = calculate_average_var5(dataset_file)
print(f'Average value of Var5: {average_var5}')
