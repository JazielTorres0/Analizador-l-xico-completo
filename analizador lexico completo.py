def Menu():
    print("1. Agregar palabra al generador")
    print("2. Salir del programa")
    choice = input("Ingrese una opcion: ")
    if choice == '1':
        codigo = input("Ingrese el token: ")
        resultado = analizador_lexico(codigo)
        for token in resultado:
            print(token)
    elif choice == '2':
        print("Hasta luego. ")
    else:
        print("Opcion invalida. ")

def es_letra(c):
    return c.isalpha() #True

def es_digito(c):
    return c.isdigit() #False

def analizador_lexico(codigo):
    i = 0
    tokens = []

    while i < len(codigo):
        c = codigo[i]

        #ignorar espacios
        if c.isspace():
            i += 1
            continue

        #identificadores o palabras reservadas
        if es_letra(c):
            lexema = c
            i += 1
            while i < len(codigo) and (es_letra(codigo[i]) or es_digito(codigo[i])):
                lexema += codigo[i]
                i += 1

            if lexema in ["int", "float", "void"]:
                tokens.append((lexema, 4))
            elif lexema == "if":
                tokens.append((lexema, 19))
            elif lexema == "while":
                tokens.append((lexema, 20))
            elif lexema == "return":
                tokens.append((lexema, 21))
            elif lexema == "else":
                tokens.append((lexema, 22))
            else:
                tokens.append((lexema, 0))

            continue

        #numeros
        if es_digito(c):
            numero = c
            i += 1
            es_real = False

            while i < len(codigo) and es_digito(codigo[i]):
                numero += codigo[i]
                i += 1

            if i < len(codigo) and codigo[i] == '.':
                es_real = True
                numero += '.'
                i += 1
                while i < len(codigo) and es_digito(codigo[i]):
                    numero += codigo[i]
                    i += 1

            tokens.append((numero, 2 if es_real else 1))
            continue

        #operadores dobles
        if i + 1 < len(codigo):
            doble = codigo[i:i+2]
            if doble == "&&":
                tokens.append(("&&", 9))
                i += 2
                continue
            if doble == "||":
                tokens.append(("||", 8))
                i += 2
                continue
            if doble in ["<=", ">="]:
                tokens.append((doble, 7))
                i += 2
                continue
            if doble in ["==", "!="]:
                tokens.append((doble, 11))
                i += 2
                continue

        #operadores simples y símbolos
        if c in "+-":
            tokens.append((c, 5))
        elif c in "*/":
            tokens.append((c, 6))
        elif c in "<>":
            tokens.append((c, 7))
        elif c == "!":
            tokens.append((c, 10))
        elif c == "=":
            tokens.append((c, 18))
        elif c == ";":
            tokens.append((c, 12))
        elif c == ",":
            tokens.append((c, 13))
        elif c == "(":
            tokens.append((c, 14))
        elif c == ")":
            tokens.append((c, 15))
        elif c == "{":
            tokens.append((c, 16))
        elif c == "}":
            tokens.append((c, 17))
        elif c == "$":
            tokens.append((c, 23))
        else:
            print(f"Símbolo no reconocido: {c}")

        i += 1

    return tokens


Menu();