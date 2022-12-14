import pandas as pd

#data = pd.read_csv("myFile0.csv")
#print(data) # debug

def reader_start():
    print("código para extração de dados do arquivo CSV")
    arqName = input("digite o nome do arquivo desejado:")
    arqToFind = arqName + ".csv"
    try:
        data = pd.read_csv(arqToFind)
    except:
        print("Ocorreu um erro!")
        #error handling TODO
    else: 
        print("Arquivo encontrado, leitura completa!")
        df = data
        df.columns = list(df)  # to put header inside data frame 
        #print(df)
        headers = list(df.columns) # to read header from data frame
        #print(var)
        reader_menu(data, headers)
def reader_menu(data, headers):
    
    print("Escolha qual campo a pesquisa será feita")
    n = 1
    for header in headers:
        print("Digite {number} para selecionar o campo '{header}' para a pesquisa.".format(number = n, header = header))
        n += 1
    ##
    ##filtered = data.query("profession == 'developer'")
    ##print(filtered)
    ##
    #print(data) 
    ##
    field = input("Opção desejada:")
    #print(headers[int(field)-1])
    print("A opção escolhida para a busca foi {header}".format(header = headers[int(field)-1]))
    

    reader_filter(data, field, headers)
def reader_filter(data, field, headers):
    valueToFind = input("Digite o que deseja procurar:")
    head = headers[int(field)-1]
    try:
        filtered = data.query("{heads} == @valueToFind".format(heads = head))
        #print(filtered)
    except Exception as e:
        print('Tem algum erro na sua busca, provavelmente não existe o que procura no arquivo em questão. :{0}'.format(e))
    else:
        filtered = data.query("{heads} == @valueToFind".format(heads = head))
    if filtered.empty:
        print("Sua pesquisa não obteve resultados...")
        reDo = input("Você deseja procurar no arquivo novamente? (S/N)")
        if reDo == "S":
            reader_start()
        elif reDo == "N":
            print("Okay, programa encerrado!")
            quit()
    print("Abaixo está o resultado de sua busca")
    print(filtered)
    choice = input("Você gostaria de exportar estes dados em um novo arquivo CSV? (S/N)")
    if choice == "S":
        reader_toCSV(filtered)
    elif choice == "N":
        print("Está certo!")
        reDo = input("Você deseja procurar no arquivo novamente? (S/N)")
        if reDo == "S":
            reader_start()
        elif reDo == "N":
            print("Okay, programa encerrado!")
def reader_toCSV(filtered):
    fileName = input("Por favor, digite o nome do arquivo que deseja criar: ")
    try:
        filtered.to_csv("./{name}.csv".format(name = fileName))
    except: 
        print("Houve algum erro!")
    else:
        filtered.to_csv("./{name}.csv".format(name = fileName))
    print("Arquivo Criado!")
    reDo = input("Você deseja procurar no arquivo novamente? (S/N)")
    if reDo == "S":
        reader_start()
    elif reDo == "N":
        print("Okay, programa encerrado!")
    
    

reader_start()