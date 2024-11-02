def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    a = 0
    b = 1
    result = 0
    for i in range(2, n + 1):
        result = a + b
        a = b
        b = result
    return result

expected_result = 3
result = fibonacci(4)

assert result == expected_result, f"Wynik oczekiwany:\n{expected_result}\nWynik otrzymany:\n{result}"

print(result)
