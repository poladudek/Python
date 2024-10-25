def DrawingRectangle(a, b):
    full_rec = ""
    full_rec += "+---" * a + "+\n"
    for _ in range(b):
        full_rec += "|   " * a + "|\n"
        full_rec += "+---" * a + "+\n"
    return full_rec

result = DrawingRectangle(4, 2) #prostokat 4 x 2
print(result)
