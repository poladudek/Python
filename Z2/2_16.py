def replacingGvr(line):
    line = line.replace("GvR", "Guido van Rossum")
    return line

line = "Neque porro quisquam est GvR qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
result = replacingGvr(line)
print(f"Wprowadzony tekst: {line}\nTekst po zastapieniu GvR na Guido van Rossum: {result} ")