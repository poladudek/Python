def countingWords(line):
    words_only = line.split()
    count = len(words_only)
    return count

line = """The
output
should\t\t be 
five\n"""
result = countingWords(line)

print("Wprowadzony tekst: {}\nIlosc slow: {}".format(line, result)) 
#output: (...)Ilosc slow: 5