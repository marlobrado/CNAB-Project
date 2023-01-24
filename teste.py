import chardet

with open('file.txt', 'rb') as f:
    result = chardet.detect(f.read())
    encodingType = result['encoding']


with open('file.txt', 'r', encoding=encodingType ) as file:
    lines = file.readlines()
    
    myList = []

    for line in lines:
    
        valorTransacao = 0
        if line[0] == '2' or line[0] == '3' or line[0] == '9':
            valorTransacao = -1 *(int(line[9:19]) / 100)
        else:
            valorTransacao = int(line[9:19]) / 100
    
    
        dadosLoja = {
            "tipo": line[0],
            "data": line[1:9],
            "valor": valorTransacao,
            "cpf": line[19:30],
            "cartao": line[30:42],
            "hora": line[42:48],
            "donoDaLoja": line[48:62].strip(),
            "nomeLoja": line[62:].strip(),
        }
        myList.append(dadosLoja)
    print(myList)

