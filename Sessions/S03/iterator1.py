# my_list = [1, 2, 3]
# my_iter = iter(my_list)
#
# next(my_iter)
# next(my_iter)
# next(my_iter)
# next(my_iter)


# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
#
#
# for char in reverse('asd'):
#     print(char)


def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row


