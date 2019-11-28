# Conversor de numeros romanos en python
# I	1	|   V	5	|   X	10
# L	50	|   C	100	|   D	500 | M	1000

# valoresNumerosRomanos = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

valores = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
valores5 = {'D': 500, 'L': 50, 'V': 5}
simbolosoRdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def romano_a_arabigo(numRomano):  # (XCIX) -> 99
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:  # Recorrer numRomano de izquierda a derecha

        # Incrementamos el valor del numero arabigo con el valor del simbolo romano
        if letra in valores:
            numArabigo += valores.get(letra)
            if ultimoCaracter == '':
                pass
            elif valores.get(ultimoCaracter) > valores.get(letra):
                numRepes = 1
            elif valores.get(ultimoCaracter) == valores.get(letra):
                numRepes += 1

                if letra in valores5:
                    return 0

                if numRepes > 3:
                    return 0

            elif valores.get(ultimoCaracter) < valores.get(letra):
                if numRepes > 1:  # No permite repeticiones en las restas
                    return 0

                # No permite restas de valores de 5 (5,50,500)
                if ultimoCaracter in valores5:
                    return 0

                distancia = simbolosoRdenados.index(letra) - \
                    simbolosoRdenados.index(ultimoCaracter)
                if distancia > 2:
                    return 0

                numArabigo -= valores.get(ultimoCaracter)*2
                numRepes = 1
        else:   # Si el simbolo romano no es correcto devolvemos Error
            return 0

        ultimoCaracter = letra

    return numArabigo


ver = print(romano_a_arabigo('MMCMLXIX'))
