def countingZeros(the_integer):
    converted_string = str(the_integer)
    zero_count = converted_string.count('0')
    return zero_count

long_int = 12203900049584730283710
result = countingZeros(long_int)

print(f"Wprowadzona liczba: {long_int}\nIlosc zer: {result}")
#output: (...) Ilosc zer: 6

