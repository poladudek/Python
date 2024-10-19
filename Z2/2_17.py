def sortingAlphabetically(line):
    word_list = line.split()
    word_list = sorted(word_list)
    line = ' '.join(word_list)
    return line

def sortingByLength(line):
    word_list = line.split()
    word_list = sorted(word_list, key=len)
    line = ' '.join(word_list)
    return line

line = "lorem ipsum dolor sit amet consectetur adipiscing elit"
result_alpha = sortingAlphabetically(line)
result_len = sortingByLength(line)

print(f"Wprowadzony tekst: {line}\nTekst po sortowaniu alfabetycznym: {result_alpha}\nTekst po sortowaniu po dlugosci wyrazow: {result_len}")
#output: (...) Tekst po sortowaniu alfabetycznym: adipiscing amet consectetur dolor elit ipsum lorem sit
#outpit: Tekst po sortowaniu po dlugosci wyrazow: sit amet elit lorem ipsum dolor adipiscing consectetur
