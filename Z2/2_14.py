def longestWord(line):
    longest_word = None
    word_list = line.split()
    longest_word = max(word_list, key=len)
    size = len(longest_word)
    return longest_word, size

line = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
wrd, size = longestWord(line)

print(f"Wprowadzony tekst: {line}\nNajdluzszy wyraz: {wrd}\nDlugosc najdluzszego wyrazu: {size}")
#output: (...)Najdluzszy wyraz: consectetur
#output: Dlugosc najdluzszego wyrazu: 11
