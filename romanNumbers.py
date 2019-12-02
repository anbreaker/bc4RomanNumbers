# Conversor de numeros romanos en python
# I	1	|   V	5	|   X	10
# L	50	|   C	100	|   D	500 | M	1000

# valoresNumerosRomanos = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

numArabigosToRoman = {'M': 1000, 'CM': 900, 'D': 500, 'C': 100,
                      'XC': 90, 'L': 50, 'X': 10, 'IX': 9, 'V': 5, 'I': 1}
valores = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
valores5 = {'D': 500, 'L': 50, 'V': 5}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def numMillares(numR):
    contarParentesis = 0
    numEntreParentesis = ''
    numPostParentesis = ''
    pAnterior = ''
    for p in numR:
        if p == ('(') or p == (')'):
            contarParentesis += 1
            if p == (')'):
                pAnterior = p
        elif pAnterior != (')'):
            numEntreParentesis += p
        elif pAnterior == (')'):
                numPostParentesis += p
    return contarParentesis, numEntreParentesis, numPostParentesis

# mandar numero fuera de los parentesis una especie de recursividad entre funciones


def romano_a_arabigo(numRomano):  # (XCIX) -> 99
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:  # Recorrer numRomano de izquierda a derecha

        if letra == '(':
            numMil = numMillares(numRomano)
            numAra = romano_a_arabigo(numMil[1])
            print(f'numParentesis -> {numMil[0]} \
                    \n numRomanoEntreParenteis -> {numMil[1]} \
                    \n numeroArabigoEntreParentesis -> {numAra} \
                    \n numPostParentesis -> {numMil[2]}')
            
            if numAra != 0:
                return numAra*1000 + romano_a_arabigo(numMil[2])

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

                distancia = simbolosOrdenados.index(letra) - \
                    simbolosOrdenados.index(ultimoCaracter)
                if distancia > 2:
                    return 0

                numArabigo -= valores.get(ultimoCaracter)*2
                numRepes = 1
        else:   # Si el simbolo romano no es correcto devolvemos Error
            return 0

        ultimoCaracter = letra

    return numArabigo


def arabigo_a_romano(numero):
    resultado = ''
    for item in numArabigosToRoman:
        cociente = numero // numArabigosToRoman.get(item)
        if cociente > 0:
            numero = numero - numArabigosToRoman.get(item)*cociente
            mayorTres = item*cociente
            if mayorTres == 'CCCC':
                resultado += 'CD'
            elif mayorTres == 'XXXX':
                resultado += 'XL'
            elif mayorTres == 'IIII':
                resultado += 'IV'
            else:
                resultado += mayorTres
            # print(f'Letra Romana {item}\'s--> {cociente}\t num Arabe--> {numRomanos.get(item)}')
    # print(f'Resultado al final --> {resultado}')
    return resultado


# ('(VII)CMXXIII'), 7923)
# ver = print(arabigo_a_romano(3999))
ver = print(romano_a_arabigo('((VII))CMXXIII'))
