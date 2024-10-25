def drawingMeasure(size):
    measure_drawing = ""
    measure_count = "" 
    for int_num in range(size + 1):
        measure_drawing += "|...."
        if int_num < 10:
            measure_count += f"{int_num}    "
        else:
            measure_count += f"{int_num}   "
    measure_drawing += "|"
    measure_full = measure_drawing + "\n" + measure_count
    return measure_full

size = input("Wprowadź długość miarki: ")
size = int(size)
result = drawingMeasure(size)
print(result)
