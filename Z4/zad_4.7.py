def flatten(sequence):
    flattened_list = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            flattened_list.extend(flatten(element))
        else:
            flattened_list.append(element)
    return flattened_list

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = flatten(seq)

assert result == expected_result, f"Wynik oczekiwany:\n{expected_result}\nWynik otrzymany:\n{result}"

print(result)
