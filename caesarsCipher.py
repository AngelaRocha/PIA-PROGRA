def Encriptar(frase):
    abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
    }
    frase = frase.upper()
    FraseEnc = '' #str vacio
    for letra in frase: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
                            # if encontrado != True
            FraseEnc += letra
    print(FraseEnc)
    
def Desencriptar(frase):
    abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
    }
    frase = frase.upper()
    FraseDes = ''
    for letra in frase:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                FraseDes += x #fraseEnc.append(x)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseDes += letra
    print(FraseDes)

if __name__ == "__main__":
    try:
        print("Menú\n1) Encriptar\n2) Desencriptar\n3) Salir")
        x = int(input("Opción: "))
        if x == 3:
            exit()
        elif x == 1:
            frase = input('Frase en texto claro: ')
            frase = frase.upper()
            fraseEnc = Encriptar(frase)
            print(fraseEnc)
        elif x == 2:
            frase = input('Frase encriptada: ')
            frase = frase.upper()
            print(Desencriptar(frase))
        else:
            print("Opción no válida")
    except ValueError as a :
        print("Error! Opción no válida, " + str(a))

    
