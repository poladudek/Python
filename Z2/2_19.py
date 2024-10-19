def threeNumWords(L):
    the_list = [str(num).zfill(3) for num in L]
    finished_string = ' '.join(the_list)
    return finished_string

L = [1, 123, 54, 678, 4, 78]
result = threeNumWords(L)

print(f"Wprowadzona lista: {L}\nUtworzony napis: {result}")
#output: Wprowadzona lista: [1, 123, 54, 678, 4, 78]
#output: Utworzony napis: 001 123 054 678 004 078

