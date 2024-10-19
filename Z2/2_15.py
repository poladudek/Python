def creatingString(L):
    to_str_type = (str(num) for num in L)
    the_string = ''.join(to_str_type)
    return the_string

L = [1, 2, 3, 4, 5]
result = creatingString(L)
print(f"Wprowadzona lista: {L}\nUtworzony napis: {result}")
#output: Wprowadzona lista: [1, 2, 3, 4, 5]
#output: Utworzony napis: 12345

