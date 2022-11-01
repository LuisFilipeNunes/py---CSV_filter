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
    #print(data)
    field = input("Opção dessejada:")
    if field == int(1):
        search_value = input("Digite o valor desejado:")
        #TODO
    
reader_start()