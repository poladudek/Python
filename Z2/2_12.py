def firstCharacters(line):
    before = list(line)
    after = []
    after.append(before[0])
    for i in range(1, len(before)-1): 
        if before[i] == ' ':
            after.append(before[i+1])
    return ''.join(after)

def lastCharacters(line):
    before = list(line)
    after = []
    size = len(before)
    for i in range(0, size):
        if before[i] == ' ':
            after.append(before[i-1])
    after.append(before[size-1])
    return ''.join(after)

line = "Lorem ipsum dolor sit amet consectetur adipiscing"
resutlt_f = firstCharacters(line)
result_l = lastCharacters(line)

print(f"Wprowadzony tekst: {line}\nNapis stworzony z pierwszych liter wyrazow: {resutlt_f}\nNapis stworzony z ostatnich liter wyrazow: {result_l}")
#output: (...)Napis stworzony z pierwszych liter wyrazow: Lidsaca
#output: Napis stworzony z ostatnich liter wyrazow: mmrttrg

