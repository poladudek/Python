def WithoutThreeMultiples(n):
    full_str = ""
    for num in range(n):
        if num % 3 != 0:
            full_str += str(num) + " " 
    return full_str
    
n = 30
result = WithoutThreeMultiples(n)
print(result)
