def calculate_structure_sum(*args):
    data_dump = [args]
    summa = 0
    while data_dump:
        el = data_dump.pop(0)
        if isinstance(el, (tuple, list, set)):
            for i in el:
                data_dump.append(i)
        elif isinstance(el, (int, float)):
            summa += el
        elif isinstance(el, (str)):
            summa += len(el)
        elif isinstance(el, (dict)):
            summa += sum(value for value in el.values())
            for key in list(el.keys()):
                summa += len(key)

    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
