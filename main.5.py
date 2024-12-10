def split_list(lst):
    if len(lst) == 0:
        return [[], []]

    middle = len(lst) // 2 + len(lst) % 2

    return [lst[:middle], lst[middle:]]


print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))