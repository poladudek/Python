def findingSums(list):
    sums = []
    for element in L:
        helper = sum(element)
        sums.append(helper)
    return sums

L = [[],[4],(1,2),[3,4],(5,6,7)]
result = findingSums(L)
print(result)