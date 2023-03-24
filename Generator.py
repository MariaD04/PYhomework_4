import types

def flat_generator(list_of_list):
    count_lists = 0
    while count_lists < len(list_of_list):
        for item in list_of_list[count_lists]:
            yield item
        count_lists += 1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result_list = [item for item in flat_generator(list_of_list)]
    print(result_list)
    test_2()