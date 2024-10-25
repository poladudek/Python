def findingSimilarities(seq_1, seq_2):
    L = []
    str_1 = str(seq_1)
    str_2 = str(seq_2)

    unique_str1 = set(str_1)
    unique_str2 = set(str_2)

    for element1 in unique_str1:
        for element2 in unique_str2:
            if element1 == element2:
                L.append(element1)

    all_unique_elements = unique_str1.union(unique_str2)
    return L, list(all_unique_elements)


seq_1 = 1234
seq_2 = 3456
result_1, result_2 = findingSimilarities(seq_1, seq_2)
seq_3 = "abcddd"
seq_4 = "defg"
result_3, result_4 = findingSimilarities(seq_3, seq_4)

print(f"Sekwencja pierwsza (liczby): {seq_1}, {seq_2}")
print(f"Sekwencja druga (litery): {seq_3}, {seq_4}\n")

print("Sekwencja pierwsza: Lista elementow wystepujacych jednoczesnie w obu sekwencjach (bez powtorzen):", result_1, "Lista wszystkich elementow z obu sekwencji (bez powtorzen):", result_2)
print("Sekwencja druga: Lista elementow wystepujacych jednoczesnie w obu sekwencjach (bez powtorzen):", result_3, "Lista wszystkich elementow z obu sekwencji (bez powtorzen):", result_4)
