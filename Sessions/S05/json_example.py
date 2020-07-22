import json

with open('json_data.json') as read_file:
    data = json.load(read_file)

print(data)

# for entry in data[1:]:
#     entry[2] = str(int(entry[2]) - 2)


# with open('json_data.json', mode="a") as csv_file_write:
#     csv_writer = csv.writer(csv_file_write, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     csv_writer.writerows(data)

