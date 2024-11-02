def factorial(n):
    result = 1
    if n == 0: 
        return 1
    if n == 1: 
        return 1
    for i in range(1, n + 1):
        result *= i
    return result

expected_result = 6
result = factorial(3)

assert result == expected_result, f"Wynik oczekiwany:\n{expected_result}\nWynik otrzymany:\n{result}"

print(result)
