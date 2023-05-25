import math

# obtiene los bytes correspondientes al pedazo recortado
# (el char actual)
def get_character_bytes(cropped_image):
    chardata_list = list(cropped_image.getdata(0))

    char_mapped_list = [0,0,0,0,0,0,0,0]

    for y in range(8):
        char_line_value = 0
        for x in range(8):
            value = 0 if (chardata_list[y*8 + x] == 0) else 1 
            char_line_value = char_line_value + (value * pow(2, 7 - x))
        char_mapped_list[y] = char_line_value
    
    #print(chardata_list)
    return char_mapped_list


# busca el caracter mas parecido a lo que le paso 
# como parametro
## TESTEAR ESTA GARCHA, con alguna imagen de ejemplo
# dos caracteres nada mas... algo asi
def findBestMatch(currentCharBytes, charRom):
    porcentaje_acumulado = 0

    promedio_porcentaje_maximo = 0
    bestCharIndex = 0

    for charIndex, char in enumerate(charRom):
        porcentaje_acumulado = 0
        
        for idx, charRomValue in enumerate(char):
            charValue = currentCharBytes[idx]
            bits_iguales = ~(charValue ^ charRomValue)

            total_bits_iguales = calc_total_iguales(bits_iguales)
            porcentaje_similaridad = total_bits_iguales / 8
            porcentaje_acumulado += porcentaje_similaridad
          
        promedio_porcentaje = porcentaje_acumulado / 8

        if (promedio_porcentaje > promedio_porcentaje_maximo):
            promedio_porcentaje_maximo = promedio_porcentaje
            bestCharIndex = charIndex
    
    return bestCharIndex


# suma el total de bits iguales
def calc_total_iguales(numero):
    total_bits = 0
    
    for potencia in range(8):
        bitNumber = 2 ** potencia
        if(numero & bitNumber != 0 ):
            total_bits += 1

    return total_bits