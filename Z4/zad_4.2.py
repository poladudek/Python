def make_ruler(n): 
    measure_drawing = ""
    measure_count = "" 
    for int_num in range(n + 1):
        measure_drawing += "|...."
        if int_num < 10:
            measure_count += f"{int_num}    "
        else:
            measure_count += f"{int_num}   "
    measure_drawing += "|"
    measure_full = measure_drawing + "\n" + measure_count
    return measure_full

def make_grid(rows, cols):
    full_rec = ""
    full_rec += "+---" * cols + "+\n"
    for _ in range(rows):
        full_rec += "|   " * cols + "|\n"
        full_rec += "+---" * cols + "+\n"
    return full_rec


expected_ruler_1 = "|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   "
expected_grid_1 = "+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+\n|   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+\n"

ruler_1 = make_ruler(15)
grid_1 = make_grid(5, 7)

assert ruler_1 == expected_ruler_1, f"Wynik oczekiwany:\n{expected_ruler_1}\nWynik otrzymany:\n{ruler_1}"
assert grid_1 == expected_grid_1, f"Wynik oczekiwany:\n{expected_grid_1}\nWynik otrzymany:\n{grid_1}"

print(ruler_1)
print(grid_1)
