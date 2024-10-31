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

ruler_1 = make_ruler(15)
grid_1 = make_grid(5, 7)

print(ruler_1)
print(grid_1)
