# Conversor de numeros romanos en python
# I	1	|   V	5	|   X	10
# L	50	|   C	100	|   D	500 | M	1000

# valoresNumerosRomanos = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

valores = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def romano_a_arabigo(numRomano):  # (XCIX) -> 99
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:
        if letra == ultimoCaracter:
            numRepes += 1
        else:
            numRepes = 1
        if numRepes > 3:
            return 0

        if letra in valores:
            if ultimoCaracter == '':
                numArabigo += valores.get(letra)
                pass
            elif valores.get(letra) <= valores.get(ultimoCaracter):
                numArabigo += valores.get(letra)
            else:
                numArabigo -= valores.get(letra)
        else:
            return 0

        ultimoCaracter = letra

    return numArabigo


ver = print(romano_a_arabigo('XCIX'))
