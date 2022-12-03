nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(some_list):
    for i in some_list:
        for k in i:
            yield k


for item in flat_generator(nested_list):
    print(item)
