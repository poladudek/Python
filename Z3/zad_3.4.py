def MakingExps():
    while True:
        x = input("""Wprowadz liczbe lub wpisz "stop" by przerwac program:   """)
        if x == 'stop':
            break
        try:
            x = float(x)
            print("Wprowadzona liczba: {}, jej trzecia potęga: {}".format(x, x**3))
        except ValueError:
            print("""Podaj prawidlowa liczbe lub wpisz "stop" aby przerwac program """)

MakingExps()
