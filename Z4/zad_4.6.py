def sum_seq(sequence):
    if not sequence:
        return 0
    if isinstance(sequence[0], (list, tuple)):
        return sum_seq(sequence[0]) + sum_seq(sequence[1:])
    return sequence[0] + sum_seq(sequence[1:])

sequence = [(1, 2), 3, 4, 5, [6, 7, 8]] 
expected_result = 36
result = sum_seq(sequence)

assert result == expected_result, f"Wynik oczekiwany:\n{expected_result}\nWynik otrzymany:\n{result}"

print(result)
