nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.i = 0
        self.k = -1
        return self

    def __next__(self):
        self.k += 1
        if self.i < len(self.some_list) and self.k < len(self.some_list[self.i]):
            res = nested_list[self.i][self.k]
        elif self.i < len(self.some_list) - 1 and self.k == len(self.some_list[self.i]):
            self.i += 1
            self.k = 0
            res = self.some_list[self.i][self.k]
        else:
            raise StopIteration
        return res


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
