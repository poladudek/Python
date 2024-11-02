def odwracanieIteracyjne(L, left, right):
    a = left
    b = right
    while a < b:
        helper = L[a]
        L[a] = L[b]
        L[b] = helper
        a += 1
        b -= 1
    return L

def odwracanieRekurencyjne(L, left, right):
    if left >= right:
        return L
    helper = L[left]
    L[left] = L[right]
    L[right] = helper
    return odwracanieRekurencyjne(L, left + 1, right - 1)


L_iteracyjne = [1, 2, 3, 4, 5, 6]
expected_result_iteracyjne = [1, 5, 4, 3, 2, 6]
result_iteracyjne = odwracanieIteracyjne(L_iteracyjne, 1, 4)
assert result_iteracyjne == expected_result_iteracyjne, f"Wynik oczekiwany:\n{expected_result_iteracyjne}\nWynik otrzymany:\n{result_iteracyjne}"

print(result_iteracyjne)

L_rekurencyjne = [1, 2, 3, 4, 5, 6, 7]
expected_result_rekurencyjne = [1, 2, 3, 7, 6, 5, 4]
result_rekurencyjne = odwracanieRekurencyjne(L_rekurencyjne, 3, 5)
assert result_rekurencyjne == expected_result_rekurencyjne, f"Wynik oczekiwany:\n{expected_result_rekurencyjne}\nWynik otrzymany:\n{result_rekurencyjne}"

print(result_rekurencyjne)
