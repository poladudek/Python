def sum_seq(sequence):
    if not sequence:
        return 0
    if isinstance(sequence[0], (list, tuple)):
        return sum_seq(sequence[0]) + sum_seq(sequence[1:])
    return sequence[0] + sum_seq(sequence[1:])

sequence = [(1, 2), 3, 4, 5, [6, 7, 8]] 
result = sum_seq(sequence)
print(result)
