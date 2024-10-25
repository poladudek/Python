def WithoutThreeMultiples(n):
    for num in range(n):
        if num % 3 != 0:
            print(num)

n = 30
WithoutThreeMultiples(n)