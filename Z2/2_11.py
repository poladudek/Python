def addingUnderlines(word):
    with_underlines = '_'.join(word)
    return with_underlines

word = "Apple"
result = addingUnderlines(word)

print(f"Wprowadzone slowo: {word}\nSlowo ze znakami oddzielonymi znakiem podkreslenia: {result}")
# output: (...) Slowo ze znakami oddzielonymi znakiem podkreslenia: A_p_p_l_e
