class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count_lists = 0
        self.count_list = 0
        self.stop = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stop:
            while self.count_lists < len(self.list_of_list):
                if self.count_list < len(self.list_of_list[self.count_lists]):
                    item = self.list_of_list[self.count_lists][self.count_list]
                    self.count_list += 1
                    return item
                self.count_lists += 1
                self.count_list = 0
        raise StopIteration
    
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result_list = [item for item in FlatIterator(list_of_list)]
    print(result_list)
    test_1()
