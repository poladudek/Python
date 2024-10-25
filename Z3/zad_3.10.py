def makingDictionary1():
    rom_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return rom_to_int

def makingDictionary2():
    rom = "IVXLCDM"
    arabic_int = [1, 5, 10, 50, 100, 500, 1000]
    rom_to_int = {} 
    for i in range(0, len(rom)):
        rom_to_int[rom[i]] = arabic_int[i]
    return rom_to_int

def makingDictionary3():
    rom = [
        ('I', 1), 
        ('V', 5), 
        ('X', 10), 
        ('L', 50), 
        ('C', 100), 
        ('D', 500), 
        ('M', 1000)
    ]
    rom_to_int = dict(rom)
    return rom_to_int

def roman2int(rom):
    rom_to_int = makingDictionary1()
    arabic_int = 0
    previous_num = 0

    for num in reversed(rom): 
        current_num = rom_to_int.get(num) # get() pobiera wartosc ze slownika
        if (current_num < previous_num):
            arabic_int -= current_num
        else:
            arabic_int += current_num
        previous_num = current_num 
    return arabic_int

result = roman2int("MCMXCIV")
print(result) #output: 1994
