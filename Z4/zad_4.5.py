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

L = [1, 2, 3, 4, 5, 6]
result = odwracanieIteracyjne(L, 1, 4)
print(result)

L = [1, 2, 3, 4, 5, 6, 7]
result = odwracanieRekurencyjne(L, 3, 5)
print(result)
