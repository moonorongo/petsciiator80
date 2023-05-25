
# Esto deberia devolver una lista
# de 256 indices
# de 8 bytes cada uno

def get_charrom():
    chardata_list = list()
    f = open("characters-2.901447-10.bin", "rb")

    bCounter = 0
    totalCounter = 0
    characterData = list()

    for x in f.read():
        if(bCounter == 7): 
#            if(totalCounter < 1024):
            characterData.append(x)
#            else:
#                characterData.append(~x)

            chardata_list.append(characterData)
            bCounter = 0
            characterData = list()
        else:
            bCounter += 1
#            if(totalCounter < 1024):
            characterData.append(x)
#            else:
#                characterData.append(~x)

        totalCounter += 1
        
        if totalCounter == 1024:
            break 

    f.close()

    inverted_chardata_list = list()

    for c in chardata_list:
        cList = list()
        for b in c:
            cList.append(~b)

        inverted_chardata_list.append(cList)

    return chardata_list + inverted_chardata_list