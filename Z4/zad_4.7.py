def flatten(sequence):
    flattened_list = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            flattened_list.extend(flatten(element)) #extend bo operujemy na listach/krotkach
        else:
            flattened_list.append(element)
    return flattened_list

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
result = flatten(seq)
print(result)
