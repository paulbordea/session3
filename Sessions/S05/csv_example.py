import csv

data = []
with open('csv_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        if not row.__contains__('birth_year'):
            data.append(row)


# for entry in data[1:]:
#     entry[2] = str(int(entry[2]) - 2)


with open('csv_data.csv', mode="a") as csv_file_write:
    csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerows(data)

