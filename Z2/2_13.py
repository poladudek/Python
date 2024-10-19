def countingWordsLen(line):
    words_only = line.split()
    word_len_count = sum(len(each_word) for each_word in words_only)
    return word_len_count

line = "The length of all words should be 29"
print(f"Wprowadzony tekst: {line}")
result = countingWordsLen(line)
print(f"Calkowita dlugosc wszystkich wyrazow: {result}") #output: Calkowita dlugosc wszystkich wyrazow: 29
